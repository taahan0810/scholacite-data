import os
import streamlit as st
import numpy as np
import glob

st. set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = 0 

# curr_page = 0

if __name__ == '__main__':
    path = os.getcwd() + '/streamlit'

    colab = []
    original = []
    gpt = []

    but1,but2,but3 = st.columns([10,1,1])


    for paper in os.listdir(path):
        colab.append(open(path + '/' + paper + '/colab.txt').read())
        original.append(open(path + '/' + paper + '/original.txt').read())
        gpt.append(open(path + '/' + paper + '/gpt.txt').read())

    no_of_pages = len(colab)
    # buttons for navigation
    with but1:
        if st.button('Previous'):
            st.session_state["page"] -= 1
            st.session_state["page"] += (no_of_pages)
            st.session_state["page"] %= no_of_pages
            st.session_state["page"] = st.session_state["page"]
    with but3:
        if st.button('Next'):
            st.session_state["page"] += 1
            st.session_state["page"] %= no_of_pages
            st.session_state["page"] = st.session_state["page"]

    # columns for gpt,original, collab sections
    col1,col2,col3 = st.columns(3)

    print(f"{st.session_state["page"]=}")

    with col1:
        st.subheader('GPT-Assisted Section')
        # st.write(colab[0])
        st.write(colab[st.session_state["page"]])
    with col2:
        st.subheader('Original Section')
        # st.write(original[0])
        st.write(original[st.session_state["page"]])
    with col3:
        st.subheader('GPT-Generated Section')
        # st.write(gpt[0])
        st.write(gpt[st.session_state["page"]])
