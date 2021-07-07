# https://pypi.org/project/automata-lib/ AUTOMATLIB
# https://pypi.org/project/visual-automata/ VISUAL AUTOMATA

# Problem
# ( 1 + 0 )* (11 + 00 + 101 + 010) ( 1 + 0 + 11 + 00 + 101 )* ( 11 + 00 )
# ( 11+ 00 + 101 )* ( 1 + 0 ) ( 1 + 0 + 11 )*

# AUTOMATA MODULES
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import streamlit as sl

# CONSTANTS
q1 = [
    "Question 1: ( b + aa + ab ) ( a + b )* ( bb + aba + ab )* ( aaa + bbb ) ( a + b ) ( a + b + ab )* "]
q2 = ["Question 2: ( 1 + 0 )* (11 + 00 + 101 + 010) ( 1 + 0 + 11 + 00 + 101 )* ( 11 + 00 ) ( 11+ 00 + 101 )* ( 1 + 0 ) ( 1 + 0 + 11 )*"]

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


my_input_str = input("Enter String:")
if dfa.accepts_input(my_input_str):
    # dfa.show_diagram(my_input_str)
    print('accepted')
else:
    # dfa.show_diagram(my_input_str)
    print('rejected')


# vis_dfa = VisualDFA(dfa)
# vis_dfa.show_diagram("110111")
