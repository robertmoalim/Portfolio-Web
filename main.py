import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.png", width=200)

with col2:
    st.title("Robert Moalim")
    content = """
    Hi, I am Robert! I am a inspiring Python programmer. I graduated in 2020 in International Business & Trade and I have done diverse programming courses.
    I have worked with ........., such as,............ If you have any questions about me feel free to contact me!
    """
    st.info(content)

    content2 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
    st.write(content2)