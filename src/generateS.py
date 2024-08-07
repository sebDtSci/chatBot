import ollama
import logging
from src.memory import ChatbotMemory, memory_counter, compressed_memory
from src.rag.new_chromadb import rag_pipeline
import streamlit as st
import os


# Désactiver le parallélisme pour éviter les deadlocks
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Param logger
logging.basicConfig(filename="app.log" , filemode="w", level=logging.DEBUG)

class Generate:
    def __init__(self, model:str="openchat:latest", ollama_options=None):
        self.model = model
        self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
        self.memory = ChatbotMemory()
        self.running = False
        self.response = ""
        self.suma_on_run = False
    
    def remember(self, sauvegarde)-> None:
        """
        Updates the Chatbot's memory with user-bot interactions from the provided sauvegarde DataFrame.

        Args:
            sauvegarde: DataFrame containing user-bot interaction data.

        Returns:
            None
        """

        try:
            for index, row in sauvegarde.iterrows():
                self.memory.update_memory(row['user'], row['bot'])
            st.sidebar.success("Load !")
        except Exception as e:
            st.sidebar.error(f"Error : {e}")
        
    def ans(self, user_input="l'assurance de manon qui à 34 ans et qui habite à paris"): # Debug modification
        """
        Generates a response from the Chatbot based on the user input and updates the Chatbot's memory.

        Args:
            user_input: The input provided by the user.

        Returns:
            str: The response generated by the Chatbot.
        """
        # Initialisation
        self.running = True
        self.response = ""
        print("MEm de conversation_history : ",self.memory.get_memory())
        context = rag_pipeline(query=user_input)
        prompt = (
            "Vous êtes un assistant intelligent. Utilisez les informations suivantes pour aider l'utilisateur.\n\n"
            "Mémoire du chatbot (à ne pas montrer à l'utilisateur) :\n"
            f"{self.memory.get_memory()}\n\n"
            "Contexte pertinent :\n"
            f"{context}\n\n"
            "Question de l'utilisateur :\n"
            f"{user_input}\n\n"
            "Répondez de manière claire et concise :\n"
        )
        result = ollama.generate(
            model=self.model,
            prompt=prompt,
            # stream=False,
            stream=True,
            options=self._ollama_option
        )
        print(f"Response generated. with model : {self.model}")
        logging.info(f"Response generated. with model : {self.model}")
        
        self.response = ""
        for chunk in result:
            self.response += chunk['response']
            yield chunk['response']
        
        self.memory.update_memory(user_input, self.response)

        # TODO: effectuer cette tache en async pour eviter qu'elle ne ralentisse tout le processus 
        if memory_counter(self.memory.get_memory()) > 500 and self.suma_on_run == False:
            self.suma_on_run = True
            print("Conversation_history : ",self.memory.get_memory())
            self.memory = ChatbotMemory(compressed_memory(self.memory.get_memory()))
            print("Compressed conversation_history : ",self.memory.get_memory())
            self.suma_on_run = False
            logging.info("Memory compressed.")

        self.running = False
