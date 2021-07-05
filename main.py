# https://pypi.org/project/automata-lib/ AUTOMATLIB
# https://pypi.org/project/visual-automata/ VISUAL AUTOMATA

# Problem
# ( 1 + 0 )* (11 + 00 + 101 + 010) ( 1 + 0 + 11 + 00 + 101 )* ( 11 + 00 )
# ( 11+ 00 + 101 )* ( 1 + 0 ) ( 1 + 0 + 11 )*

from automata.fa.dfa import DFA

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

my_input_str = input("Enter String:")

if dfa.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
