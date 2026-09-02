import sys
import random
import json
command = sys.argv
input = command[1]
input = open(input, "r")
chain = json.load(input)

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
