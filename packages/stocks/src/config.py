import json



class Dataset(object):
    def __init__(self, kwargs):
        self.source = kwargs["source"]
        self.symbol = kwargs["symbol"]

        self.period = kwargs["period"]
        self.resolution = kwargs["resolution"]
        return

class Report(object):
    def __init__(self, kwargs):
        self.datasets = [Dataset(x) for x in kwargs["datasets"]]
        return


class Config(object):
    def __init__(self, directory, config):
        with open(f'{directory}/{config}') as config_file:
            self.raw = json.load(config_file)

        self.parse()
        return

    def parse(self):
        self.datasets = [Dataset(x) for x in self.raw["datasets"]]
        self.reports = [Report(x) for x in self.raw["reports"]]
        return
