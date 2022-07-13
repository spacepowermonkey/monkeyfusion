from dataclasses import dataclass
from typing import Any



@dataclass
class IndexSnapshot:
    name: str
    period: str
    resolution: str

    metrics: Any
    rel_metrics: Any
    symbols: Any
    rankings: Any


class Index(object):
    def __init__(self, report, definition):
        self.name = definition[0]
        self.report = report


        self.snapshots = {}
        for scale in report.scales:
            self.snapshots[scale.period] = IndexSnapshot(self.name, scale.period, scale.resolution, None, {}, {}, None)


        self.symbols = {}
        for symbol in definition[1]:
            stock = report.symbols[symbol]
            self.symbols[stock.name] = stock
            stock.indexes[self.name] = self

            for scale in report.scales:
                self.snapshots[scale.period].symbols[stock.name] = stock.snapshots[scale.period]
                stock.snapshots[scale.period].indexes[self.name] = self.snapshots[scale.period]

        self.page = None
        return
