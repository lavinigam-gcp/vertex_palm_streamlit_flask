import streamlit as st
from vertexai.preview.language_models import ChatModel, InputOutputTextPair, ChatSession, TextGenerationModel
import vertexai
from streamlit_chat import message

PROJECT_ID = "cloud-llm-preview1"
vertexai.init(project=PROJECT_ID, location="us-central1")

def create_session(temperature=0.2,
                   max_output_tokens=256,
                   top_k=40,
                   top_p=.80,
                   context="",
                   examples_for_context=[], 
                   ):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
        "top_k": top_k,
        "top_p": top_p,
        "context": context,
        "examples": examples_for_context
    }
    # st.write("its using this temperature values for reference = ",temperature)
    chat = ChatSession(model=chat_model, **parameters)
    return chat


def response(chat, message):
    response = chat.send_message(
        message=message, max_output_tokens=256, temperature=0.2, top_k=40, top_p=0.8
    )
    return response.text

def clear_chat() -> None:
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.messages = []
    st.session_state.user_text = ""

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


st.title("Vertex AI PaLM Chat API Demo")



tab1, tab2 = st.tabs(["General Bot","ByoB"]) 


with tab1: 
    if st.button("Clear Chat"):
        clear_chat()

    with st.container():
        st.write (" ")
        temperature_value = st.slider('set temperature :', 0.0, 1.0, 0.2)
        st.write ("temperature is : ",temperature_value)

    #storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

 

    with st.container():
        user_input=st.text_input("You:",key='input')
        if user_input:
            chat_model = create_session(temperature = temperature_value)
            bot_message = response(chat_model,user_input)
            # st.write(bot_message)
            output=bot_message
            #store the output
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    with st.container():
        if st.session_state['generated']:
            for i in range(len(st.session_state["generated"])-1,0,-1):
                # st.write(i)
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style='big-smile')
                message(st.session_state["generated"][i], key=str(i), avatar_style='bottts')
                






# experimental 
# user_input = get_text()

# if user_input:
#     output = query({
#         "inputs": {
#             "past_user_inputs": st.session_state.past,
#             "generated_responses": st.session_state.generated,
#             "text": user_input,
#         },"parameters": {"repetition_penalty": 1.33},
#     })

#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output["generated_text"])

# if st.session_state['generated']:

#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
# generation_model = TextGenerationModel.from_pretrained("text-bison@001")


# st.title("PaLM 2 Demo - Question Answering with multiple, large documents")

# st.sidebar.button("Method 1")
# prompt = "What is a large language model?"
# response = generation_model.predict(prompt=prompt)
# st.write(response.text)

# st.write(st.session_state["generated"])
# st.write(st.session_state["past"])
# if st.session_state['generated']:
#     for i in range(0, len(st.session_state["generated"]), 1):
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style='personas')
#         message(st.session_state['generated'][i], key=str(i), avatar_style='identicon')
# AvatarStyle = Literal[
#     "adventurer",
#     "adventurer-neutral",
#     "avataaars",
#     "avataaars-neutral",
#     "big-ears",
#     "big-ears-neutral",
#     "big-smile",
#     "bottts",
#     "bottts-neutral",
#     "croodles",
#     "croodles-neutral",
#     "fun-emoji",
#     "icons",
#     "identicon",
#     "initials",
#     "lorelei",
#     "lorelei-neutral",
#     "micah",
#     "miniavs",
#     "open-peeps",
#     "personas",
#     "pixel-art",
#     "pixel-art-neutral",
#     "shapes",
#     "thumbs",
# ]
# chat_placeholder = st.empty()

# with chat_placeholder.container():
#     for i in range(len(st.session_state['generated'])):                
#         message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
#         message(st.session_state['generated'][i], key=f"{i}")
    
#     st.button("Clear message", on_click=on_btn_click)

# with st.container():
#     user_input=st.text_input("User Input:", key='input')
#     if user_input:
#         chat_model = create_session()
#         bot_message = response(chat_model,user_input)
#         # st.write(bot_message)
#         output=bot_message
#         #store the output
#         st.session_state['past'].append(user_input)
#         st.session_state['generated'].append(output)

# [
#             InputOutputTextPair(
#                 input_text="How many moons does Mars have?",
#                 output_text="The planet Mars has two moons, Phobos and Deimos.",
#             ),
#         ],