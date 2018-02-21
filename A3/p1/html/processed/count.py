import os
import subprocess
pth = '/Python27/Assignment3/p2/html/processed/'
text_files = [f for f in os.listdir(pth) if f.endswith ('.processed.txt')]
fileindex = 0
numberoffiles = 0


while (fileindex < len(text_files)):
	wordcount=0
	for line in open (text_files[fileindex]):
		if line in open (text_files[fileindex]):
			if 'blue' in line:
				wordcount = wordcount+1
		if (wordcount>0):
			numberoffiles = numberoffiles+1
		print text_files[fileindex] + ' Processed files had word (blue): ' + '{0}'.format(wordcount) + 'times'
		fileindex= fileindex+1
