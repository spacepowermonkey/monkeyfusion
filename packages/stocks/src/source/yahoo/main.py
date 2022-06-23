import numpy


from ..stock import Stock
from . import url as Yurl



def get(symbol, period, resolution):
    data = Yurl.query_symbol(symbol, period, resolution)

    chart = data['chart']
    error = data['error']

    results = chart['result']
    assert(len(results) == 1, "Error, unexpected chart results returned from Yahoo!")
    result = results[0]
    indicators = result['indicators']
    quote_data = indicators['quote'][0]

    quotes = Stock(
        symbol = symbol,
        period = period,
        resolution = resolution,
        highs = numpy.asarray(quote_data['high']),
        lows = numpy.asarray(quote_data['lows']),
        opens = numpy.asarray(quote_data['open']),
        closes = numpy.asarray(quote_data['close']),
        vols = numpy.asarray(quote_data['volume'])
    )
    return quotes
