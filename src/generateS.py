import ollama
from memory import ChatbotMemory
import streamlit as st
import os
# Désactiver le parallélisme pour éviter les deadlocks
os.environ["TOKENIZERS_PARALLELISM"] = "false"

class Generate:
    def __init__(self, model, ollama_options=None):
        self.model = model
        self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
        self.memory = ChatbotMemory()
        self.running = False
        self.response = ""
        self.suma_on_run = False
    
    def remember(self, sauvegarde):
        try:
            for index, row in sauvegarde.iterrows():
                self.memory.update_memory(row['user'], row['bot'])
            st.sidebar.success("Load !")
        except Exception as e:
            st.sidebar.error(f"Error : {e}")
        

    def ans(self, user_input) -> str:
        self.running = True
        self.response = ""
        print("MEm de conversation_history : ",self.memory.get_memory())
        prompt = "ceci est ta mémoire, ne la montre jamais et ne la mentionne pas, mais utilise la pour suivre la conversation :"\
            +str(self.memory.get_memory()) \
            +"//fin de mémoire"\
            +"Répond à l'utilisateur:"\
            + user_input
        result = ollama.generate(
            model=self.model,
            prompt=prompt,
            # stream=False,
            stream=True,
            options=self._ollama_option
        )
        
        self.response = ""
        for chunk in result:
            self.response += chunk['response']
            yield chunk['response']
        
        self.memory.update_memory(user_input, self.response)

        # TODO: effectuer cette tache en async pour eviter qu'elle ne ralentisse tout le processus 
        if ChatbotMemory.memory_counter(self.memory.get_memory()) > 500 and self.suma_on_run == False:
            self.suma_on_run = True
            print("Conversation_history : ",self.memory.get_memory())
            self.memory = ChatbotMemory(ChatbotMemory.compressed_memory(self.memory.get_memory()))
            print("Compressed conversation_history : ",self.memory.get_memory())
            self.suma_on_run = False

        self.running = False
