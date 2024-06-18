import ollama
from memory import ChatbotMemory

class Generate:
    def __init__(self, model, ollama_options=None):
        self.model = model
        self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
        self.memory = ChatbotMemory()
        self.running = False
        self.response = ""

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
            stream=False,
            options=self._ollama_option
        )
        self.response = result['response']
        self.memory.update_memory(user_input, self.response)
        # self.memory.update_memory('last_response', self.response)
        self.running = False
        return self.response

# import ollama
# from memory import ChatbotMemory

# class Generate:
#     def __init__(self, model, ollama_options=None):
#         self.model = model
#         self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
#         self.memory = ChatbotMemory()
#         self.running = False
#         self.response = ""

#     def ans(self, user_input) -> str:
#         self.running = True
#         self.response = ""
#         result = ollama.generate(
#             model=self.model,
#             prompt=user_input,
#             stream=False,
#             options=self._ollama_option
#         )
#         self.response = result['response']
#         self.memory.add_conversation(user_input, self.response)
#         self.memory.update_memory('last_response', self.response)
#         self.running = False
#         return self.response