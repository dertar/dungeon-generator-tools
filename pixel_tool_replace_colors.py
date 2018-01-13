from PIL import Image
import sys


def getReplaceColor(pixels):
	width = pixels.size[0]
	height = pixels.size[1]

	if width != 2:
		print('Error parsing color palette')
		exit(-1)

	color = []

	for y in range(0,height):
		color.append( (pixels.getpixel((0,y)),pixels.getpixel((1,y)) ) )

	return color

def replaceColors(pixels,palette):
	width = pixels.size[0]
	height = pixels.size[1]

	changed = 0

	for x in range(0,width):
		for y in range(0,height):
			color = isColor(pixels.getpixel((x,y)),palette)
			if color != None:
				pixels.putpixel((x,y),color[1])
				changed += 1

	return changed

def isColor(rgb,palette):
	for color in palette:
		if color[0][0] == rgb[0] and color[0][1] == rgb[1] and color[0][2] == rgb[2]:
			return color
	return None

def main(inFile,outFile,colorFile):
	print('input image file name  : ' + inFile)
	print('output image file name : ' + outFile)
	print('color file             : ' + colorFile)

	image = Image.open(inFile)

	colors = getReplaceColor( Image.open(colorFile) )

	print('replacing colors: ')

	for color in colors:
		print('\t' + str(color[0]) + ' to ' + str(color[1]) )

	changedRgbs = replaceColors(image,colors)

	print('Changed colors: ' + str(changedRgbs))

	if changedRgbs != 0:
		image.save(outFile)

	print('Done!')


if __name__ == '__main__':
	if len(sys.argv) == 4:
		main(sys.argv[1],sys.argv[2],sys.argv[3])
	else:
		print('Incorrect argv parameters!!!')
		print('Usage: script.py [input image file name] [output image file name] [pattern file]')