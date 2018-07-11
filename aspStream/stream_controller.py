import clingo
import streamed_program_basic
import streamed_program_job

externals = """
#external window(A,WT) : WT=1-wsize..0, wterm(A).
"""

def on_model(m):
    show = " ".join([str(i) for i in m.symbols(shown=True)])
    print("Answer:\n{}".format(show))

def set_externals(ctl, window):
    for idx, item in enumerate(window):
        for term, value in item:
            atom = clingo.parse_term("window("+term+",-"+str(idx)+")")
            ctl.assign_external(atom, value)


class AbstractStreamedProgram:

    def __init__(self):
        self.base = ""
        self.wsize = 1

    def next(self):
        return None


def main(sp):

    # ground base
    ctl = clingo.Control(["-c wsize={}".format(sp.wsize)])
    ctl.add("base",[],sp.base + externals)
    ctl.ground([("base",[])])

    # solve until end of the stream
    window = [[]]*sp.wsize
    item = sp.next()
    while item is not None:
        window = [item] + window[:-1]
        set_externals(ctl, window)
        print("\nSolving...")
        ctl.solve(on_model=on_model)
        item = sp.next()

if __name__ == '__main__':
    stars = "*"*60
    print("{}\nBasic\n{}".format(stars, stars))
    main(streamed_program_basic.StreamedProgramBasic())
    print("")
    instances = []
    instances.append(("examples/stream_instance1.lp", False))
    instances.append(("examples/stream_instance1.lp",  True))
    instances.append(("examples/stream_instance2.lp", False))
    instances.append(("examples/stream_instance2.lp",  True))
    instances.append(("examples/stream_instance3.lp",  True))
    for instance, extended in instances:
        print("\n{}\nInstance = {}\tExtended = {}\n{}\n{}{}".format(
            stars, instance, extended, stars, open(instance).read(), stars)
        )
        main(streamed_program_job.StreamedProgramJob(instance, extended))
