import streamlit as st
from generateS import Generate

def main():
    st.title("Chatbot Interface with Memory")
    
    # Options de modèles disponibles
    model_options = ["aya:35b", "model2", "model3"]
    selected_model = st.selectbox("Choisissez le modèle", model_options)
    
    if "chatbot" not in st.session_state or st.session_state.model_name != selected_model:
        st.session_state.chatbot = Generate(model=selected_model)
        st.session_state.model_name = selected_model
    
    chatbot = st.session_state.chatbot

    if "history" not in st.session_state:
        st.session_state.history = []

    # Affichage de l'historique des conversations en ordre inversé
    for chat in reversed(st.session_state.history):
        user_message = f"""
        <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
            <b>Vous:</b> {chat['user']}
        </div>
        """
        bot_message = f"""
        <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
            <b>Stem:</b> {chat['bot']}
        </div>
        """
        st.markdown(bot_message, unsafe_allow_html=True)
        st.markdown(user_message, unsafe_allow_html=True)
    
    # Espace de saisie et bouton d'envoi en bas de la page
    user_input = st.text_input("Vous:", key="input")
    
    if st.button("Envoyer"):
        if user_input:
            response_generator = chatbot.ans(user_input)
            response = ""
            response_placeholder = st.empty()

            for chunk in response_generator:
                response += chunk
                response_placeholder.markdown(f"""
                <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
                    <b>Stem:</b> {response}
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.history.append({"user": user_input, "bot": response})

if __name__ == "__main__":
    main()



# import streamlit as st
# from generateS import Generate

# def main():
#     st.title("Chatbot Interface with Memory")
    
#     model_name = "aya:35b" 

#     if "chatbot" not in st.session_state:
#         st.session_state.chatbot = Generate(model=model_name)
    
#     chatbot = st.session_state.chatbot

#     if "history" not in st.session_state:
#         st.session_state.history = []

#     user_input = st.text_input("You:", key="input")

#     if st.button("Send"):
#         if user_input:
#             response_generator = chatbot.ans(user_input)
#             response = ""
#             response_placeholder = st.empty()

#             for chunk in response_generator:
#                 response += chunk
#                 response_placeholder.markdown(f"""
#                 <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                     <b>Stem:</b> {response}
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             st.session_state.history.append({"user": user_input, "bot": response})

#     for chat in reversed(st.session_state.history):
#         user_message = f"""
#         <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
#             <b>Vous:</b> {chat['user']}
#         </div>
#         """
#         # bot_message = f"""
#         # <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#         #     <b>Stem:</b> {chat['bot']}
#         # </div>
#         # """
#         # st.markdown(bot_message, unsafe_allow_html=True)
#         st.markdown(user_message, unsafe_allow_html=True)
        

# if __name__ == "__main__":
#     main()


# def main():
#     st.title("Chatbot Interface with Memory")
    
#     model_name = "aya:35b" 

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
#         user_message = f"""
#         <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
#             <b>Vous:</b> {chat['user']}
#         </div>
#         """
#         bot_message = f"""
#         <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#             <b>Stem:</b> {chat['bot']}
#         </div>
#         """
#         st.markdown(bot_message, unsafe_allow_html=True)
#         st.markdown(user_message, unsafe_allow_html=True)
        

# if __name__ == "__main__":
#     main()
