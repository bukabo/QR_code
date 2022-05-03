from PIL import Image, ImageDraw

im = Image.open('manchester_united_PNG26.png')


def interpolate(f_co, t_co, interval):
    det_co = [(t - f) / interval for f, t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]


gradient = Image.new('RGBA', im.size, color=0)
draw = ImageDraw.Draw(gradient)

f_co = (133, 255, 154)
t_co = (154, 5, 30)
for i, color in enumerate(interpolate(f_co, t_co, im.width * 2)):
    draw.line([(i, 0), (0, i)], tuple(color), width=1)

im_composite = Image.alpha_composite(gradient, im)
# im_composite.show()

with open('лого3.png', 'wb') as f:
    im_composite.save(f)
