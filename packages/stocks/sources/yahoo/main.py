import json



from monkeytroope import constants as const
from monkeytroope import stockdb as db



from . import format as Yformat
from . import url as Yurl



def crawl(symbol, period, resolution):
    print(const.UX_BANNER)
    print(f"QUERYING YAHOO FOR {symbol}...")
    data = Yurl.query_symbol(symbol, period, resolution)
    chart = Yformat.YahooChart(data)
    meta = chart.result.meta
    meta["period"] = meta["range"]
    meta["resolution"] = meta["dataGranularity"]
    print("...RESPONSE:")
    print(f"...COUNT {len(chart.result.timestamp)}")
    print(json.dumps(meta, indent=2))

    print(const.UX_BANNER)
    print(f"BUILDING STOCK DB FOR {symbol}")
    quotes = chart.result.to_quotes()
    history = db.stock.Record(symbol, meta, quotes)
    history.save()
    
    print(const.UX_BANNER + '\n\n\n')
    return
