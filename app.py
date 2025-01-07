import streamlit as st
import pandas as pd
import duckdb

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)

st.write("""
# SQL
Space Repetition System SQL practice
""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Join", "Group By", "Windows Functions"),
        index=None,
        placeholder="Select a theme..."
    )

tab1, tab2, tab3 = st.tabs(['cat', 'chien', 'oiseau'])

with tab1:
    input_t = st.text_area(label="put ton texte:")
    if input_t:
        result = duckdb.query(input_t).df()
        st.write(input_t)
        st.dataframe(result)

with tab2:
    input_te = st.text_area(label="pfewfwete:")
    st.write(input_te)

with tab3:
    input_tf = st.text_area(label="put tofewfwefwen texte:")
    st.write(input_tf)

