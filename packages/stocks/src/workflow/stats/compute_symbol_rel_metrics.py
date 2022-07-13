import numpy

from dataclasses import dataclass
from typing import Any



from .tools import diff, ema, norm, roc



@dataclass
class StockRelMetrics:
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
    for index in report.indexes.values():
        for snapshot in index.snapshots.values():
            for symbol in snapshot.symbols.values():
                snapshot.rel_metrics[symbol.name] = StockRelMetrics()

                snapshot.rel_metrics[symbol.name].price = symbol.metrics.price / snapshot.metrics.price


                snapshot.rel_metrics[symbol.name].price_max = numpy.amax(snapshot.rel_metrics[symbol.name].price)
                norm_price = skew_to_interval(snapshot.rel_metrics[symbol.name].price_max, 1)
                snapshot.rel_metrics[symbol.name].nprice = norm_price(snapshot.rel_metrics[symbol.name].price)

                snapshot.rel_metrics[symbol.name].ema_ribbon = ema.spectrum(snapshot.rel_metrics[symbol.name].price, power=8)
                snapshot.rel_metrics[symbol.name].nema_ribbon = numpy.apply_along_axis(norm_price, 0, snapshot.rel_metrics[symbol.name].ema_ribbon)


                snapshot.rel_metrics[symbol.name].diff = roc.apply(snapshot.rel_metrics[symbol.name].price)
                snapshot.rel_metrics[symbol.name].diff_max = numpy.amax(snapshot.rel_metrics[symbol.name].diff)
                norm_diff = skew_to_interval(snapshot.rel_metrics[symbol.name].diff_max, 0)
                snapshot.rel_metrics[symbol.name].ndiff = norm_diff(snapshot.rel_metrics[symbol.name].diff)

                snapshot.rel_metrics[symbol.name].diff_ribbon = roc.twoD(snapshot.rel_metrics[symbol.name].ema_ribbon)
                snapshot.rel_metrics[symbol.name].ndiff_ribbon = numpy.apply_along_axis(norm_diff, 0, snapshot.rel_metrics[symbol.name].diff_ribbon)
    
    return
