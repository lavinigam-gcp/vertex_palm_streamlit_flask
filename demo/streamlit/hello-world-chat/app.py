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
        message=message
    )
    return response.text

def clear_chat() -> None:
    st.session_state['generated'] = []
    st.session_state['past'] = []

def hard_reset_session() -> None: 
    st.session_state = {states : [] for states in st.session_state}


st.title("Vertex AI PaLM Chat API Demo")


#session states
def create_session_state():
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    if 'temperature' not in st.session_state:
        st.session_state['temperature'] = []
    if 'debug_mode' not in st.session_state:
        st.session_state['debug_mode'] = False
    if 'chat_input' not in st.session_state:
        st.session_state['chat_input'] = ''

def chat_input_submit():
    st.session_state.chat_input = st.session_state.chat_widget
    st.session_state.chat_widget = ''

def clear_duplicate_data():
    for i in range(len(st.session_state['past'])-1,0,-1):
        if st.session_state['past'][i][i] == st.session_state['past'][i-1][i-1]:
            del st.session_state['past'][i]
            del st.session_state['generated'][i]




#creating session states    
create_session_state()


#defining tabs 
# setting_tab, chat_tab = st.columns(2)


with st.container():
# with setting_tab:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Chat Settings:")
        if st.button("Clear Chat"):
            clear_chat()
        if st.button("Hard Reset"):
            hard_reset_session()
        debug_mode_choice = st.radio("debug mode ", (False,True))
        st.session_state['debug_mode'] = debug_mode_choice
    with col2:
        st.write("Model Settings:")
        temperature_value = st.slider('set temperature :', 0.0, 1.0, 0.2)
        st.session_state['temperature'].append(temperature_value)
    with col3:
        st.write("Current Settings: ")
        st.write ("Temperature: ",st.session_state['temperature'][-1])
        st.write ("Debug Model: ",st.session_state['debug_mode'])

with st.container():
# with chat_tab:
    #get the user input for chat
    
    user_input = st.text_input('Your message to the bot:', key='chat_widget', on_change=chat_input_submit)

    if st.session_state.chat_input:
        #call the vertex PaLM API and send the user input
        chat_model = create_session(temperature = temperature_value)
        bot_message = response(chat_model,st.session_state.chat_input)

        #store the output
        if st.session_state['past'][-1] != st.session_state.chat_input:
            st.session_state['past'].append(st.session_state.chat_input)
            st.session_state['generated'].append(bot_message)
        # clear_duplicate_data()
            

    #display generated response 
    if st.session_state['generated'] and st.session_state['past']:
        for i in range(len(st.session_state["generated"])-1,-1,-1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style='big-smile')
            message(st.session_state["generated"][i], key=str(i), avatar_style='bottts')

    if st.session_state['debug_mode']:
        st.write("len of generated response: ",len(st.session_state["generated"]))
        st.write(f'Last mssage to bot: {st.session_state.chat_input}')
        st.write(st.session_state)


