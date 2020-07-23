import re
# import fuzzywuzzy

def hasNumbers(inputString):
	return bool(re.search(r'\d', inputString))

file = "D:\\ITC - Projects\\Restaurant Predictor\\tester.txt"

text_file = open(file, 'r+')

text = text_file.readlines()
text = ''.join(text)

volume = re.findall('Vol[\n]*.*|VOL[\n]*.*', text)

only_volume = volume[:]
i = 0

while(True):
    if(i == len(only_volume)):
        break

    if not hasNumbers(only_volume[i]):
        only_volume.pop(i)

    else:
        i += 1

for i in range(len(only_volume)):
	print(only_volume[i])
	var = re.findall("[0-9]*[.|,]{0,2}[0-9]+",only_volume[i])
	if(len(var) > 0):
		var = var[0]
	print(var)
	print()
