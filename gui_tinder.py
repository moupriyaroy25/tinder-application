from tkinter import*
from tinder_backend import*
from tkinter import messagebox
class TinderGUI:
 def __init__(self):
        self.root=Tk()
        self.root.maxsize(300,900)
        self.root.title("TINDER")
        self.tinderbackend=TinderBackend()
        lbl=Label(self.root,text="WELCOME TO TINDER",width=25,height=3,bg="pink",font=('Courier,12'))
        lbl.grid(row=0,column=0)
        btnLogin=Button(self.root,text="LOG IN",width=12,height=2,bg="Skyblue",command=lambda:self.userlogin())
        btnLogin.grid(row=1,column=0,padx=10,pady=10)
        btnRegister = Button(self.root, text="REGISTER", width=12, height=2, bg="Skyblue",command=lambda:self.userregister())
        btnRegister.grid(row=2, column=0, padx=10, pady=10)
        btnExit=Button(self.root, text="EXIT", width=12, height=2, bg="Skyblue",command=lambda:self.root.destroy())
        btnExit=btnExit.grid(row=3, column=0, padx=10, pady=10)
        self.root.mainloop()
 def userlogin(self):
        child=Toplevel(master=self.root)
        child.maxsize(300,900)
        child.title("Login")
        lblemail=Label(child,text="email",width=10,height=2,font=('Courier',12)).grid(row=0,column=0)
        entemail=Entry(child,width=20)
        entemail.grid(row=0,column=1,padx=20)
        lblpassword=Label(child,text="password",width=10,height=2,font=('Courier',12)).grid(row=1,column=0,pady=30)
        entpassword=Entry(child, width=20,show="*")
        entpassword.grid(row=1, column=1, padx=20)
        btnSubmit=Button(child,text='submit',width=10,height=1,bg="Skyblue",font=('Courier',12),command=lambda:self.uservalidate(child,entemail.get(),entpassword.get())).grid(row=2,column=0)
 def uservalidate(self,child,uemail,upass):
        flag=self.tinderbackend.verifyuser(uemail,upass)
        if flag!="":
            messagebox.showinfo("succsses","Successful Login")
            child.destroy()
            self.usermenu(flag)
        else:
            messagebox.showinfo("error","Invalid credentials!")

 def userregister(self):
        child = Toplevel(master=self.root)
        child.maxsize(300, 900)
        child.title("Register")

        lblname = Label(child, text="name", width=10, height=2, font=('Courier', 12)).grid(row=0, column=0)
        entname = Entry(child, width=20)
        entname.grid(row=0, column=1)
        lblemail=Label(child,text="email",width=10,height=2,font=('Courier',12)).grid(row=1,column=0)
        entemail = Entry(child, width=20)
        entemail.grid(row=1, column=1)
        lblpassword=Label(child,text="password",width=10,height=2,font=('Courier',12)).grid(row=2,column=0)
        entpassword = Entry(child, width=20)
        entpassword.grid(row=2, column=1)
        lblgender = Label(child, text="gender", width=10, height=2, font=('Courier', 12)).grid(row=3, column=0)
        entgender = Entry(child, width=20)
        entgender.grid(row=3, column=1)
        lblcity = Label(child, text="city", width=10, height=2, font=('Courier', 12)).grid(row=4, column=0)
        entcity = Entry(child, width=20)
        entcity.grid(row=4, column=1)
        btnSubmit=Button(child,text="Submit",width=10,height=2,bg='SkyBlue',command=lambda:self.getdetails(child,entname.get(),entemail.get(),entpassword.get(),entgender.get(),entcity.get()))
        btnSubmit.grid(row=5,column=0)


 def getdetails(self,child,name,email,password,gender,city):
        self.tinderbackend.adduser(name,email,password,gender,city)
        messagebox.showinfo("Success","Registration Successful")
        child.destroy()

 def usermenu(self,name):
       self.umenu= Toplevel(master=self.root)
       self.umenu.maxsize(500, 900)
       lblWelcome=Label(self.umenu,text="WELCOME!%s"%(name),width=30,height=3,font=('Courier', 12)).grid(row=0,column=0)
       btnviewallusers=Button(self.umenu,text="View All Users",width=20,height=4,bg='SkyBlue',font=('Courier', 12),command=lambda :self.viewallusers()).grid(row=1,column=0,pady=10)
       btnpropose=Button(self.umenu,text="Propose Someone",width=20,height=4,bg='SkyBlue',font=('Courier', 12),command=lambda :self.propose()).grid(row=2,column=0,pady=10)
       btnviewsentproposals=Button(self.umenu,text="View Sent Proposals",width=20,height=4,bg='SkyBlue',font=('Courier', 12),command=lambda :self.viewsentproposals()).grid(row=3,column=0,pady=10)
       btnviewreceivedproposals = Button(self.umenu, text="View Received Proposals", width=30, height=4,bg='SkyBlue',font=('Courier', 12), command=lambda: self.viewreceivedproposals()).grid(row=4,column=0,pady=10)
       btnviewmatches=Button(self.umenu,text="View Matches",width=20,height=4,bg='SkyBlue',font=('Courier', 12),command=lambda :self.viewmatches()).grid(row=5,column=0,pady=10)
       btnlogout=Button(self.umenu,text="Log Out",width=20,height=4,bg='SkyBlue',font=('Courier', 12),command=lambda :self.root.destroy()).grid(row=6,column=0,pady=10)

 def viewallusers(self):
       userlist=self.tinderbackend.view_all_users()
       viewalluser=Toplevel(master=self.umenu)
       viewalluser.maxsize(500,900)
       c=0
       for i in userlist:
              lblUser=Label(viewalluser,text="%s %s %s %s"%(i[0],i[1],i[4],i[5]),width=30,height=3).grid(row=c,column=0)
              c=c+1
 def propose(self):
       userlist=self.tinderbackend.view_all_users()
       self.propose=Toplevel(master=self.umenu)
       self.propose.maxsize(500,900)
       lbl=Label(self.propose,text="MAKE YOUR MOVE",width=30,height=3,font=('Courier', 12)).grid(row=0,column=0)
       c = 0
       for i in userlist:
           lblUser = Label(self.propose, text="%s %s " % (i[0], i[1]), width=30, height=3).grid(row=c,column=0)
           btn=Button(self.propose,text="propose",width=10,height=3,bg="skyblue",font=('Courier', 12),command=lambda :self.enterid()).grid(row=c,column=1)
           c=c+1
 def enterid(self):
       enterid=Toplevel(master=self.propose)
       enterid.maxsize(300,900)
       lbljuliet_id = Label(enterid, text="Enter Juliet id", width=10, height=2, font=('Courier', 12)).grid(row=1, column=0)
       entjuliet_id = Entry(enterid, width=20)
       entjuliet_id.grid(row=1, column=1)
       btnSubmit = Button(enterid, text="Submit", width=10, height=2, bg='SkyBlue',command=lambda: self.getid(entjuliet_id.get()))
       btnSubmit.grid(row=2, column=0)
 def getid(self,juliet_id):
       self.tinderbackend.propose(juliet_id)
       messagebox.showinfo("sent","Proposal Sent!!!")
       self.propose.destroy()
 def viewsentproposals(self):
       sentproposals=self.tinderbackend.view_sent_proposals()
       viewsentproposals = Toplevel(master=self.umenu)
       viewsentproposals.maxsize(500, 900)
       c=0
       for i in sentproposals:
           lblsentproposals=Label(viewsentproposals,text="%s %s %s"%(i[4],i[7],i[8]),width=30,height=3).grid(row=c,column=0)
           c=c+1
 def viewreceivedproposals(self):
       receivedproposals=self.tinderbackend.view_recieved_proposal()
       viewreceivedproposals = Toplevel(master=self.umenu)
       viewreceivedproposals.maxsize(500, 900)
       c=0
       for i in receivedproposals:
           lblreceivedproposals=Label(viewreceivedproposals,text="%s %s %s"%(i[4],i[7],i[8]),width=30,height=3).grid(row=c,column=0)
           c=c+1
 def viewmatches(self):
     matches = self.tinderbackend.view_matches()
     viewmatches = Toplevel(master=self.umenu)
     viewmatches.maxsize(500, 900)
     c=0
     for i in matches:
         lblmatches=Label(viewmatches,text="%s %s %s"%(i[4],i[7],i[8]),width=30,height=3).grid(row=c,column=0)
         c=c+1



ob=TinderGUI()


