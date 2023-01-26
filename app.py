import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1/1176.png", width=100)
st.sidebar.subheader("About the Extractor Engine:")
st.sidebar.markdown("##### This tool allows querying the text retrieved from the URL using OpenAI’s [text-davinci-003] engine")
st.sidebar.markdown("##### The URL text can be referenced in the prompt as “following text”")

st.sidebar.subheader("How to use:")
st.sidebar.markdown("##### Kindly provide a prompt with the request, the url for text retrieval, OpenAI api-key and temperature to process the text")

st.sidebar.subheader("About the GPT-3 Model:")
st.sidebar.markdown("##### Davinci is the most capable model in GPT-3 and can do anything that any other model can do, and much more—often with fewer instructions")
st.sidebar.markdown("Davinci is able to solve logic problems, determine cause and effect, understand the intent of text, produce creative content, explain character motives, and handle complex summarization tasks")

st.sidebar.subheader("Powered by")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/1280px-OpenAI_Logo.svg.png", width=150)

st.sidebar.caption("Streamlit App by </Shahnab>")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-information-extraction-with-chat-c0a48ea.hf.space", width=1100, height=650, scrolling=True)
