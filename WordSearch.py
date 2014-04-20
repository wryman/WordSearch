
#  File: WordSearch.py

#  Description:  Solves a wordsearch (excluding diagonals)

#  Student Name:  William Ryman

#  Student UT EID:  wrr368	


#  Course Name: CS 303E 

#  Unique Number: 

#  Date Created: 4/20/14

#  Date Last Modified: 4/20/14

#prints selected range of lines from startline
	#This section defines m rows by n columns
startline1 = 0
stopline1=0 # or whatever line I need to jump to
hidden1 = open('hidden.txt', "r")
linesCounter1 = 1
for line in hidden1:
	if linesCounter1 > startline1 and linesCounter1<=stopline1+1:
		line=line.rstrip('\n')
		for i in range(len(line)):
			if line[i]==' ':
				m=(line[0:i])
				n=int(line[i+1:])
	linesCounter1 += 1
print(m)
print(n)
hidden1.close()

startline2 = 0
stopline2=0 # or whatever line I need to jump to
hidden2 = open('hidden.txt', "r")
linesCounter2 = 1
for line in hidden2:
	if linesCounter2 > startline2 and linesCounter2<=stopline2+1:
		line=line.rstrip('\n')
		for i in range(len(line)):
			if line[i]==' ':
				m=(line[0:i])
				n=int(line[i+1:])
	linesCounter2 += 1
print(m)
print(n)
hidden2.close()