import numpy


from ...types.symbol import StockSnapshot
from . import url as Yurl



def get(symbol, scale):
    data = Yurl.query_symbol(symbol, scale.period, scale.resolution)

    chart = data['chart']
    error = chart['error']

    results = chart['result']
    assert(len(results) == 1)
    result = results[0]
    indicators = result['indicators']
    quote_data = indicators['quote'][0]

    data = StockSnapshot(
        name=symbol,
        period = scale.period,
        resolution = scale.resolution,
        highs = numpy.asarray(quote_data['high']),
        lows = numpy.asarray(quote_data['low']),
        opens = numpy.asarray(quote_data['open']),
        closes = numpy.asarray(quote_data['close']),
        vols = numpy.asarray(quote_data['volume']),
        metrics = None,
        indexes = {}
    )

    return data
