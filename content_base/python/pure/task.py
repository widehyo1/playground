class Task:
    def __init__(self, executor, outfile, taskname="unnamed", nxt=None):
        self.executor = executor
        self.outfile = outfile
        self.taskname = taskname
        self.nxt = nxt

    def __repr__(self):
        if self.nxt:
            return f'{self.taskname} -> {self.nxt}'
        else:
            return f'{self.taskname}*'

class Flow:
    def __init__(self, rawdata, task=None):
        self.rawdata = rawdata
        self.task = task

    def __iter__(self):
        return self

    def __next__(self):
        if self.task:
            print(f'=== {self.task.taskname} ===')
            processed_data = self.task.executor(self.rawdata)
            processed_data.to_csv(self.task.outfile, index=None)
            print(f'writing {str(self.task.outfile)} done!')
            self.task = self.task.nxt
        else:
            raise StopIteration

    def execute(self):
        for _ in self:
            # execute task
            ...
