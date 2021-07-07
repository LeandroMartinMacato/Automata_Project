import pandas as pd
from visual_automata.fa.dfa import VisualDFA
from automata.fa.dfa import DFA
import streamlit as st
from PIL import Image  # IMAGE MODULE

# TODO
# Reset input box when clicking reset button


# CONSTANTS
QUESTION = ["First Expression", "Second Expression"]
Q1 = "( b | aa | ab ) ( a | b )´ ( bb | aba | ab )´ ( aaa | bbb ) ( a | b ) ( a | b | ab )´"
Q2 = "( 1 | 0 )´ ( 11 | 00 | 101 | 010 ) ( 1 | 0 | 11 | 00 | 101 )´ ( 11 | 00 ) (11 | 00 | 101 )´ ( 1 | 0 ) ( 1 | 0 | 11 )´"


# Streamlit Start
st.title("The Automata Wizard 🧙🏻‍♂️")

st.markdown("""

#### The Automata Wizard will help you check String if it is valid on 2 sample Regular Expression while simulating the path the string took in the deterministic finite automaton (DFA)
""")

image = Image.open("logo_wiz.png")
st.sidebar.image(image)
input_box = st.sidebar.selectbox(
    "Expression List:", ("Select an Expression", QUESTION[0], QUESTION[1]))  # select box

# Page Control
# FIRST EXPRESSION
if input_box == QUESTION[0]:
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
    st.subheader(Q1)

    # Input Form
    with st.form("form"):
        st.header("String Checker 🧵")
        first_user_input = st.text_input(
            label="Enter String To Check If Valid: ⤵")
        submit_button = st.form_submit_button(label="Submit")

    # Try catch to catch error from switching expression
    try:
        if not first_user_input:
            st.write("Enter a string to simulate DFA")
        elif submit_button:
            if first_dfa.accepts_input(first_user_input):
                with st.form("1st Rectangle"):
                    st.header(
                        "deterministic-finite-automaton (DFA) Simulation:")
                    st.write(vis_dfa.show_diagram(first_user_input))
                    st.subheader("String is accepted! 🧙🏻‍♂️💯🎇")

                    # Table Simulation
                    df = pd.DataFrame(
                        vis_dfa.input_check(first_user_input))

                    listy = []
                    for x in df.iloc[:, 2]:
                        if x == "*q8":
                            # listy.append("Reject")
                            listy.append("Final_State")
                        else:
                            listy.append("Accepted")

                    df["Accepted/Final_State"] = listy
                    st.write(df)
                    st.header("Context-Free Grammar(CFG):")
                    st.markdown(''' 
                        Start symbol: S \n
                        S → PQRTUV  \n
                        P → b | aa | ab \n
                        Q → aQ | bQ | ε \n
                        R → bbR | abaR | abR | ε \n
                        T → aaa | bbb \n
                        U → a | b  \n		
                        V → aε | bε | abε | ε	OR	V -> UV | abV | ε   \n
                        ''')
                    # Reset
                    reset_button = st.form_submit_button(label="Reset")
                    if reset_button:
                        first_user_input = " "

            else:
                st.header(
                    "deterministic-finite-automaton (DFA) Simulation:")
                st.write(vis_dfa.show_diagram(first_user_input))
                st.subheader("String is not accepted! 🧙🏻‍♂️💢")

    except:
        st.write("Wrong Input!")


# SECOND EXPRESSION
elif input_box == QUESTION[1]:
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
    st.subheader(Q2)

    # User input Box
    with st.form("form"):
        st.header("String Checker 🧵")
        second_user_input = st.text_input(
            label="Enter String To Check If Valid: ⤵")
        submit_button = st.form_submit_button(label="Submit")

    # Check if string is valid
    try:
        if not second_user_input:
            st.write("Enter a string to simulate DFA")
        elif submit_button:
            if dfa.accepts_input(second_user_input):  # If accepted
                with st.form("2nd Rectangle"):
                    st.header(
                        "deterministic-finite-automaton (DFA) Simulation:")
                    st.write(vis_dfa.show_diagram(second_user_input))
                    st.subheader("String is accepted! 🧙🏻‍♂️💯🎇")
                    # Table SECTION
                    df = pd.DataFrame(
                        vis_dfa.input_check(second_user_input))
                    listy = []
                    for x in df.iloc[:, 2]:
                        if x == "*q8":
                            listy.append("Final_State")
                        else:
                            listy.append("Accepted")
                    df["Accepted/Final_State"] = listy
                    st.write(df)
                    st.header("Context-Free Grammar(CFG):")
                    st.markdown('''
                        Start symbol: S \n
                        S → PQRTUVW \n
                        P → 1P | 0P | ε \n
                        Q → 11 | 00 | 101 | 010 \n
                        R → 1R | 0R | 11R | 00R | 101R | ε \n
                        T → 11 | 00 \n
                        U → 11U | 00U | 101U | ε \n
                        V → 1 | 0   \n
                        W → 1W | 0W | 11W | ε \n
                        ''')
                    reset_button = st.form_submit_button(label="Reset")
                    if reset_button:
                        second_user_input = ""
            else:  # IF REJECTED
                st.header(
                    "deterministic-finite-automaton (DFA) Simulation:")
                st.write(vis_dfa.show_diagram(second_user_input))
                st.subheader("String is not accepted! 🧙🏻‍♂️💢")
    except:
        st.write("Wrong Input!")
else:
    st.header("⬅ Select an expression to start 🧝🏻‍♂️")
