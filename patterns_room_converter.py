from PIL import Image
import sys

colors = ( 
		((255,255,255),'EMPTY'),
		((0,0,0),'SOLID_BLOCK'),
		((128,128,128),'MOVE_BLOCK'),
		((128,62,128),'NON_MOVE_BLOCK'),
		((255,0,0),'TRAP'),
		((255,120,0),'MOD_TRAP'),
		((0,0,255),'DROP_PLATFORM'),
		((0,255,0),'MOVE_PLATFORM'),
		((255,255,0),'LIGHT'),
		((0,255,225),'IN_OUT')
	)

endColor = ((255,127,237),'END')

def makePatterns(pixels,widthPattern,heightPattern,offsetBetween):	
	it = [0,0]
	patterns = []

	while it[1] < pixels.size[1]:
		it[0] = 0
		while it[0] < pixels.size[0]:

			pattern = createPattern(pixels,getRegionPixels(it[0],it[1],widthPattern,heightPattern))
			
			
			
			if( isEndPattern(pattern) ):
				print('Found end cap!')
				it[0] = pixels.size[0]
				it[1] = pixels.size[1]
			else:
				patterns.append(pattern)

			it[0] += widthPattern + offsetBetween

		it[1] += heightPattern + offsetBetween



	return patterns


def isEndPattern(pattern):
	return pattern[0][0] == endColor[1]

def createPattern(pixels,region):
	pattern = []
	for col in region:
		line = []
		for row in col:
			line.append( toPattern(pixels.getpixel(row)) )
		pattern.append(line)

	return pattern

def getRegionPixels(x,y,widthPattern,heightPattern):
	coordinates = []
	for i in range(y,y + heightPattern):
		line = []
		for j in range(x, x + widthPattern):
			line.append( (j,i) )
		coordinates.append(line)
	return coordinates


def toPattern(rgb):
	name = 'EMPTY'

	for c in colors:
		if c[0][0] == rgb[0] and c[0][1] == rgb[1] and c[0][2] == rgb[2]:
			name = c[1]

	chance = rgb[3] - 155

	if chance < 0:
		chance = 0

	if endColor[0][0] == rgb[0] and endColor[0][1] == rgb[1] and endColor[0][2] == rgb[2]:
		return endColor[1]
	else: 
		return '{p: ' + name + ', c: ' + str(chance) + '}'

def toJson(patterns):
	json = '[\n'
	first = True

	for p in patterns:
		if first:
			first = False
		else :
			json += ','
		
		json += '\n\t\t' + packPattern(p)
		'''
		json += '\t\t\t[\n'

	

		json += '\n\t\t\t]\n'
		'''

	return json + '\n\t]'

def packPattern(pattern):

	line = '[\n'
	first = True
	for m in pattern:
		if first:
			first = False
		else:
			line += ','

		line += '\n' + packMatrixPattern(m)

	return line + '\n\t\t]'

def packMatrixPattern(pattern):

	line = '\t\t\t['
	first = True
	for m in pattern:
		if first:
			first = False
		else:
			line += ','

		line += m

	return line + ']'

def writeFile(json,textFileName):
	file = open(textFileName,'w+')
	file.write(json)
	file.close()

def main(imgFileName, textFileName, widthPattern, heightPattern, offsetBetween):

	print('Image file name (input) : ' + imgFileName)
	print('Text file name (output) : ' + textFileName)
	print('Width pattern           : ' + str(widthPattern) + ' px')
	print('Height pattern          : ' + str(heightPattern) + ' px')
	print('Offset between patterns : ' + str(offsetBetween) + ' px')

	print('Converting .....')
	patterns = makePatterns(Image.open(imgFileName),widthPattern,heightPattern,offsetBetween)

	print('Converted ' + str(len(patterns)) + ' patterns')

	json = toJson(patterns)

	#print(json)
	writeFile(json,textFileName)

	print('Saving ....')

	print('Done!')


if __name__ == '__main__':
	if len(sys.argv) == 6:
		main(sys.argv[1],sys.argv[2],int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
	else:
		print('Incorrect argv parameters!!!')
		print('Usage: script.py [Image file name] [Text file name] [Width pattern] [Height pattern] [Offset]')