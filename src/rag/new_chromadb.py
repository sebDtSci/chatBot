import os
import time
import chromadb
from chromadb.config import Settings
from src.rag.document_reader import reader
from src.rag.dataBase_gen import generate_embedding
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Initialize Chroma
chromadb_client = chromadb.Client(Settings(persistence=True, db_path="data/db",embedding_model="openai"))
collection = chromadb_client.create_collection("documents")

# Add documents
documents = reader("data/documents_to_rag")
collection.add(documents=documents["content"],ids=documents["id"])

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
    res = collection.query(query_texts=query, n_results=1)
    res = res["documents"]
    context = "".join([j for i in res for j in i])
    return context

if __name__ == "__main__":
    monitor_directory("data/documents_to_rag")