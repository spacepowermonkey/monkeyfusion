import json
import urllib.request as requests



def _add_cors_to_url(url):
    url += '&corsDomain=finance.yahoo.com&.tsrc=finance'
    return url

def _add_cors_to_headers(headers):
    headers['authority'] = 'query1.finance.yahoo.com'
    headers['origin'] = 'https://finance.yahoo.com'
    headers['sec-fetch-site'] = 'same-site'
    headers['sec-fetch-mode'] = 'cors'
    headers['sec-fetch-dest'] = 'empty'
    return headers



class RequestParams(object):
    def __init__(self,
        interval='1d', qrange='5y',
        includePrePost=False, useYfid=True,
        region='US', language='en-US'
    ):
        self.interval = interval
        self.range = qrange
        self.includePrePost = includePrePost
        self.useYfid = useYfid
        self.region = region
        self.language = language
        return

    def to_string(self):
        param_string = '?'
        param_string += f'interval={self.interval}'
        param_string += f'&range={self.range}'

        param_string += '&includePrePost=' + ('true' if self.includePrePost else 'false')
        param_string += '&useYfid=' + ('true' if self.useYfid else 'false')

        param_string += f'&region={self.region}'
        param_string += f'&lang={self.language}'

        return param_string





def request_for_symbol(stock_symbol, period, resolution):
    params = RequestParams(interval=resolution, qrange=period)

    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{stock_symbol}'
    url += params.to_string()
    url = _add_cors_to_url(url)

    headers = {
        'dnt': '1',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://finance.yahoo.com/quote/gme?ltr=1' 
    }
    headers = _add_cors_to_headers(headers)

    request = requests.Request(url, headers=headers)
    return request

def query_symbol(stock_symbol, period, resolution):
    request = request_for_symbol(stock_symbol, period, resolution)
    response = requests.urlopen(request)
    data = json.loads( response.read().decode() )
    return data