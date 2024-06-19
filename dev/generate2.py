import ollama
from transformers import pipeline
from src.memory import ChatbotMemory

class Generate:
    def __init__(self, model, prompt, ollama_options=None):
        self.model = model
        self._ollama_option = ollama_options if ollama_options else {'temperature': 1}
        self.memory = ChatbotMemory()
        self.summarizer = pipeline("summarization")
        self.running = False
        self.response = ""
        self.prompt = prompt

    def _summarizer(self, text):
        summary = self.summarizer(text, max_length=130, min_length=5, do_sample=False)
        return summary[0]['summary_text']

    # def ans(self, user_input) -> str:
    def ans(self) -> str:
        self.running = True
        self.response = ""
        result = ollama.generate(
            model=self.model,
            prompt=self.prompt,
            stream=False,
            options=self._ollama_option
        )
        self.response = result['response']
        summarized_response = self._summarizer(self.response)
        self.memory.add_conversation(self.prompt, summarized_response)
        self.memory.update_memory('last_response', summarized_response)
        self.running = False
        return summarized_response