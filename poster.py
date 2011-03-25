import Image, ImageDraw, sys

global application_name, version_number, cmd_name
global output_filename, top_tile, left_tile, height, width, zoom, style

application_name = 'osmposter'
cmd_name = 'poster.py'
version_number = "0.0.1"

server_url = "http://c.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707"	
tilesize = 256

def download_tiles(top_tile, left_tile, height, width, zoom, style):
	prefix_url = "/" + str(style) + "/" + str(tilesize) + "/" + str(zoom)
	
	for x in range(0, int(height)/tilesize):
		for y in range(0, int(width)/tilesize):
			print x,y

def generate_poster(height, width, output_filename):
	return
	
	
def version():
	print "This is " + application_name + " " + version_number

def help():
	version()
	print ""
	print "Usage: " + cmd_name + " output_filename top_tile left_tile height width zoom styleid"
	print ""
	print "Available options:"
	print " -v" + " - " + "output version number"
	print " -h" + " - " + "this help"
	
#Main program
if len(sys.argv) == 8:
	global output_filename, top_tile, left_tile, height, width, zoom, style
	output_filename = sys.argv[1]
	top_tile = sys.argv[2]
	left_tile = sys.argv[3]
	height = sys.argv[4]
	width = sys.argv[5]
	zoom = sys.argv[6]
	style = sys.argv[7]
	
	download_tiles(top_tile, left_tile, height, width, zoom, style)
	generate_poster(height, width, output_filename)
elif len(sys.argv) == 2:
	option = sys.argv[1]
	if option == "-v": version()
	elif option == "-h": help()
else:
	print "FAILED: You need to specifiy all attributes. Try -h to get help."



#im = Image.open("5392.png")

#draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
#del draw 

# write to stdout
#im.save(sys.stdout, "PNG")
