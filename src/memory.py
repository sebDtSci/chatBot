class ChatbotMemory:
    def __init__(self):
        self.conversation_history = []

    def update_memory(self, user_input, bot_response):
        self.conversation_history.append(f"'user': {user_input}, 'bot': {bot_response}")

    def get_memory(self):
        return self.conversation_history
