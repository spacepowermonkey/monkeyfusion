from .colorize import colorize



def render(array, samples, height, width, offset, palette):
    w_step = width/samples
    step = array.shape[0] / samples

    sample_data = []
    for i in range(samples-1):
        sample_data.append(
            array[int(i * step)]
        )
    sample_data.append( array[-1] )

    svg = f'<g transform="translate(0 {offset})">'
    for i in range(0, len(sample_data)):
        color = colorize(palette, sample_data[i])

        rect = f'<rect fill="{color}" x="{i * w_step}" y="{0}"  width="{w_step}" height="{height}" />'
        svg += rect
    svg += '</g>'

    return svg



def render2D(array, samples, height, width, palette):
    row_height = height / array.shape[0]

    svg = ''
    for i in range(array.shape[0]):
        offset = i * row_height
        svg += render(array[i], samples, height, width, offset, palette)

    return svg
