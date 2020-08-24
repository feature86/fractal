from numpy import complex, array
from PIL import Image
import colorsys

WIDTH = 1024


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255, 1.0, 0.5))
    return tuple(color.astype(int))


def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return (0, 0, 0)


img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

printProgressBar(0, WIDTH, prefix='Progress:',
                 suffix='Complete', length=50)
for x in range(img.size[0]):
    printProgressBar(x, WIDTH,
                     prefix='Progress:', suffix='Complete', length=50)
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot(
            (x - (0.75*WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4))

img.show()
