class StreamedProgramBasic:

    def __init__(self):

        # PUBLIC
        self.base = """
            wterm(a(1..2)).
            all(WT) :- WT=1-wsize..0, window(A,WT) : wterm(A).
            #show window/2.
            #show all/1.
        """
        self.wsize=2

        # PRIVATE
        self.data = [
            [("a(1)", True), ("a(2)", False)],
            [("a(1)", True), ("a(2)",  True)],
            [("a(1)",False), ("a(2)", False)],
            [("a(1)", True), ("a(2)",  True)]
        ]

    def next(self):
        out = None
        if len(self.data):
            out = self.data[0]
            self.data = self.data[1:]
        return out
