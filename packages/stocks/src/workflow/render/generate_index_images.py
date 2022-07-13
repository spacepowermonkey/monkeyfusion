import colorcet
import math
import numpy
import os



from .tools.images.main import render



def price_norm_for_color(array):
    results = numpy.zeros(shape=array.shape)
    for i in range(array.shape[0]):
        # Palette is red-high, green-low.
        results[i] = 1 - ( max(0, array[i]/2) if array[i] <= 1.0 else min(1, 0.5 + (array[i]-1)/2) )
    return results

def diff_norm_for_color(array):
    results = numpy.zeros(shape=array.shape)
    for i in range(array.shape[0]):
        # Palette is red-high, green-low.
        results[i] = 1 - max(0, min(1, array[i]*4 + 1/2))
    return results

def invert_norm(array):
    results = numpy.zeros(shape=array.shape)
    for i in range(array.shape[0]):
        results[i] = 1 - array[i]
    return results



def apply(report):
    for index in report.indexes.values():
        sym_dir = f'{report.root}/indexes/{index.name}'
        img_dir = f'{sym_dir}/images'
    
        os.makedirs(img_dir, exist_ok=True)

        for snapshot in index.snapshots.values():
            
            # Generate images:
            price = numpy.apply_along_axis(price_norm_for_color, 0, numpy.vstack([snapshot.metrics.price, snapshot.metrics.ema_ribbon]))
            nprice = numpy.apply_along_axis(invert_norm, 0, numpy.vstack([snapshot.metrics.nprice, snapshot.metrics.nema_ribbon]))
            diff = numpy.apply_along_axis(diff_norm_for_color, 0, numpy.vstack([snapshot.metrics.diff, snapshot.metrics.diff_ribbon]))
            ndiff = numpy.apply_along_axis(invert_norm, 0, numpy.vstack([snapshot.metrics.ndiff, snapshot.metrics.ndiff_ribbon]))

            render(img_dir, f'{snapshot.name}-{snapshot.period}-price', price, palette=colorcet.palette.CET_D3)
            render(img_dir, f'{snapshot.name}-{snapshot.period}-nprice', nprice, palette=colorcet.palette.CET_L17)
            render(img_dir, f'{snapshot.name}-{snapshot.period}-diff', diff, palette=colorcet.palette.CET_D3)
            render(img_dir, f'{snapshot.name}-{snapshot.period}-ndiff', ndiff, palette=colorcet.palette.CET_L17)

    return