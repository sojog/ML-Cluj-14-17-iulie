# pip install streamlit
# streamlit run filename

import streamlit as st
import pickle
import numpy as np

st.title("Ai fi supravietuit pe Titanic...?")

mesaj = st.chat_input("Insereaza o valoare")


QUESTIONS = [
    "In primul rand, cati ani ai??",
    "De unde ai plecat? 1-Southhamption/ 2- Queenstown / 3 - restul"

]




print(mesaj)

if not st.session_state.get("messages"):
    st.session_state["messages"]  = []

if not st.session_state.get("Q_index"):
    st.session_state["Q_index"] = 0

with st.chat_message("ai") as msg:
    st.write(QUESTIONS[st.session_state.get("Q_index", 0)])


if mesaj:
    print("Am primit un nou mesaj")
    st.session_state["messages"].append((mesaj, "user"))
    print('st.session_state["messages"]', st.session_state["messages"])

    if st.session_state.get("Q_index", 0) + 1 < len(QUESTIONS):
        st.session_state["Q_index"] += 1
        intrebarea = QUESTIONS[st.session_state.get("Q_index", 0)]
        st.session_state["messages"].append((intrebarea, "ai"))
    else:
        # FOLOSIRE DE MODEL
        with open("model.pkl", "rb") as freader:
            model = pickle.load(freader)
            mesaje = st.session_state["messages"]
            mesaje_user = [m[0] for m in mesaje if m[1] == "user"]
            varsta, locatia = mesaje_user
            print("Utilizatorul are varsta:", varsta, "Si a plecat din locatia:", locatia)
            try:
                varsta = varsta(int)
            except:
                varsta = 20

            try:
                locatia = locatia(int)
            except:
                locatia = 1

            rezultat = model.predict([[3.0,	7.25,	7.0,	1.0,	locatia]])
            supravietuieste = rezultat.flatten()[0]
            supravietuieste = bool(supravietuieste)

        mesaj_supravietuire = f" Cel mai probabil { 'nu' if not supravietuieste else ''} supravietuiai"
        st.session_state["messages"].append((mesaj_supravietuire, "ai"))    



for mesaj, role in st.session_state["messages"]:
    with st.chat_message(role) as msg:
        st.write(mesaj)
    