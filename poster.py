import Image, ImageDraw, sys

im = Image.open("5392.png")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw 

# write to stdout
im.save(sys.stdout, "PNG")
