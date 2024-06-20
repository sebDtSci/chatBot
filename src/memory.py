from transformers import pipeline

class ChatbotMemory:
    def __init__(self, conv:list = []):
        self.conversation_history = conv

    def update_memory(self, user_input, bot_response):
        self.conversation_history.append(f"'user': {user_input}, 'bot': {bot_response}")

    def get_memory(self):
        return self.conversation_history
    
    def get_compressed_memory(sentence:str)->str:
        summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
        summary = summarizer(sentence, max_length=50, min_length=5, do_sample=False)
        return summary[0]['summary_text']

    def compressed_memory(conv_hist:list)->list:
        return [ChatbotMemory.get_compressed_memory(sentence) for sentence in conv_hist]
        

    def memory_counter(conv_hist:list)->int:
        st = ''.join(conv_hist)
        return len(st.split())


