# https://whitemech.github.io/pythomata/quickstart/

from pythomata import SimpleDFA


states = {"q0", "q1", "q2", "q3"}
alphabet = {"0", "1"}
initial_state = "q0"
accepting_states = {"q0"}


transition_function = {
    "q0": {
        "0": "q2",
        "1": "q1",
    },
    "q1": {
        "0": "q3",
        "1": "q0",
    },
    "q2": {
        "0": "q0",
        "1": "q3",
    },
    "q3": {
        "0": "q1",
        "1": "q2",
    }
}

automaton = SimpleDFA(
    states=states,
    alphabet=alphabet,
    initial_state=initial_state,
    accepting_states=accepting_states,
    transition_function=transition_function,
)

print(automaton.alphabet.size)  # 2

list(automaton.alphabet)  # ['0', '1']

automaton.accepts("")         # True
automaton.accepts("0")        # False - only one '0'
automaton.accepts("1")        # False - only one '1'
automaton.accepts("00")       # True
automaton.accepts("11")       # True
automaton.accepts("01" * 42)  # True

digraph = automaton.to_graphviz()
# Now `digraph` is a `graphviz.dot.Digraph` object.
digraph.render("my-even-01-automaton")


# # Create object from pythomata SimpleDFA class
# dfa = SimpleDFA(states, alphabet, initial_state,
#                 accepting_states, transition_function)

# # Word to test
# word = "bbbac"

# # Print if it accepts
# print(dfa.accepts(word))

# # Other Operation [minimize | Trim]
# dfa_minimized = dfa.minimize()
# dfa_trimmed = dfa.trim()


# # translate into graph
# graph = dfa.minimize().trim().to_graphviz()

# graph.render(r"E:\Programming\Python\~PROJECTS\100-Days-Of-Code-Python")
