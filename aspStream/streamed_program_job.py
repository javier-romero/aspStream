JOB=open("job.lp").read()
STREAM=open("stream.lp").read()
STREAM_EXTENDED=open("stream_extended.lp").read()


class StreamedProgramJob:

    def __init__(self, extended=False):

        # PUBLIC
        self.base = JOB + STREAM
        if extended:
            self.base += STREAM_EXTENDED
        self.wsize = 3

        # PRIVATE
        # these should be gathered from the logic program
        self.horizon = 4  # job.lp
        self.jobs = 4     # stream.lp
        self.requests = 2 # stream.lp
        self.machines = 2 # stream.lp
        #
        self.externals = []
        for p in range(1, self.requests+1):
            for m in range(1, self.machines+1):
                for d in range(1, self.horizon+1):
                    self.externals.append("request({},{},{})".format(p,m,d))
        self.data = [
            [ "request(1,1,2)", "request(2,2,2)"],
            [ "request(1,2,2)"],
            [ "request(1,1,2)"],
        ]
        if not extended:
            return
        for m in range(1, self.machines+1):
            for t in range(1, self.horizon+1):
                self.externals.append("occupied({},{})".format(m,t))
        for r in range(1, self.requests+1):
            for t in range(1-self.wsize, 0):
                self.externals.append("done({},{})".format(r,t))
        self.data = [
            [ "request(1,1,2)", "request(2,2,2)"],
            [ "request(1,2,2)"],
            [ "request(1,1,4)"],
            #[ "request(1,1,4)", "done(1,-2)"],
        ]

    def next(self):
        out = None
        if len(self.data):
            out = [(i,  True) for i in self.data[0]] + [
                   (i, False) for i in self.externals if i not in self.data[0]
            ]
            self.data = self.data[1:]
        return out


if __name__ == "__main__":
    s = StreamedProgramJob()
    item = s.next()
    while item is not None:
        print(item)
        item = s.next()
