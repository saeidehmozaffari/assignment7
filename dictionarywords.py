#!/usr/bin/env python
# coding: utf-8

# In[14]:


def loading():
    try:
        myFile=open('dictionary.txt','r')
        rows=myFile.read().split('\n')
        myFile.close()
        for i in range(len(rows)):
            if rows[i]=='':
                break
            else:
                myword=rows[i].split(',')
                words.append({'english':myword[0],'persian':myword[1]})
        #print(words)
        print('dictionary loaded')
        return 1
    except:
        print('file not found please chek your adress')
        return 0
def showMenu():
    print('1- add new word ')
    print('2- translation english to persian')
    print('3- translation persian to english')
    print('4- exit')
def addWord():
    words.append({'english':input('enter english word'),'persian':input('ener persian word')})
    print('new word added')
    print(words)

def enTpr():
    wordList=[]
    trlist=[]
    sentences=input('enter english sentences')
    sentence=sentences.split('.')
    #print(sentence)
    for s in range(len(sentence)):
        wordList.append(sentence[s].split(' '))
    #print(wordList)
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            for w in words:
                if wordList[i][j]==w['english']:
                    trlist.append((w['persian']))
                    break
    print(trlist)
def prTen():
    wordList=[]
    trlist=[]
    sentences=input('enter persian sentences')
    sentence=sentences.split('.')
    for s in range(len(sentence)):
        wordList.append(sentence[s].split(' '))
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            for w in words:
                if wordList[i][j]==w['persian']:
                    trlist.append(w['english'])
                    break
    print(trlist)
def saveDic():
    myFile=open('dictionary.txt','w')
    for i in range(len(words)):
        myFile.write(words[i]['english']+','+words[i]['persian']+'\n')
    myFile.close()
words=[]    
x=loading()
if x==1:
    while True:
        showMenu()
        choice=int(input('enter a number:'))
        if choice==1:
            addWord()
        elif choice==2:
            enTpr()
        elif choice==3:
            prTen()
        elif choice==4:
            saveDic()
            break
        else:
            print('enter a currect number')

