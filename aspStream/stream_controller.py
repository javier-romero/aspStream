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
        print("Solving...")
        #print(window)
        ctl.solve(on_model=on_model)
        item = sp.next()

if __name__ == '__main__':
    # choose one
    #main(streamed_program_basic.StreamedProgramBasic())
    #main(streamed_program_job.StreamedProgramJob())
    main(streamed_program_job.StreamedProgramJob(True))
