from .source import yahoo



def get_data_from_yahoo(symbol:str):
    pass

def stats_workflow(data):
    pass

def stats_index_workflow(stocks_data:dict):
    pass

def generate_report_page(data, stats):
    pass

def generate_ensemble_page(stocks_data:dict, stocks_stats:dict):
    pass

def build_report(index_page, stocks_pages):
    pass



def generate_report(symbols:[str], period:str, resolution:str):
    stocks_data = {}
    stocks_stats = {}
    stocks_pages = {}
    for symbol in symbols:
        stocks_data[symbol] = yahoo.get(symbol, period, resolution)
        stocks_stats[symbol] = stats_workflow(stocks_data[symbol])
        stocks_pages[symbol] = generate_report_page(stocks_data[symbol], stocks_stats[symbol])
    
    stocks_index_stats = stats_index_workflow(stocks_data)
    stocks_index_page = generate_ensemble_page(stocks_data, stocks_stats)

    build_report(stocks_index_page, stocks_pages)
    return



if __name__ == '__main__':
    #config stuff
    generate_report(symbols, period, resolution)
