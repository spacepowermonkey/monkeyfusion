import os



def apply(report):
    for symbol in report.symbols.values():
        sym_dir = f'{report.root}/symbols/{symbol.name}'

        os.makedirs(sym_dir, exist_ok=True)


        page = ''

        # Add header
        page += '---\n'
        page += f'title: {symbol.name} Stock Report\n'
        page += 'layout: page\n'
        page += '---\n'
        page += '\n\n\n'
        
        # Add performance
        page += '## Performance\n\n'

        page += '### Returns\n\n'
        page += 'Period | Return on Investment | Heatmap\n'
        page += '--- | --- | ---\n'
        for snapshot in symbol.snapshots.values():
            page += f'{snapshot.period} | ![](images/{symbol.name}-{snapshot.period}-price.png) | ![](images/{symbol.name}-{snapshot.period}-nprice.png)\n'
        page += '\n'
        page += 'Returns across various time periods, with the left chart showing return on $1 and the right chart a heatmap of those returns.'
        page += '\n\n\n'

        # Add momentum
        page += '### Momentum\n\n'
        page += 'Period | Rate of Return | Heatmap\n'
        page += '--- | --- | ---\n'
        for snapshot in symbol.snapshots.values():
            page += f'{snapshot.period} | ![](images/{symbol.name}-{snapshot.period}-diff.png) | ![](images/{symbol.name}-{snapshot.period}-ndiff.png)\n'
        page += '\n'
        page += 'Momentum across various time periods, with the left chart showing raw differences in price and the right chart a heatmap.'
        page += '\n\n\n'

        # Indexes
        page += '## Indexes\n\n'
        for index in symbol.indexes.values():
            page += f'### {index.name}\n\n'
            page += 'Period | Relative Returns | Relative Momentum\n'
            page += '--- | --- | ---\n'
            for snapshot in symbol.snapshots.values():
                page += f'{snapshot.period} | ![](images/rel-{index.name}-{snapshot.period}-nprice.png) | ![](images/rel-{index.name}-{snapshot.period}-ndiff.png)\n'
            page += '\n'
            page += f'Heatmaps of returns and momentum relative to the index average.'
            page += '\n\n\n'


        with open(f'{sym_dir}/index.md', 'w') as page_output:
            page_output.write(page)

    return
