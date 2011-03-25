import Image, ImageDraw, sys

global application_name, version_number, cmd_name
global top_tile, left_tile, height, width, zoom, style

application_name = 'osmposter'
cmd_name = 'poster.py'
version_number = "0.0.1"

def download_tiles():
	return

def generate_poster():
	return
	
	
def version():
	print "This is " + application_name + " " + version_number

def help():
	version()
	print ""
	print "Usage: " + cmd_name + " top_tile left_tile height width zoom style"
	print ""
	print "Available options:"
	print " -v" + " - " + "output version number"
	print " -h" + " - " + "this help"
	
#Main program
if len(sys.argv) == 7:
	global top_tile, left_tile, height, width, zoom, style
	top_tile = sys.argv[1]
	left_tile = sys.argv[2]
	height = sys.argv[3]
	width = sys.argv[4]
	zoom = sys.argv[5]
	style = sys.argv[6]
	
	download_tiles()
	generate_poster()
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
