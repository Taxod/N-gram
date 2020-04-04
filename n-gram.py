import time
import re
import operator

'''
Python 3.7.6
Anaconda Prompt
conda 4.8.3  
Windows 10

Agenda
1. read word data (txt)
2. clean the data, remove puncation, alpha and numeric
3. count the tf and store into the dictionary and sort
4. write to the csv file
'''
def clean_data(inputString):
	inputString = re.sub(r'[^\w]','',inputString)
	inputString = re.sub(r'[A-Za-z0-9]','',inputString)
	return inputString

print("start time: ", end="")
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)

#read data and print data shape
filename = "Text.txt"
fp = open(filename,"r")
Text = fp.read()
fp.close()
Text = clean_data(Text)

#initail a dictionary
_dict ={}

#set the gram
N_gram = 2

print("N-gram = ",end = "")
print(N_gram)


for i in range(0,len(Text)-(N_gram - 1)):
	#slice
	gram = Text[i:i+N_gram]
	#clean chinese punctuation
	if ('，' in gram or '。' in gram or '；'in gram or ' ' in gram or '、' in gram):
		continue
	else:
		#count the frequency and store in the dictionary
		if gram not in _dict:
			_dict[gram] = 0
		_dict[gram] +=1


#(optional) To remove the frequency less than specific times 
# specific_times = 50
# _dict = {key:value for key, value in _dict.items() if value > specific_times}


#sort the dictionary
_dict = {key: value for key, value in sorted(_dict.items(), key=lambda item: item[1],reverse = True)}

#write into the file
filename = str(N_gram) + "_gram.csv"
fp = open(filename,"w")
for key in _dict.keys():
        fp.write("%s, %s\n" % (key, _dict[key]))
fp.close()

print("end time: ", end="")
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)