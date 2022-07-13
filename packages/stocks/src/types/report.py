from dataclasses import dataclass



from .symbol import Symbol
from .index import Index



@dataclass
class Scale:
    period : str
    resolution : str

class Report(object):
    def __init__(self, root, scales):
        self.root = root
        self.scales = list(map(lambda x: Scale(*x), scales))
        
        self.symbols = {}
        self.indexes = {}
        self.overview = None
        return
