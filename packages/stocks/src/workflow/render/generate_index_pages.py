import os



def apply(report):
    for index in report.indexes.values():
        sym_dir = f'{report.root}/indexes/{index.name}'

        os.makedirs(sym_dir, exist_ok=True)


        page = ''

        # Add header
        page += '---\n'
        page += f'title: {index.name} Stock Report\n'
        page += 'layout: page\n'
        page += '---\n'
        page += '\n\n\n'
        
        # Add performance
        page += '## Performance\n\n'

        page += '### Returns\n\n'
        page += 'Period | Return on Investment | Heatmap\n'
        page += '--- | --- | ---\n'
        for snapshot in index.snapshots.values():
            page += f'{snapshot.period} | ![](images/{index.name}-{snapshot.period}-price.png) | ![](images/{index.name}-{snapshot.period}-nprice.png)\n'
        page += '\n'
        page += 'Returns across various time periods, with the left chart showing return on $1 and the right chart a heatmap of those returns.'
        page += '\n\n\n'

        # Add momentum
        page += '### Momentum\n\n'
        page += 'Period | Rate of Return | Heatmap\n'
        page += '--- | --- | ---\n'
        for snapshot in index.snapshots.values():
            page += f'{snapshot.period} | ![](images/{index.name}-{snapshot.period}-diff.png) | ![](images/{index.name}-{snapshot.period}-ndiff.png)\n'
        page += '\n'
        page += 'Momentum across various time periods, with the left chart showing raw differences in price and the right chart a heatmap.'
        page += '\n\n\n'

        page += '## Rankings\n\n'
        for snapshot in index.snapshots.values():
            page += f'### {snapshot.period} Rankings\n\n'
            page += 'Grade | Percentile | Symbols\n'
            page += '--- | --- | ---\n'
            page += 'A | 90% | '
            for i in range(0, 3):
                page+= f'[{snapshot.rankings[i].name}](/reports/stocks/symbols/{snapshot.rankings[i].name}) '
            page += '\n'
            page += 'B | 70% | '
            for i in range(3, 9):
                page+= f'[{snapshot.rankings[i].name}](/reports/stocks/symbols/{snapshot.rankings[i].name}) '
            page += '\n'
            page += 'C | 30% | '
            for i in range(9, 21):
                page+= f'[{snapshot.rankings[i].name}](/reports/stocks/symbols/{snapshot.rankings[i].name}) '
            page += '\n'
            page += 'D | 10% | '
            for i in range(21, 27):
                page+= f'[{snapshot.rankings[i].name}](/reports/stocks/symbols/{snapshot.rankings[i].name}) '
            page += '\n'
            page += 'E | | '
            for i in range(27, 30):
                page+= f'[{snapshot.rankings[i].name}](/reports/stocks/symbols/{snapshot.rankings[i].name}) '
            page += '\n\n\n'


        with open(f'{sym_dir}/index.md', 'w') as page_output:
            page_output.write(page)

    return
