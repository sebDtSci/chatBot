import ollama

class generate():
    def __init__(self, model, prompt) -> None:
        self.model = model
        self.prompt = prompt
        self._ollama_option = {'temperature':1}
    
    def reponse(self)-> str:
        res =  ollama.generate(
            model = self.model,
            prompt= self.prompt,
            stream =False,
            options= self._ollama_option
        )
        print(res)
        return res['response']
        