from .render import(
    generate_index_images,
    generate_index_pages,
    generate_overview,
    generate_symbol_images,
    generate_symbol_pages
)
from .stats import (
    compute_index_metrics,
    compute_index_rankings,
    compute_symbol_metrics,
    compute_symbol_rel_metrics
)


def apply(report):
    compute_symbol_metrics.apply(report)
    compute_index_metrics.apply(report)
    compute_symbol_rel_metrics.apply(report)
    compute_index_rankings.apply(report)

    generate_symbol_images.apply(report)
    generate_symbol_pages.apply(report)
    generate_index_images.apply(report)
    generate_index_pages.apply(report)

    generate_overview.apply(report)
    return
