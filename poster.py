import Image, ImageDraw, sys, os

global application_name, version_number, cmd_name
global output_filename, top_tile, left_tile, height, width, zoom, style

application_name = 'osmposter'
cmd_name = 'poster.py'
version_number = "0.0.1"

server_url = "http://a.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707"	
tilesize = 256

def execute_cmd(action, cmd):
	sys.stdout.write(action + "...")
	sys.stdout.flush()
	
	value = os.system(cmd)
	if value != 0: raise Exception(action + " failed.") 
	print " FINISHED"

def clean():
	print "Deleting temporary files..."
	if os.path.isdir("tiles"):
		execute_cmd("Deleting tiles folder", "rm -R tiles")

def download_tiles(top_tile, left_tile, height, width, zoom, style):
	prefix_url = str(style) + "/" + str(tilesize) + "/" + str(zoom)
	clean()
	execute_cmd("Creating tiles folder", "mkdir tiles")

	print "Downloading tiles..."
	for x in range(0, int(height)/tilesize + 1):
		for y in range(0, int(width)/tilesize + 1):
			url = server_url + "/" + prefix_url + "/" + str(int(top_tile) + y) + "/" + str(int(left_tile) + x) + ".png"
			execute_cmd("Downloading " + url, "wget -O tiles/"+ str(x) + "_" + str(y) + ".png " + url)

def generate_poster(height, width, output_filename):
	img = Image.new("RGBA", (int(width), int(height)))
	
	print "Placing tiles..."
	for x in range(0, int(height)/tilesize + 1):
		for y in range(0, int(width)/tilesize + 1):
			tile = Image.open("tiles/" + str(x) + "_" + str(y) + ".png")
			img.paste(tile, (y * tilesize, x * tilesize))
	img.save(output_filename)
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
	clean()
elif len(sys.argv) == 2:
	option = sys.argv[1]
	if option == "-v": version()
	elif option == "-h": help()
else:
	print "FAILED: You need to specifiy all attributes. Try -h to get help."
