from dataclasses import dataclass
from typing import Any



@dataclass
class Stock:
    symbol: str
    period: str
    resolution: str
    highs: Any
    lows: Any
    opens: Any
    closes: Any
    vols: Any
