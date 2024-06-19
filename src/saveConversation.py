import pandas as pd
from datetime import datetime

def save_conversation(title, history):
    conversation = ""
    for chat in history:
        conversation += f"Vous: {chat['user']}\nStem: {chat['bot']}\n"
    
    data = {
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Titre": [title],
        "Conversation": [conversation]
    }
    df = pd.DataFrame(data)
    
    try:
        # Append mode ('a'), header only if the file does not already exist
        df.to_csv("conversations.csv", mode='a', header=not pd.io.common.file_exists("conversations.csv"), index=False)
        st.success("Conversation sauvegardée avec succès !")
    except Exception as e:
        st.error(f"Erreur lors de la sauvegarde de la conversation: {e}")
        
def load_conversations():
    try:
        return pd.read_csv("conversations.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Titre", "Conversation"])