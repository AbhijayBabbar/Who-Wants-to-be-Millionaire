import csv
import random
from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from pygame import mixer

class game:

    def loadgame(self):
        self.questioncount = 0
        self.list1 = []
        count = 0
        while True:
            n = random.randint(3, 49)
            if count == 15:
                break
            elif not (n in self.list1):
                self.list1.append(n)
                count = count + 1

        rd = open("data.csv", "r", encoding="utf-8")

        crd = csv.reader(rd)

        self.databank = []

        for p in crd:
            for i in range(0, len(self.list1)):
                if str(self.list1[i]) == p[0]:
                    d = {"ques": p[1], "optiona": p[2], "optionb": p[3], "optionc": p[4], "optiond": p[5], "ans": p[6]}
                    self.databank.append(d)

        for ques in self.databank:
            print(ques)

        self.ques1 = self.databank[self.questioncount]

        self.lb1["text"]=self.ques1["ques"]
        self.rd1["text"]=self.ques1["optiona"]
        self.rd2["text"]=self.ques1["optionb"]
        self.rd3["text"]=self.ques1["optionc"]
        self.rd4["text"]=self.ques1["optiond"]
        self.result=0
        self.a.set(0)


    def nextquestion(self):

       mixer.init()
       mixer.music.load('lock.mp3')
       mixer.music.play()

       if askyesno("KBC","Are you Sure You want to Lock")==1:

            flag=False
            if self.databank[self.questioncount]["ans"]=="A" and self.a.get()==1:
                flag=True
            elif self.databank[self.questioncount]["ans"]=="B" and self.a.get()==2:
                flag = True
            elif self.databank[self.questioncount]["ans"]=="C" and self.a.get()==3:
                flag = True
            elif self.databank[self.questioncount]["ans"] == "D" and self.a.get() == 4:
                flag = True


            if flag==True:
                showinfo("KBC","Right Answer")
                self.questioncount=self.questioncount+1
                q=self.databank[self.questioncount]
                self.lb1["text"]=q["ques"]
                self.rd1["text"]=q["optiona"]
                self.rd2["text"]=q["optionb"]
                self.rd3["text"]=q["optionc"]
                self.rd4["text"]=q["optiond"]
                self.result=self.result+1
            else:
                showerror("KBC","Wrong Answer Game will Restart")
                self.loadgame()
            self.a.set(0)
            # self.lb2["text"]=str(self.result)

    def __init__(self):



        self.result=0
        self.root=Tk()
        self.root.config(background="#705285")

        self.p1=PanedWindow(self.root,bg='#705285')
        self.p2=PanedWindow(self.root,bg='#705285')
        self.left=Frame(self.p2,bg='#705285')
        self.right=Frame(self.p2,bg='#705285')
        self.left.grid(row=0,column=0)
        self.right.grid(row=0,column=1)
        self.p3=PanedWindow(self.root,bg='#705285')
        self.p1.pack()
        self.p3.pack()
        self.p2.pack()


        img = PhotoImage(file="KBC-Logo.png",width="200",height="200")  # only .png img
        self.lb3=Label(self.p1, image=img)
        self.lb3.pack()

        mixer.init()
        mixer.music.load('welcome.mp3')
        mixer.music.play()
        self.lb3["image"]=None

        self.a = IntVar()
        self.root.geometry("1024x800")
        self.lb1=Label(self.p3)
        self.rd1=Radiobutton(self.left,variable=self.a,value=1)
        self.rd2 = Radiobutton(self.left,variable=self.a,value=2)
        self.rd3 = Radiobutton(self.left,variable=self.a,value=3)
        self.rd4 = Radiobutton(self.left,variable=self.a,value=4)
        self.rd5 = Radiobutton(self.left,text="1000",bg='brown')
        self.rd6 = Radiobutton(self.left, text="2000", bg='brown')
        self.rd7 = Radiobutton(self.right, text="3000", bg='brown')
        self.rd8 = Radiobutton(self.right, text="5000", bg='brown')
        self.rd9 = Radiobutton(self.right, text="10000", bg='brown')
        self.rd10 = Radiobutton(self.right, text="20000", bg='brown')
        self.rd11= Radiobutton(self.right, text="40000", bg='brown')
        self.rd12 = Radiobutton(self.right, text="80000", bg='brown')
        self.rd13 = Radiobutton(self.right, text="160000", bg='brown')
        self.rd14 = Radiobutton(self.right, text="320000", bg='brown')
        self.rd15 = Radiobutton(self.right, text="640000", bg='brown')
        self.rd16 = Radiobutton(self.right, text="1250000", bg='brown')
        self.rd17 = Radiobutton(self.right, text="2500000", bg='brown')
        self.rd18 = Radiobutton(self.right, text="5000000", bg='brown')
        self.rd19 = Radiobutton(self.right, text="10000000", bg='brown')
        self.rd20 = Radiobutton(self.right, text="70000000", bg='brown')

        self.bt1=Button(self.p2,text="Lock it",command=self.nextquestion,bg='lightgreen',width=10)
        # self.lb2=Label(self.p2,text="")
        self.lb1.config(background="#705285",fg="black",font=(None,25))
        self.rd1.config(background="#705285",fg="black",font=(None,20))
        self.rd2.config(background="#705285",fg="black",font=(None,20))
        self.rd3.config(background="#705285",fg="black",font=(None,20))
        self.rd4.config(background="#705285",fg="black",font=(None,20))



        self.loadgame()

        self.lb1.grid(row=0,column=0)
        self.rd1.grid(row=1,column=0)
        self.rd2.grid(row=2,column=0)
        self.rd3.grid(row=3,column=0)
        self.rd4.grid(row=4,column=0)
        self.bt1.grid(row=2,column=0)
       

        # self.lb2.grid(row=3,column=1)


        self.root.mainloop()



#----------------------------------------------
obj=game()



