import math
import json
import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle


def toRGB(t):
    rgb = [x * 255 for x in t]
    r,g,b = map(int, rgb)
    return (r,g,b)


def plot_colortable(colors, *, ncols=4, sort_colors=True):
    jsonColorRGB = {}
    jsonColorHEX = {}
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7
        jsonColorRGB[name]=toRGB(mcolors.to_rgb(colors[name]))
        jsonColorHEX[name]=colors[name]
        
        ####CHANGE THE FILE NAMES IN THE 2 FILES BELOWS FOR XKCD
        ####"colorsXKCD_RGB.json" and "colorsXKCD_HEX.json"
        
        with open("colorsCSS4_RGB.json", "w") as outfile:
            json.dump(jsonColorRGB, outfile, indent=4)  
        with open("colorsCSS4_HEX.json", "w") as outfile:
            json.dump(jsonColorHEX, outfile, indent=4)  

        
        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig
    
# xkcd_fig = plot_colortable(mcolors.XKCD_COLORS)
# xkcd_fig.savefig("colorsXKCD_RGB.png")   
xkcd_fig = plot_colortable(mcolors.CSS4_COLORS)
xkcd_fig.savefig("ColorsCSS4.png")   
