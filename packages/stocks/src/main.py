from .source import yahoo

from .workflow import (
    generate_page,
    generate_index_page,
    stats_workflow,
    stats_index_workflow
)



def build_report(index_page, stocks_pages):
    pass



def generate_report(symbols:[str], period:str, resolution:str):
    stocks_data = {}
    stocks_stats = {}
    stocks_pages = {}
    for symbol in symbols:
        stocks_data[symbol] = yahoo.get(symbol, period, resolution)
        stocks_stats[symbol] = stats_workflow.apply(stocks_data[symbol])
        stocks_pages[symbol] = generate_page.apply(stocks_data[symbol], stocks_stats[symbol])
    
    stocks_index_stats = stats_index_workflow.apply(stocks_data)
    stocks_index_page = generate_index_page.apply(stocks_data, stocks_stats)

    build_report(stocks_index_page, stocks_pages)
    return



if __name__ == '__main__':
    #config stuff
    generate_report(symbols, period, resolution)
