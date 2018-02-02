#!/usr/bin/python3
import sys,os,glob,random

# Check Arguments 
if len(sys.argv) < 2 :
	print ("\n\tUsage   : omxfolder.py [OPTION] DIR")
	print ("\n\tExample : omxfolder.py /home/Music")
	print ("\tExample : omxfolder.py -s .")
	print ("\tExample : omxfolder.py -s -r ~/Music\n")
	print ("\tOPTIONS : \n")
	print ("\t\t  -r\tRecursive")
	print ("\t\t  -s\tShuffle")
	print ("\t\t  -l\tOnly print files\n")
	exit()

if "-r" in sys.argv : 
	recursive_flag = True
else : 
	recursive_flag = False

if "-s" in sys.argv : 
	shuffle_flag = True
else : 
	shuffle_flag = False

if "-l" in sys.argv : 
	list_flag = True
else : 
	list_flag = False

# To make sure Dir has same format
dir = sys.argv[-1]
if dir[-1] == '/':
	dir = dir[0:-1]
	
dir = glob.escape(dir)

audio_files = []

def add_files (type_file) : 
	if recursive_flag == True : 
		for f in glob.iglob(dir + '/**/*.'+type_file, recursive=recursive_flag) :
			audio_files.append(str(f))
	else : 
		for f in glob.iglob(dir + '/*.'+type_file, recursive=recursive_flag) :
			audio_files.append(str(f))

print ("playing audios in "+str(dir))
add_files("mp3")
add_files("flac")
add_files("m4a")

if shuffle_flag == True : 
	audio_files = random.sample(audio_files,len(audio_files))

for afile in audio_files:
	if list_flag == True : 
		print (afile)
	else : 
		print (afile)
		os.system('omxplayer "'+afile+'"')




