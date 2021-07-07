# https://docs.streamlit.io/en/stable/

# https://www.youtube.com/watch?v=Klqn--Mu2pE
import pandas as pd
from visual_automata.fa.dfa import VisualDFA
from automata.fa.dfa import DFA
import streamlit as st
from PIL import Image  # IMAGE MODULE

# TODO
# WHILE NOTHING IS IN INPUT BOX DONT DISPLAY SHIT
# When switching expression there will be an error becoz naka submit parin yung input FIXED


# CONSTANTS
q1 = "( b + aa + ab ) ( a + b )* ( bb + aba + ab )* ( aaa + bbb ) ( a + b ) ( a + b + ab )* "
q2 = "(1+0)* (11+00+101+010) ( 1+0+11+00+101)* (11+00) (11+00+101)* (1+0) (1+0+11)*"


# Streamlit Start
st.title("The Automata Wizard 🧝🏻‍♂️")

st.markdown("""

#### Automata Wizard will help you check String if it is valid on 2 sample Regular Expression while simulating the path the string took in the DFA
""")

image = Image.open("logo_wiz.png")
st.sidebar.image(image)
input_box = st.sidebar.selectbox(
    "Select Expression:", (q1, q2))  # select box

# Page Control
if input_box == q1:
    first_dfa = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4',
                'q5', 'q6', 'q7', 'q8'},
        input_symbols={'a', 'b'},
        transitions={
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'q2', 'b': 'q2'},
            'q2': {'a': 'q3', 'b': 'q5'},
            'q3': {'a': 'q4', 'b': 'q5'},
            'q4': {'a': 'q7', 'b': 'q5'},
            'q5': {'a': 'q3', 'b': 'q6'},
            'q6': {'a': 'q3', 'b': 'q7'},
            'q7': {'a': 'q8', 'b': 'q8'},
            'q8': {'a': 'q8', 'b': 'q8'}
        },
        initial_state='q0',
        final_states={'q8'}
    )
    vis_dfa = VisualDFA(first_dfa)  # Create Visual DFA from DFA

    st.header("Regular Expression:")
    st.subheader(q1)
    # st.write(q1)
    with st.form("form"):
        first_user_input = st.text_input(
            label="Enter String To Check If Valid:")
        submit_button = st.form_submit_button(label="Submit")

    # Try catch to catch error from switching expression
    try:

        if first_dfa.accepts_input(first_user_input):
            st.write("ACCEPTED!")
            st.write(vis_dfa.show_diagram(first_user_input))
        else:
            st.write("REJECTED!")
            st.write(vis_dfa.show_diagram(first_user_input))
    except:
        st.write("ERROR")

elif input_box == q2:
    dfa = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4',
                'q5', 'q6', 'q7', 'q8'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'0': 'q4', '1': 'q3'},
            'q2': {'0': 'q3', '1': 'q4'},
            'q3': {'0': 'q4', '1': 'q4'},
            'q4': {'0': 'q5', '1': 'q6'},
            'q5': {'0': 'q7', '1': 'q6'},
            'q6': {'0': 'q5', '1': 'q7'},
            'q7': {'0': 'q8', '1': 'q8'},
            'q8': {'0': 'q8', '1': 'q8'}
        },
        initial_state='q0',
        final_states={'q8'}
    )
    vis_dfa = VisualDFA(dfa)

    # Start

    st.header("Regular Expression:")
    st.subheader(q2)

    # User input Box
    with st.form("form"):
        second_user_input = st.text_input(
            label="Enter String To Check If Valid:")
        submit_button = st.form_submit_button(label="Submit")

    # Check if string is valid
    try:
        if dfa.accepts_input(second_user_input):
            st.write("ACCEPTED!")
            st.write(vis_dfa.show_diagram(second_user_input))
        else:
            st.write("REJECTED!")
            st.write(vis_dfa.show_diagram(second_user_input))
    except:
        st.write("Clear Input First")

    # Visual DFA


else:
    st.write("ERROR")
