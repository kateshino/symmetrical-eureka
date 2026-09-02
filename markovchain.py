import sys
import random

command = sys.argv
input = command[1]
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

sentence = ""
count = 0
til = random.randrange(0,len(chain))	
for word in chain:
	count += 1
	if count == til:
		if word[len(word) - 1] == ".":
			til += 1
		else:
			sentence += word
			break
endsent = False
while endsent == False:
	lastword = sentence.split(" ")
	lastword = lastword[len(lastword)-1]
	nextwords = []
	for i in chain[lastword]:
		for x in range(0,i[1]):
			nextwords.append(i[0])
	nextword = random.choice(nextwords)
	sentence = sentence + " " + nextword
	if nextword[len(nextword) - 1] == "." or nextword[len(nextword) - 1] == "?" or nextword[len(nextword) - 1] == "!":
		endsent = True
print(sentence)
