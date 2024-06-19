import ollama
from src.memory import ChatbotMemory
import streamlit as st

class Generate:
    def __init__(self, model, ollama_options=None):
        self.model = model
        self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
        self.memory = ChatbotMemory()
        self.running = False
        self.response = ""
    
    def remember(self, sauvegarde):
        try:
            for lines in sauvegarde:
                self.memory.update_memory(lines['user'], lines['bot'])
            st.success("Load !")
        except Exception as e:
            st.error(f"Error : {e}")
        

    def ans(self, user_input) -> str:
        self.running = True
        self.response = ""
        print(self.memory.get_memory())
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
        
        ## Stream False:
        
        # self.response = result['response']
        # self.memory.update_memory(user_input, self.response)
        # self.running = False
        # return self.response
        
        ## Stream True:
        
        self.response = ""
        for chunk in result:
            self.response += chunk['response']
            yield chunk['response']
        
        self.memory.update_memory(user_input, self.response)
        self.running = False