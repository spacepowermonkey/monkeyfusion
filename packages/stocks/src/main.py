import time



from .source import yahoo

from .types.index import Index
from .types.report import Report
from .types.symbol import Symbol

from .workflow import main as workflow



def main(root, symbols, indexes, scales):
    report = Report(root, scales)

    for symbol in symbols:
        report.symbols[symbol] = Symbol(symbol, report)
        for scale in report.scales:
            time.sleep(1)
            report.symbols[symbol].snapshots[scale.period] = yahoo.get(symbol, scale)
    
    for index in indexes:
        report.indexes[index[0]] = Index(report, index)

    workflow.apply(report)
    return



if __name__ == '__main__':
    symbols = [
        'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX',
        'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM',
        'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH',
        'CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW'
    ]
    scales = [
        ('5d', '15m'),
        ('1mo', '30m'),
        ('1y', '1d')
        #('5y', '1d')
    ]


    root = '/data'

    main(root, symbols, [('DOW30', symbols)], scales)
