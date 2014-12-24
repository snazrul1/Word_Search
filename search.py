__author__='Sadat'

import re

file=open('README.md')
str2search=''

for message in file:
	str2search += message 

#Look for all possible combination of the word 'code'
word='(C|c)(O|o)(D|d)(E|e)'
compile_word=re.compile(word)

#Search for 'code' on the README.md
word_search=re.search(compile_word,str2search)

#Determine frequency of the word 'code'
word_frequency=re.findall(compile_word,str2search)
count=0
for word in word_frequency:
    count += 1

#Print output
print
print 'Word searched:'
print(word_search.group())
print
print 'Frequency:'
print str(count)
print
