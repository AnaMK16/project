
# Word order
NumberOfWords = int(input("Enter the amount of words: "))

#create empty dictionary 
wordsDictionary = {} 

for each in range(NumberOfWords):
    key = input("Enter the word: ") # Enters string value NumberOfWords times 

    if key in wordsDictionary.keys(): # checks if input value is one of the keys of wordsDictionary 
        wordsDictionary[key]+=1 # if the condition is true value of the input string increases 


    else:
        wordsDictionary[key]  = 1
     # if it's false new entry will be created, where key is input string and its value equals to 1    

    
print(len(wordsDictionary))

for word, occurency in wordsDictionary.items():
    print(occurency,end = " ") #iterate over wordDictionary items and print the value

#Lexicographic order
Number_of_words = int(input("Enter Number"))
for _ in range(Number_of_words):
    s = input() #input string Number_of_words times
    s = list(s[::-1]) #reverses s
    done = 0
    for i in range(1,len(s)):
        if s[i-1] > s[i]: #if a string element is greater than the previous element , code block will be executed 
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:  #if a condition is false, following code block will be executed   
        print("No Answer") 


# Bomberman Game    

def bomb(b,r,c):
    field = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j] == 'O':
                field[i][j] = '.'
                if i+1<r:
                    field[i+1][j] = '.'
                if i>0:
                    field[i-1][j] = '.'
                if j+1<c:
                    field[i][j+1] = '.'
                if j>0:
                    field[i][j-1] = '.'
    return field

r,c,n = input().split()
r,c,n = int(r),int(c),int(n)
b = []
for i in range(r):
        row = list(input())
        b.append(row)
if n%2==0:
    f = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        print(''.join(map(str,f[i])))
else:
    bombed1 = bomb(b,r,c)               
    bombed2 = bomb(bombed1,r,c)  
    
    if n==1:
        for i in range(r):
            print(''.join(map(str,b[i])))
    elif (n+1)%4==0:
        for i in range(r):
            print(''.join(map(str,bombed1[i])))
    elif (n+2)%4==0:
        for i in range(r):
            print(''.join(map(str,b[i])))
    else:
        for i in range(r):
            print(''.join(map(str,bombed2[i])))







          
