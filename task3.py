import random
i=0   #кол-во возмонжных итераций
word=input('Input random word: ')
word_list=list(word)

while i<5:
    n = random.sample(word_list,len(word))
    print(n)
    i+=1
    continue


