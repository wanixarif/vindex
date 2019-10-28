# # import subprocess
import os
fname=input("File name and start pos")
x=len(fname)
mult_occurences=list()
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
            flag = 1
        c = f.readline().lower()
if not flag:
	print('Not found')
t=mult_occurences[0]
time=int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:])
time_command='./seek.sh '+str(time)+' '+fname
os.system(time_command)


# fp = open(fname[0:(x-4)]+'.srt',"r")
# read=fp.readlines()
# with open("x.txt","w") as new:
#     for i in read:
#         new.write(i)
# # for y in read:
# #     print("Found")
# fp.close()

