import os
# from dotenv import load_dotenv
import time
import chromadb
from chromadb.config import Settings
from src.rag.document_reader import reader
from src.rag.enbedding import filtre_augmented
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

STORAGE_PATH="data/db"
if STORAGE_PATH is None:
    raise ValueError('STORAGE_PATH environment variable is not set')

# Initialize Chroma
# chromadb_client = chromadb.Client(Settings())
chromadb_client = chromadb.PersistentClient(path=STORAGE_PATH)
# collection = chromadb_client.create_collection("documentsTest")
collection = chromadb_client.get_or_create_collection(name = "documentsTest")


# Add documents
documents = reader("data/documents_to_rag")
contents = [doc["content"] for doc in documents]
ids = [doc["id"] for doc in documents]
collection.add(documents=contents,ids=ids)

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        if file_path.endswith((".docx", ".txt", ".pdf")):
            print(f"New file detected: {file_path}")
            # Parse the new document
            new_documents = reader(os.path.dirname(file_path))
            # Add the new document to ChromaDB
            collection.add(documents=[doc["content"] for doc in new_documents], ids=[doc["id"] for doc in new_documents])
            print(f"Added new document to the collection: {file_path}")

def monitor_directory(directory):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def rag_pipeline(query:str) ->str :
    # chroma enbed query grace à query_texts, c'est juste incroyable
    # res = collection.query(query_texts=query, n_results=5)
    # res_doc = res["documents"]
    # best_context = filtre_augmented(query, res_doc)

    # if best_context:
    #     print(f'Context Found ! {len(best_context)}')
    #     print('best cont ', best_context)
    #     return best_context
    # else :
    #     return ""

    res = collection.query(query_texts=query, n_results=5)
    print('res ', res)
    if res != None:
        res = res["documents"]
        context = "".join([j for i in res for j in i])
        print(f'Context Found ! {len(context)}')
        return context
    else :
        return ""

if __name__ == "__main__":
    monitor_directory("data/documents_to_rag")