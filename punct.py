import re, string

filename = r"C:\Users\fpank\Downloads\es-en\es-en\es1.txt"
filename = open(filename, 'r',encoding="utf-8")
file = filename

lst=[]

for word in file:
	word = word.strip('\n')          
	out = re.sub('[%s]' % re.escape(string.punctuation), '', word)
	lst.append(out)
	
	
file1_name=r"C:\Users\fpank\Downloads\es-en\es-en\es_p1.txt"
file1=open(file1_name, 'w',encoding="utf-8").writelines(lst)



