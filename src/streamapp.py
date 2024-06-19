import streamlit as st
from generateS import Generate

def main():
    st.title("Chatbot Interface with Memory")
    
    model_name = "aya:35b"  # Remplacez par le nom de votre modèle

    # Initialiser le chatbot dans st.session_state si ce n'est pas déjà fait
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = Generate(model=model_name)
    
    chatbot = st.session_state.chatbot

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("You:", key="input")

    if st.button("Send"):
        if user_input:
            response = chatbot.ans(user_input)
            st.session_state.history.append({"user": user_input, "bot": response})

    # Affichage de l'historique des conversations en ordre inversé
    for chat in reversed(st.session_state.history):
        user_message = f"""
        <div style="text-align: left; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
            <b>Vous:</b> {chat['user']}
        </div>
        """
        bot_message = f"""
        <div style="text-align: right; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
            <b>Stem:</b> {chat['bot']}
        </div>
        """
        st.markdown(user_message, unsafe_allow_html=True)
        st.markdown(bot_message, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



# import streamlit as st
# from generateS import Generate

# def main():
#     st.title("Chatbot Interface with Memory")
    
#     model_name = "aya:35b"  # Remplacez par le nom de votre modèle

#     # Initialiser le chatbot dans st.session_state si ce n'est pas déjà fait
#     if "chatbot" not in st.session_state:
#         st.session_state.chatbot = Generate(model=model_name)
    
#     chatbot = st.session_state.chatbot

#     if "history" not in st.session_state:
#         st.session_state.history = []

#     user_input = st.text_input("You:", key="input")

#     if st.button("Send"):
#         if user_input:
#             response = chatbot.ans(user_input)
#             st.session_state.history.append({"user": user_input, "bot": response})

#     # Affichage de l'historique des conversations en ordre inversé
#     for chat in reversed(st.session_state.history):
#         st.write(f"**User**: {chat['user']}")
#         st.write(f"**Bot**: {chat['bot']}")

# if __name__ == "__main__":
#     main()



# import streamlit as st
# from generateS import Generate

# def main():
#     st.title("Chatbot Interface with Memory")
    
#     model_name = "aya:35b"  # Remplacez par le nom de votre modèle

#     # Initialiser le chatbot dans st.session_state si ce n'est pas déjà fait
#     if "chatbot" not in st.session_state:
#         st.session_state.chatbot = Generate(model=model_name)
    
#     chatbot = st.session_state.chatbot

#     if "history" not in st.session_state:
#         st.session_state.history = []

#     user_input = st.text_input("You:", key="input")

#     if st.button("Send"):
#         if user_input:
#             response = chatbot.ans(user_input)
#             st.session_state.history.append({"user": user_input, "bot": response})

#     if st.session_state.history:
#         for chat in st.session_state.history:
#             st.write(f"**User**: {chat['user']}")
#             st.write(f"**Bot**: {chat['bot']}")

# if __name__ == "__main__":
#     main()