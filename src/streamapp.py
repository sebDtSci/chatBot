# import streamlit as st
# from generateS import Generate

# def main():
#     st.title("Chatbot Interface with Memory")
    
#     model_options = ["aya:35b", "openchat:latest", "llama3:latest"]
#     selected_model = st.selectbox("Choisissez le modèle", model_options)

#     if "chatbot" not in st.session_state or st.session_state.model_name != selected_model:
#         st.session_state.chatbot = Generate(model=selected_model)
#         st.session_state.model_name = selected_model
    
#     chatbot = st.session_state.chatbot

#     if "history" not in st.session_state:
#         st.session_state.history = []

#     # CSS pour fixer la zone de saisie en bas de la page
#     # st.markdown(
#     #     """
#     #     <style>
#     #     .fixed-bottom {
#     #         position: fixed;
#     #         bottom: 0;
#     #         left: 0;
#     #         width: 100%;
#     #         background: white;
#     #         padding: 10px;
#     #         box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
#     #     }
#     #     .chat-history {
#     #         padding-bottom: 100px; /* Espace en bas pour la zone de saisie */
#     #     }
#     #     </style>
#     #     """, unsafe_allow_html=True
#     # )

#     # Affichage de l'historique des conversations avec espace en bas
#     st.markdown('<div class="chat-history">', unsafe_allow_html=True)
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
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Zone de saisie fixée en bas
#     st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
#     user_input = st.text_input("You:", key="input")
#     if st.button("Send") and user_input:
#         # Afficher le message de l'utilisateur immédiatement
#         st.session_state.history.append({"user": user_input, "bot": ""})
#         st.experimental_rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Gestion des réponses du chatbot après l'envoi du message
#     if st.session_state.history and st.session_state.history[-1]["bot"] == "":
#         user_input = st.session_state.history[-1]["user"]
#         response_generator = chatbot.ans(user_input)
#         response = ""
#         response_placeholder = st.empty()

#         for chunk in response_generator:
#             response += chunk
#             response_placeholder.markdown(f"""
#             <div style="text-align: left; background-color: #BLUE; padding: 10px; border-radius: 10px; margin: 10px 0;">
#                 <b>Stem:</b> {response}
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.session_state.history[-1]["bot"] = response
#         st.experimental_rerun()

# if __name__ == "__main__":
#     main()

##########################################################################################################################################################################
import streamlit as st
from generateS import Generate

def main():
    st.title("Chatbot Interface with Memory")
    
    model_options = ["aya:35b", "openchat:latest", "llama3:latest"]
    selected_model = st.selectbox( f""" 
                                  background-color: red
                                  "Choisissez le modèle" 
                                  """, model_options)

    if "chatbot" not in st.session_state or st.session_state.model_name != selected_model:
        st.session_state.chatbot = Generate(model=selected_model)
        st.session_state.model_name = selected_model
    
    chatbot = st.session_state.chatbot

    if "history" not in st.session_state:
        st.session_state.history = []

    

    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input:
        # Afficher le message de l'utilisateur immédiatement
        st.session_state.history.append({"user": user_input, "bot": ""})
        st.experimental_rerun()

    # Gestion des réponses du chatbot après l'envoi du message
    if st.session_state.history and st.session_state.history[-1]["bot"] == "":
        user_input = st.session_state.history[-1]["user"]
        response_generator = chatbot.ans(user_input)
        response = ""
        response_placeholder = st.empty()

        for chunk in response_generator:
            response += chunk
            response_placeholder.markdown(f"""
            <div style="text-align: left; background-color: blue; padding: 10px; border-radius: 10px; margin: 10px 0;">
                <b>Stem:</b> {response}
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.history[-1]["bot"] = response
        st.experimental_rerun()
    
    # Affichage de l'historique des conversations
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
