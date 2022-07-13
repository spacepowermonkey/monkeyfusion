import colorcet



def cet_rg(value):
    return colorize(colorcet.palette.CET_D3, value)


def cet_worb(value):
    return colorize(colorcet.palette.CET_L17, value)


def colorize(palette, value):
    color_count = len(palette) -1
    index = min(color_count, max(0, int( color_count * value ) ))

    return palette[index]
