from __future__ import absolute_import
from __future__ import print_function
import six

import language_check

from tkinter import *
from tkinter import messagebox

import rake
import operator
import io

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

counter=1
file=open("questions.txt","r")
q=[line.rstrip('\n') for line in file]
totmark=[0,0,0,0,0]

def nex():
    global counter
    if(counter<5):
        counter=counter+1
        ques.set(str(q[counter-1]))
        
    else:
        messagebox.showwarning("Limit Exceeded","Sorry, No more questions available!")

def prev():
    global counter
    if(counter>1):
        counter=counter-1
        ques.set(str(q[counter-1]))
    else:
        messagebox.showwarning("Limit Exceeded","This is the first question!")

def finish():  
    s=0
    for i in totmark:
        s=s+i
    one = str(totmark[0])
    two = str(totmark[1])
    three = str(totmark[2])
    four = str(totmark[3])
    five = str(totmark[4])
    for i in range(5):
        if totmark[i]<=0.5:
            if i==0:
                rem1 = "Not Known"
            if i==1:
                rem2 = "Not Known"
            if i==2:
                rem3 = "Not Known"
            if i==3:
                rem4 = "Not Known"
            if i==4:
                rem5 = "Not Known"     
        if totmark[i]>0.5 and totmark[i]<=1:
            if i==0:
                rem1 = "Vaguely Understood"
            if i==1:
                rem2 = "Vaguely Understood"
            if i==2:
                rem3 = "Vaguely Understood"
            if i==3:
                rem4 = "Vaguely Understood"
            if i==4:
                rem5 = "Vaguely Understood"
        if totmark[i]>1 and totmark[i]<=1.5:
            if i==0:
                rem1 = "Moderately Understood"
            if i==1:
                rem2 = "Moderately Understood"
            if i==2:
                rem3 = "Moderately Understood"
            if i==3:
                rem4 = "Moderately Understood"
            if i==4:
                rem5 = "Moderately Understood"
        if totmark[i]>1.5:
            if i==0:
                rem1 = "Satisfactory"
            if i==1:
                rem2 = "Satisfactory"
            if i==2:
                rem3 = "Satisfactory"
            if i==3:
                rem4 = "Satisfactory"
            if i==4:
                rem5 = "Satisfactory" 
    messagebox.showinfo("Results","Marks for first question = "+one+"\nMarks for second question = "+two+"\nMarks for third question = "+three+"\nMarks for fourth question = "+four+"\nMarks for fifth question = "+five+"\n\nThe total score obtained in the test="+str(s)+"/10\n\nRemarks from the teacher : \n\tFor Question 1: "+rem1+"\n\tFor Question 2: "+rem2+"\n\tFor Question 3: "+rem3+"\n\tFor Question 4: "+rem4+"\n\tFor Question 5: "+rem5)  

def enFunc():
    
    global counter
    
    ans = entry.get('1.0','end')
    n=0
    for line in ans:
        words=[line.split(' ') for line in ans]
    n=len(words)
    if(n>=37):
        marks1=5
    elif(n>=27):
        marks1=3
    else:
        marks1=0
            
    a=marks1
    
    fname="data/docs/mp"+str(counter)+".txt"


    stoppath = "data/stoplists/SmartStoplist.txt"

    rake_object = rake.Rake(stoppath)
    sample_file = io.open(fname, 'r',encoding="iso-8859-1")
    text = ans

    sentenceList = rake.split_sentences(text)
    stopwords = rake.load_stop_words(stoppath)
    stopwordpattern = rake.build_stop_word_regex(stoppath)
    phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern, stopwords)

    wordscores = rake.calculate_word_scores(phraseList)

    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
    keyw=dict(rake_object.run(text))
    f1=io.open(fname, 'r',encoding="iso-8859-1")
    text1=f1.read()
    que=text1.split("\n")
    print(que[0])
    l=text1.split("\n\n")
    kw=l[2].split("\n")
    print("Keyword in original file = ",kw)
    total=len(kw)
    print("No of keywords in original file = ",total)

    c=0
    for i in keyw:
        for j in range(0,total):
            if(kw[j].lower() in i.lower()):
                print("Detected = " +str(i))
                c=c+1
    print("Count = ",c)

    percentage=(c/total)*100

    if(percentage>=90):
        marks2=35
        message = "Marks obtained for keyword:" + str(marks2) + "/30"

    elif(percentage>=80 and percentage<90):
        marks2=33
        message = "Marks obtained for keyword:"+ str(marks2) + "/30"

    elif(percentage>=70 and percentage<80):
        marks2=30
        message = "Marks obtained for keyword:" + str(marks2) + "/30"

    elif(percentage>=60 and percentage<80):
        marks2=27
        message = "Marks obtained for keyword:" + str(marks2) + "/30"

    elif(percentage>=50 and percentage<60):
        marks2=25
        message = "Marks obtained for keyword:" + str(marks2) + "/30"

    elif(percentage>=40 and percentage<50): 
        marks2=20
        message = "Marks obtained for keyword:" + str(marks2) + "/30"
        
    else:
        marks2 = 0
        message = "Marks obtained for keyword:" + str(marks2) + "/30"
   
    b=marks2

    tool=language_check.LanguageTool('en-US')

    count=0
    text=str(ans)
    txtlen=len(text.split())
    setxt = set(text.split())
    setlen = len(setxt)
    matches=tool.check(text)
    print("No. of Errors = ",len(matches))
    noOfError=len(matches)
    for i in range (0,noOfError):
        print(matches[i].msg)
    
    if (noOfError<=3 and n>0):
        marks3=10
    elif (noOfError<=5):
        marks3=8
    elif (noOfError<=8):
        marks3=5
    else:
        marks3=0
    print("Marks obtained after parsing =",marks3,"/10")
    c=marks3
    d=a+b+c

    print("Marks obtained out of 50 is =",d,"/50")
    tot=(d/50)*2
    global totmark
    totmark[counter-1]=tot

def showrpt():
    objects = ('Question 1', 'Question 2', 'Question 3','Question 4','Question 5')
    y_pos = np.arange(len(objects))
    performance = [totmark[0],totmark[1],totmark[2],totmark[3],totmark[4]]
    plt.xlim(0, 2)
    plt.barh(y_pos, performance, align='center', alpha=0.5,color="yellow")
    plt.yticks(y_pos, objects)

    plt.xlabel('Student\'s understanding level')
    plt.title('Student\'s knowledge analysis')
    plt.show() 

root = Tk()
root.geometry('800x1800')
label= Label(root,text="ANSWER ALL THE FOLLOWING QUESTIONS",bg="lightyellow",bd=20)
label.place(x=300,y=10)

ques= StringVar()
ques.set(str(q[counter-1]))
labelQ=Label(root,textvariable=ques,text=str(q[0]),width=100, bg="lightyellow", bd=20)
labelQ.place(x=10,y=100)

entry= Text(root)
entry.place(x=100,y=200)

prevBtn= Button(root, text = '<', command = prev)
prevBtn.place(x=120,y=600)

button1= Button(root, text = 'Submit', command = enFunc)
button1.place(x=400,y=600)

nextBtn= Button(root, text = '>', command = nex)
nextBtn.place(x=700,y=600)

finishbtn=Button(root,text='Finish',command=finish)
finishbtn.place(x=300,y=650)

showrpt=Button(root,text='Show report',command=showrpt)
showrpt.place(x=500,y=650)

root.mainloop()

