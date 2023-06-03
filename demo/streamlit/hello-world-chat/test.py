import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)

col3, col4 = st.columns(2)

with col3:
    if 'something' not in st.session_state:
        st.session_state.something = ''

    def submit():
        st.session_state.something = st.session_state.widget
        st.session_state.widget = ''

    user_input = st.text_input('Something', key='widget', on_change=submit)

    st.write(f'Last submission: {st.session_state.something}')

with col4:
    if 'something2' not in st.session_state:
        st.session_state.something2 = ''

    def submit2():
        st.session_state.something2 = st.session_state.widget2
        st.session_state.widget2 = ''

    user_input = st.text_input('Something 2', key='widget2', on_change=submit2)

    st.write(f'Last submission: {st.session_state.something2}')