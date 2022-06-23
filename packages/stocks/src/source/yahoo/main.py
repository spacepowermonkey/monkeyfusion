import json



from . import format as Yformat
from . import url as Yurl



def get(symbol, period, resolution):
    data = Yurl.query_symbol(symbol, period, resolution)
    chart = Yformat.YahooChart(data)
    meta = chart.result.meta
    meta["period"] = meta["range"]
    meta["resolution"] = meta["dataGranularity"]

    quotes = chart.result.to_quotes()
    return quotes
