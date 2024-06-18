import ollama
from memory import ChatbotMemory
from transformers import pipeline

class Generate():
    def __init__(self, model, prompt:str, inputMem:str, outputMem:str ) -> None:
        self.model = model
        self.prompt = prompt
        self._ollama_option:dict = {'temperature':1}
        self.inputMem = inputMem
        self.outputMem = outputMem
        self.running = False
        self.response = ""
        self.memory = ChatbotMemory()
    
    def _write_mem(self):
        with open(self.outputMem, "w", encoding='utf-8') as file:
            file.write(self.response)
    
    def _read_mem(self):
        with open(self.inputMem, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        res = []
        for line in lines:
            role = line.split(' ')[0]
            content = line[len(role)+1:].strip()
            content = content.replace("/n","\n")
            res.append({"role":role, "content":content})
            
        return res

    def _getPrompt(self):
        prompts = self._read_mem() 
        prompts.append({"role": "user", "content": self.prompt})
        return " ".join([p['content'] for p in prompts])
    
    def _summarizer(self):
        summarizer = pipeline("summarization")
        summary = summarizer(self.response, max_length=130, min_length=5, do_sample=False)
        return summary[0]['summary_text']
            
    def ans(self)-> str:
        self.running = True
        self.response = ""
        answer =  ollama.generate(
            model = self.model,
            prompt= self._getPrompt(),
            stream =False,
            options= self._ollama_option
        )
        self.response = answer['response']
        print(self.response)
        self.memory.update_memory('last_response', self._summarizer())
        self._write_mem()
        self.running = False
        return self.response