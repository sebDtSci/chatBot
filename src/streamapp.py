import streamlit as st
from generateS import Generate
from saveConversation import save_conversation, load_conversations
from memory import ChatbotMemory

def main():
    st.title("Chatbot Interface with Memory")
    
    model_options = ["aya:35b", "openchat:latest", "llama3:latest"]
    selected_model = st.selectbox("Choisissez le modèle" , model_options)

    if "chatbot" not in st.session_state or st.session_state.model_name != selected_model:
        st.session_state.chatbot = Generate(model=selected_model)
        st.session_state.model_name = selected_model
    
    chatbot = st.session_state.chatbot

    if "history" not in st.session_state:
        st.session_state.history = []

    # Charger les conversations sauvegardées
    conversations_df = load_conversations()
    st.sidebar.title("Conversations sauvegardées")
    conversation_titles = conversations_df["Titre"].tolist()
    selected_conversation = st.sidebar.selectbox("Sélectionnez une conversation", conversation_titles)
    if st.sidebar.button("Load") and selected_conversation:
        # conversation_data = conversations_df[conversations_df["Titre"] == selected_conversation]["Conversation"].values[0]
        chatbot.remember(conversations_df)
        # st.sidebar.text_area("Conversation", conversation_data, height=400)
    

    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        # Afficher le message de l'utilisateur immédiatement
        st.session_state.history.append({"user": user_input, "bot": ""})
        # st.experimental_rerun()
        st.rerun()

    # Gestion des réponses du chatbot après l'envoi du message
    if st.session_state.history and st.session_state.history[-1]["bot"] == "":
        user_input = st.session_state.history[-1]["user"]
        response_generator = chatbot.ans(user_input)
        response = ""
        response_placeholder = st.empty()

        for chunk in response_generator:
            response += chunk
            response_placeholder.markdown(f"""
            <div style="text-align: left; background-color: #229954 ; padding: 10px; border-radius: 10px; margin: 10px 0;">
                <b>Stem:</b> {response}
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.history[-1]["bot"] = response
        # st.experimental_rerun()
        st.rerun()
    
    # Affichage de l'historique des conversations
    for chat in reversed(st.session_state.history):
        user_message = f"""
        <div style="text-align: right; padding: 10px; margin: 10px 0;">
            <div><b>Vous:</b></div>
            <div style="background-color: #GREEN; border-radius: 10px; padding: 10px;">
                {chat['user']}
            </div>
        </div>
        """
        bot_message = f"""
        <div style="text-align: left; padding: 10px; margin: 10px 0;">
            <div><b>Stem:</b></div>
            <div style="background-color: #BLUE; border-radius: 10px; padding: 10px;">
                {chat['bot']}
            </div>
        </div>
        """
        # user_message = f"""
        # <div style="text-align: right; background-color: #2471A3; padding: 10px; border-radius: 10px; margin: 10px 0;">
        #     <b>Vous:</b> {chat['user']}
        # </div>
        # """
        # bot_message = f"""
        # <div style="text-align: left; background-color: #229954 ; padding: 10px; border-radius: 10px; margin: 10px 0;">
        #     <b>Stem:</b> {chat['bot']}
        # </div>
        # """
        st.markdown(bot_message, unsafe_allow_html=True)
        st.markdown(user_message, unsafe_allow_html=True)

    save_title = st.text_input("Sauvegarder la conversation en tant que :", key="save_title")
    if st.button("Save") and save_title:
        save_conversation(save_title, st.session_state.history)
        
    
if __name__ == "__main__":
    main()
###################################################################################################################################################################
# import streamlit as st
# from generateS import Generate
# import logging

# def main():
#     st.title("Chatbot Interface with Memory")
    
#     # model_name = "aya:35b"
#     model_options = ["aya:35b", "openchat:latest", "llama3:latest"]
#     selected_model = st.selectbox("Choisissez le modèle", model_options)

#     # if "chatbot" not in st.session_state:
#     #     st.session_state.chatbot = Generate(model=selected_model)
#     if "chatbot" not in st.session_state or st.session_state.model_name != selected_model:
#         st.session_state.chatbot = Generate(model=selected_model)
#         st.session_state.model_name = selected_model
    
#     chatbot = st.session_state.chatbot

#     if "history" not in st.session_state:
#         st.session_state.history = []

#     user_input = st.text_input("You:", key="input")
    

#     if st.button("Send"):
#         if user_input:
#             response_generator = chatbot.ans(user_input)
#             response = ""
#             response_placeholder = st.empty()
            
#             # écrit le message de l'utilisateur dans le streamlit
#         elif st.session_state.history == []:
#             user_message = f"""
#             <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                 <b>Vous:</b> {user_input}
#             </div>
#             """
#             st.markdown(user_message, unsafe_allow_html=True)
#         else:
#             for chat in reversed(st.session_state.history):
#                 user_message = f"""
#                 <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                     <b>Vous:</b> {chat['user']}
#                 </div>
#                 """
#                 # bot_message = f"""
#                 # <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                 #     <b>Stem:</b> {chat['bot']}
#                 # </div>
#                 # """
#                 # st.markdown(bot_message, unsafe_allow_html=True)
#                 st.markdown(user_message, unsafe_allow_html=True)
                

#             for chunk in response_generator:
#                 response += chunk
#                 response_placeholder.markdown(f"""
#                 <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                     <b>Stem:</b> {response}
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             st.session_state.history.append({"user": user_input, "bot": response})

#     # for chat in reversed(st.session_state.history):
#     #     user_message = f"""
#     #     <div style="text-align: right; background-color: #GREEN; padding: 10px; border-radius: 10px; margin: 10px 0;">
#     #         <b>Vous:</b> {chat['user']}
#     #     </div>
#     #     """
#     #     bot_message = f"""
#     #     <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#     #         <b>Stem:</b> {chat['bot']}
#     #     </div>
#     #     """
#     #     st.markdown(bot_message, unsafe_allow_html=True)
#     #     st.markdown(user_message, unsafe_allow_html=True)
        

# if __name__ == "__main__":
#     main()

## Stream False:

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
