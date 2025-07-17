# pip install streamlit
# streamlit run filename

import streamlit as st

st.title("Insereaza ceva...")
mesaj = st.chat_input("Insereaza o valoare")




print(mesaj)

if not st.session_state.get("messages"):
    st.session_state["messages"]  = []

if mesaj:
    print("Am primit un nou mesaj")
    st.session_state["messages"].append(mesaj)
    print('st.session_state["messages"]', st.session_state["messages"])

for mesaj in st.session_state["messages"]:
    with st.chat_message("human") as msg:
        st.write(mesaj)
    
    with st.chat_message("ai") as msg:
        st.write("da da da da...ai dreptate")