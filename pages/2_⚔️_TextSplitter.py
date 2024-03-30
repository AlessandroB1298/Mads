import streamlit as st
from stream_lit_config import styles, animate_intro


def serve():
    styles()
    header = ("TextSplitting Agent")
    p = ("Hello, You can use the radial menu on the left to upload text/pdf files you wish to splt")
    animate_intro(header, p)
    
serve()