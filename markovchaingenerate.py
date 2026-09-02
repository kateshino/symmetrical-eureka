import sys
import json

command = sys.argv
input = command[1]
output = command[2]
wordlist = ""
chain = {}

input = open(input, "r")
for line in input:
	wordlist += line
wordlist = wordlist.strip()
wordlist = wordlist.replace("\n","")
wordlist = wordlist.lower()
wordlist = wordlist.split(" ")

for word in range(len(wordlist)):
	if wordlist[word] not in chain:
		chain[wordlist[word]] = []
	nextword = ""
	if word != len(wordlist) - 1:
		nextword = wordlist[word + 1]
	wordpresent = False
	while wordpresent == False:
		for i in chain[wordlist[word]]:
			if nextword in i:
				wordpresent = True
				i[1] += 1
		break
	if wordpresent == False:
		chain[wordlist[word]].append([nextword,1])

output = open(output, "a")
output.write(json.dumps(chain))
