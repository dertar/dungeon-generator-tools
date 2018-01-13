## The tools for uwague ##
### Room patterns maker -  converts a pixel images of the room into a json file. ###
Used PIL lib.
 * 1 pixel = 1 block
 * Each color equals specific block (see: patterns\palette.png)
 * Alpha channel responds to the block appearance factor(if 255 = 100%; if <= 155 = 0%)
 
 Usage: patterns_room_converter.py [Image file name] [Text file name] [Width pattern] [Height pattern] [Offset between rooms]

see examples in convertPatterns.bat.

  ### Pixels replacer - replaces specific colors to others in image file ###
Used PIL lib.\
Usage: pixel_tool_replace_colors.py [input image file name] [output image file name] [pattern file]

see examples of pattern files in 'pattern' folder

