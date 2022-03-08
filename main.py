#Dictionaries similiar to list. Use key/value pairs. In a dictionay, the word you are looking up is the key, and the definiton is the value

cats = {'Jane':6, 'Tom':12, 'Sox':8} #Cat name Jane (string) is key, age 6 (int) is the value

print(cats)

print(cats['Tom']) #just use key to retive value. Can't feed values, only keys

cats["Wilson"] = 1 #add an  entry to dictonay
print(cats)

del(cats['Tom']) #remove an entry
print(cats)

print(len(cats))

#create a dictionay with ints fo rkeys and Booleans for values

dict = {1:True, 2:False}
print(dict)

