from urllib.parse import unquote
import re

for i in range(1, 255):
	str = '/index.php/path%{:02X}info.php'
	url = str.format(i)
	#url = '/index.php/pathinfo.php'
	url = unquote(url)

	pattern = "^(.+?\.php)(/.*)$"
	match = re.match(pattern, url)
	#If-statement after search() tests if it succeeded
	
	if match:
	   print("regex matches: ", match.group(2))
	else:
		print("current no: ", i )
		print('pattern not found')