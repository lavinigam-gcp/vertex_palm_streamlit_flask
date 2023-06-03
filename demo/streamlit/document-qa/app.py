import streamlit as st
from vertexai.preview.language_models import ChatModel, InputOutputTextPair, ChatSession, TextGenerationModel
import vertexai
from streamlit_chat import message

PROJECT_ID = "cloud-llm-preview1"
vertexai.init(project=PROJECT_ID, location="us-central1")