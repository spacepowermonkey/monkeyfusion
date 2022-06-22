import json



class YahooQueryResult(object):
    def __init__(self, data):
        self._raw = data
        self.meta = data['meta']
        self.meta['source'] = 'yahoo'
        self.timestamp = data['timestamp']
        self.indicators = data['indicators']
        return

    def to_quotes(self):
        quotes = []

        quote_symbol = self.meta['symbol']
        quote_currency = self.meta['currency']

        quote_data = self.indicators['quote'][0]

        values_high = quote_data['high']
        values_low = quote_data['low']
        values_open = quote_data['open']
        values_close = quote_data['close']
        values_volume = quote_data['volume']

        for i in range(len(self.timestamp)):
            quotes.append((
                self.timestamp[i],
                values_open[i], values_close[i], values_high[i], values_low[i],
                values_volume[i]                
            ))

        return quotes



class YahooChart(object):
    def __init__(self, data):
        self._raw = data['chart']

        self.error = self._raw['error']
        self.result = YahooQueryResult( self._read_result() )
        return

    def _read_result(self):
        results = self._raw['result']
        assert(len(results) == 1)
        return results[0]
