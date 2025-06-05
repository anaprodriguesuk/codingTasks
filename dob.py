# Opening the file to read
with open('DOB.txt', 'r+') as file:
    line = file.read()

'''Spliting the  lines, and the words in each line,
If words length is more or equal 2 the first[0] and second[1] words 
are printed out'''

sections = line.split("\n")
   
for i in sections:
    words = i.split()
    if len(words) >= 2:
        print(words[0], words[1])
       
print()
     
''' A new 'for loop' to print the other data in the line at the same time
If the length words is less or equal 5 the third[2], fourth[3], and fifth[4] 
words are printrd out'''      
       
for i in sections:
    words = i.split()
    if len(words) >= 5:
        print(words[2], words[3], words[4])
