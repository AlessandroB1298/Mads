import streamlit as st
from stream_lit_config import styles, animate_intro



def list():
    styles()

    header = "Grocery List splitter and Organizer"
    p = "This page allows you to split and organize your list then print it out or share it on your phone"
    animate_intro(header, p)
list()