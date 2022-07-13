def apply(report):
    for index in report.indexes.values():
        for snapshot in index.snapshots.values():
            snapshot.rankings = sorted(
                list(snapshot.symbols.values()),
                key=lambda x: x.metrics.price[-1],
                reverse=True
            )
    return