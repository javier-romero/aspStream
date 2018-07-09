#script (python)
import clingo
import sys

window = """
time(0..2).
input(a(1..2)).
#external holds(X,T) : input(X), time(T).
#show holds/2.
"""

base = """
all(T) :- time(T), holds(X,T) : input(X).
#show all/1.
"""

def _on_model(m):
    print "Answer:\n{}".format(" ".join([str(i) for i in m.symbols(shown=True)]))

def set_externals(ctl, stream):
    for idx, item in enumerate(stream):
        for x, value in item:
            ctl.assign_external(clingo.parse_term("holds("+x+","+str(idx)+")"), value)

def main():

    ctl = clingo.Control()
    ctl.add("base",[],base + window)
    ctl.ground([("base",[])])

    # first iteration
    stream = [
        [("a(1)",True), ("a(2)", False)],
        [],
        []
    ]
    set_externals(ctl, stream)
    ctl.solve(on_model=_on_model)

    # next iteration
    new = [("a(1)",False), ("a(2)", True)]
    stream = [new] + stream[0:-1]
    set_externals(ctl, stream)
    ctl.solve(on_model=_on_model)

    # next iteration
    new = [("a(1)",True), ("a(2)", True)]
    stream = [new] + stream[0:-1]
    set_externals(ctl, stream)
    ctl.solve(on_model=_on_model)

    # next iteration
    new = [("a(1)",False), ("a(2)", False)]
    stream = [new] + stream[0:-1]
    set_externals(ctl, stream)
    ctl.solve(on_model=_on_model)

    # next ...

if __name__ == '__main__':
    main()
