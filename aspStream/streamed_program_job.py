# defines
JOB=open("job.lp").read()
STREAM=open("stream.lp").read()
STREAM_EXTENDED=open("stream_extended.lp").read()

# class
class StreamedProgramJob:

    def __init__(self, instance, extended=False):

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

        # read instance
        with open(instance) as f:
            self.data = [line[:-1].split() for line in f]

        # define externals
        self.externals = []
        for p in range(1, self.requests+1):
            for m in range(1, self.machines+1):
                for d in range(1, self.horizon+1):
                    self.externals.append("request({},{},{})".format(p,m,d))

        # return if not extended
        if not extended:
            return

        # define more externals if extended
        for r in range(1, self.requests+1):
            for t in range(1-self.wsize, 0):
                self.externals.append("done({},{})".format(r,t))
        for m in range(1, self.machines+1):
            for t in range(1, self.horizon+1):
                self.externals.append("occupied({},{})".format(m,t))

    def next(self):
        out = None
        if len(self.data):
            out = [(i,  True) for i in self.data[0]] + [
                   (i, False) for i in self.externals if i not in self.data[0]
            ]
            self.data = self.data[1:]
        return out


# main
if __name__ == "__main__":
    for instance in [
        'examples/stream_instance1.lp',
        'examples/stream_instance2.lp',
        'examples/stream_instance3.lp',
    ]:
        print("\ninstance = {}".format(instance))
        s = StreamedProgramJob(instance, extended=True)
        item = s.next()
        while item is not None:
            print(item)
            item = s.next()
        

