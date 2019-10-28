# # import subprocess
import os
import sys
while True:
	fname = input("File name:: ")
	if os.path.exists(fname):
		break
	else:
		print("File doesn't exist, retry")
x = len(fname)
occurence_number = 0
mult_occurences = list()
sentence_list=list()
#x-4 to ommit extension, won't work for .ts files or files with
#extension not equal to three characters
if not os.path.exists(fname[0:(x-4)]+'.srt'):
    command = './vid.sh '+fname
    print("Generating subs")
    os.system(command)
f = open(fname[0:(x-4)]+'.srt', "r")
z = input('Enter word:').lower()
flag = 0
while f.readline():
    a = f.readline()
    c = f.readline().lower()
    while c and c != '\n':
        if z in c.strip().split():
            if z not in mult_occurences:
                mult_occurences.append(a[:8])
                sentence_list.append(c)
            flag = 1
        c = f.readline().lower()
if not flag:
	print('Not found try entering some other closely related word.')
	sys.exit()
if len(mult_occurences) > 1:
    print("More than one occurence(s) found:")
    for i in range(0, len(mult_occurences)):
        print(i+1, ")  ",sentence_list[i]," at ", mult_occurences[i])
    occurence_number = int(input("Enter your choice to play at: "))-1
else:
    print("Found at ",mult_occurences[0])
t = mult_occurences[occurence_number]
time = int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:])
time_command = './seek.sh '+str(time)+' '+fname
os.system(time_command)
