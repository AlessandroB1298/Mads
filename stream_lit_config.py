import streamlit as st
# Define the animation function for introduction
def animate_intro(header, p):
    st.markdown(
        """
        <style>
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        .intro-text {
            animation: fadeIn 2s ease-in-out;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <h1 class="intro-text" style="text-align: center;">{header}</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p class="bio" style="text-align: center;">{p}</p>
        """,
        unsafe_allow_html=True
    )

        


def styles():
    st.set_page_config(page_title="Chatbot", page_icon="💬")
    
    with open('./wave.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


