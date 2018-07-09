import clingo

# domain specific

window_size = 3

base = """
input(a(1..2)).
all(T) :- time(T), holds(X,T) : input(X).
#show holds/2. #show all/1.
"""

stream = [
    [("a(1)", True), ("a(2)", False)],
    [("a(1)", True), ("a(2)",  True)],
    [("a(1)",False), ("a(2)", False)],
    [("a(1)", True), ("a(2)",  True)]
]

# domain independent

window_program = """
time(1-window_size..0).
#external holds(X,T) : input(X), time(T).
"""

def on_model(m):
    show = " ".join([str(i) for i in m.symbols(shown=True)])
    print("Answer:\n{}".format(show))

def set_externals(ctl, window):
    for idx, item in enumerate(window):
        for atom, value in item:
            clingo_atom = clingo.parse_term("holds("+atom+",-"+str(idx)+")")
            ctl.assign_external(clingo_atom, value)

def main():

    # preliminaries
    ctl = clingo.Control(["-c window_size={}".format(window_size)])
    ctl.add("base",[],base + window_program)
    ctl.ground([("base",[])])

    # solve until end of the stream
    window = [[]]*window_size
    for item in stream:
        window = [item] + window[:-1]
        set_externals(ctl, window)
        ctl.solve(on_model=on_model)

if __name__ == '__main__':
    main()
