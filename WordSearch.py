
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
				m=int(line[0:i])
				n=int(line[i+1:])
	linesCounter1 += 1
hidden1.close()


# stores each line of the puzzle in a list where each element corresponds to one line
startline2 = 2
stopline2=m+2 # or whatever line I need to jump to
hidden2 = open('hidden.txt', "r")
linesCounter2 = 1
puzzlelines=[]
for line in hidden2:
	if linesCounter2 > startline2 and linesCounter2<=stopline2+1:
		line=line.rstrip('\n')
		puzzlelines.append(line)
	linesCounter2 += 1
hidden2.close()
print('m=',m)
print('n=',n)
print(puzzlelines)
puzzlecols=[]
#prints first column as seperate strings
#for some reason even numbered indexed of q are blank
for q in puzzlelines:
	print(q[0])
