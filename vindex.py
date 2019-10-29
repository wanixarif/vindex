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
found=True
isint=1
#x-4 to ommit extension, won't work for .ts files or files with
#extension not equal to three characters
if not os.path.exists(fname[0:(x-4)]+'.srt'):
    command = './vid.sh '+fname
    print("Generating subs")
    os.system(command)
while found:
    subs_file = open(fname[0:(x-4)]+'.srt', "r")
    search_term = input('Enter word:').lower()
    while subs_file.readline():
        flag = 0
        time_stamp = subs_file.readline()
        line = subs_file.readline().lower()
        para=''
        while line and line != '\n':
            para+=line
            if search_term in line.strip().split():
                if search_term not in mult_occurences:
                    mult_occurences.append(time_stamp[:8])
                flag = 1
                found=False
            line = subs_file.readline().lower()
        if(flag==1):
            sentence_list.append(para)
    if not flag:
        print('Not found try entering some other closely related word.')
if len(mult_occurences) > 1:
    print("More than one occurence found:")
    for i in range(0, len(mult_occurences)):
        print(i+1, ") ",sentence_list[i]," at ", mult_occurences[i],sep='')
    while isint:
        try:
            occurence_number = int(input("Enter your choice to play at: "))-1
            if occurence_number<len(mult_occurences) and occurence_number>0:
                isint=0
            else:
                print("Invalid choice")
        except:
            print("Invalid choice")
else:
    print("Found at ",mult_occurences[0])
t = mult_occurences[occurence_number]
time = int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:])
time_command = './seek.sh '+str(time)+' '+fname
os.system(time_command)
