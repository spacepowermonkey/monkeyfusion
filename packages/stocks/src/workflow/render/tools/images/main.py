import cairosvg



from . import data_grid



height = 1000
width = 1000

samples = 200



def render(path, filename, data, palette):
    # Render the values into SVG.
    spec_render = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n'

    spec_render += data_grid.render2D(data, samples=samples, height=height, width=width, palette=palette)
    
    spec_render += "</svg>\n"

    with open(f"{path}/{filename}.svg","w") as handle:
        handle.write(spec_render)
    cairosvg.svg2png(
        file_obj=open(f"{path}/{filename}.svg", "rb"), write_to=f"{path}/{filename}.png"
    )

    return
