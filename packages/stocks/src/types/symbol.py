from dataclasses import dataclass
from typing import Any



@dataclass
class StockSnapshot:
    name: str
    period: str
    resolution: str
    
    highs: Any
    lows: Any
    opens: Any
    closes: Any
    vols: Any

    metrics: Any
    indexes: Any


class Symbol(object):
    def __init__(self, name, report):
        self.name = name

        self.report = None
        self.snapshots = {}
        self.indexes = {}

        self.page = None
        return
