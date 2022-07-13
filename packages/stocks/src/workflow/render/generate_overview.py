import os



def apply(report):
    sym_dir = f'{report.root}'

    os.makedirs(sym_dir, exist_ok=True)


    page = ''
    
    # Add header
    page += '---\n'
    page += f'title: Stock Report\n'
    page += 'layout: page\n'
    page += '---\n'
    page += '\n\n\n'
    page += 'This page has links to the indexes and stocks tracked by our service.\n'
    page += '\n\n\n'

    page += '## Indexes\n\n'
    for index in sorted(list(report.indexes)):
        page += f'[{index}](/reports/stocks/indexes/{index}) '
    page += '\n\n'

    page += '## Symbols\n\n'
    for symbol in sorted(list(report.symbols)):
        page += f'[{symbol}](/reports/stocks/symbols/{symbol}) '
    
    page += '\n\n\n'
    page += 'This report generated with [MonkeyFusion](https://www.spacepowermonkey.com/software/monkeyfusion/).\n'


    with open(f'{sym_dir}/index.md', 'w') as page_output:
            page_output.write(page)
    
    return
