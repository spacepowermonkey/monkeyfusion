import numpy

from dataclasses import dataclass
from typing import Any



from .tools import diff, ema, norm, roc



@dataclass
class StockMetrics:
    # These are ordered in the sequnce they're built.
    price           : Any = None
    price_max       : Any = None
    nprice          : Any = None
    diff            : Any = None
    ndiff           : Any = None

    ema_ribbon      : Any = None
    diff_ribbon     : Any = None

    nema_ribbon     : Any = None
    ndiff_ribbon    : Any = None


def skew_to_interval(val, offset):
    fn = norm.by_val(val)
    def _norm(array):
        return (fn(array) - offset) * 1/2 + 1/2
    return _norm


def apply(report):
    for symbol in report.symbols.values():
        for snapshot in symbol.snapshots.values():
            snapshot.metrics = StockMetrics()

            snapshot.metrics.price = norm.by_first(snapshot.closes)
            snapshot.metrics.price_max = numpy.amax(snapshot.metrics.price)

            norm_price = skew_to_interval(snapshot.metrics.price_max, 1)
            snapshot.metrics.nprice = norm_price(snapshot.metrics.price)

            snapshot.metrics.diff = roc.apply(snapshot.metrics.price)
            snapshot.metrics.diff_max = numpy.amax(snapshot.metrics.diff)

            norm_diff = skew_to_interval(snapshot.metrics.diff_max, 0)
            snapshot.metrics.ndiff = norm_diff(snapshot.metrics.diff)

            snapshot.metrics.ema_ribbon = ema.spectrum(snapshot.metrics.price, power=8)
            snapshot.metrics.diff_ribbon = roc.twoD(snapshot.metrics.ema_ribbon)

            snapshot.metrics.nema_ribbon = numpy.apply_along_axis(norm_price, 0, snapshot.metrics.ema_ribbon)
            snapshot.metrics.ndiff_ribbon = numpy.apply_along_axis(norm_diff, 0, snapshot.metrics.diff_ribbon)
        
    return
