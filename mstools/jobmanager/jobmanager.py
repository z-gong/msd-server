class JobManager:
    def __init__(self, queue=None, nprocs=None):
        self.queue = queue
        self.nprocs = nprocs

    def generate_sh(self, workdir, commands: [str], name):
        pass

    def submit(self):
        pass

    def get_info_from_name(self, name):
        pass