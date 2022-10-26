import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

#------------FEATURES OF PROJECT------------------#

class features:

    def logout(self):
        main.destroy()
        gui.login()

    def calculate(self):

        global SBalance, sales, rent, SalExp, InvExp, OtherExp, utilities, purchases

#An unexpected error was occuring whenever any field was left empty so it was handled
        try:
            SBalance = eval(Entry1.get())
            SalExp = eval(Entry2.get())
            sales = eval(Entry3.get())
            utilities = eval(Entry4.get())
            purchases = eval(Entry5.get())
            rent = eval(Entry6.get())
            InvExp = eval(Entry7.get())
            OtherExp = eval(Entry8.get())
        except:
            tk.messagebox.showerror("Error","FIll all the fields")

        else:
            Text1.insert(END, "Rs. {}".format(SBalance))
            Text2.insert(END, "Rs. {}".format(purchases))
            Text3.insert(END, "Rs. {}".format(sales))
            Text4.insert(END, "Rs. {}".format((sales) - (purchases + SalExp + utilities + rent + InvExp + OtherExp)))
            Text5.insert(END, "Rs. {}".format(rent + utilities))
            Text6.insert(END, "Rs. {}".format(SalExp + InvExp + OtherExp))

    def reset(self):
        Text1.delete("1.0", "end")
        Text2.delete("1.0", "end")
        Text4.delete("1.0", "end")
        Text3.delete("1.0", "end")
        Text5.delete("1.0", "end")
        Text6.delete("1.0", "end")


FEATURES = features()

#----------LOGIN AND REGISTER OF ADMINS---------------#

class Users:

    def loginAdmin(self):

        uname = Entry1.get()
        pwd = Entry2.get()
        global User, pwindex
        for i in range(3000):
            infile = open("UserID.txt", 'r+')
            content = infile.read()
            listofidpw = content.split()


            if uname not in listofidpw:

                tk.messagebox.showinfo("Error", "This username does not exist.")
                break
            else:
                pwindex = listofidpw.index(uname) + 1

            if listofidpw[pwindex] == pwd:
                User = uname
                tk.messagebox.showinfo("Login", "Logged In Successfully")
                main.destroy()
                gui.CashFlow()

                break
            else:
                tk.messagebox.showinfo("Error", "Access denied, Invalid Password/Username")
                break

    def createAdmin(self):
        UserName = Username.get()
        password = Password.get()
        name = Name.get()
        phone = Phone.get()

        infile = open("UserID.txt", 'r+')
        content = infile.read()
        listofidpw = content.split()
        if UserName in listofidpw:
            tk.messagebox.showerror("Error", "User Already Exist")
        elif (UserName == "") or (password == "") or (name == "") or (phone == ""):
            tk.messagebox.showerror("Error", "Please fill all the fields")

        else:
            #An error was occuring whenever any field was left empty or phone number was invalid so it was handled.
            try:
                int(phone)==phone
            except:
                tk.messagebox.showerror("Error", "Invalid phone number")
            else:
                infile = open('UserID.txt', 'r+')
                content = infile.read()
                infile.write(" {0} {1}".format(UserName, password))
                tk.messagebox.showinfo("Success", "Customer Registered Successfully")
                infile.close()
                infile1 = open('Admin.txt', 'r+')
                infile1.write("{0} {1} ".format(name, phone))
                infile1.close()

USER = Users()

#----------GUI----------------------------#

class GUI:
    def CashFlow(self):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'

        font10 = "-family {Segoe UI} -size 24 -weight bold"
        font11 = "-family {Segoe UI} -size 17 -weight bold"
        font12 = "-family {Segoe UI} -size 19 -weight bold"
        font14 = "-family {Segoe UI} -size 10 -weight bold"
        font15 = "-family {Segoe UI} -size 11 -weight bold"

        global Entry1, Text1, Entry2, Entry3, Entry4, Entry5, Entry6, Entry7, Entry8, Text2, Text3, Text4, Text5, Text6, main

        main = Tk()
        main.geometry("1003x696+300+74")

        main.resizable(0, 0)
        main.title("Main Page")
        main.configure(background="#ff0000")

        Frame1 = tk.Frame(main)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.184, relwidth=1.003)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#d9d9d9")

        Label1 = tk.Label(main)
        Label1.place(relx=0.01, rely=0.201, height=71, width=984)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font10)
        Label1.configure(foreground="#000000")
        Label1.configure(relief="raised")
        Label1.configure(text='''CASH FLOW SYSTEM''')

        menubar = tk.Menu(main, font="TkMenuFont", bg='#ff0000', fg=_fgcolor)
        main.configure(menu=menubar)

        Frame2 = tk.Frame(main)
        Frame2.place(relx=0.01, rely=0.316, relheight=0.668, relwidth=0.982)

        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")

        Text1 = tk.Text(Frame2)
        Text1.place(relx=0.02, rely=0.043, relheight=0.138, relwidth=0.14)
        Text1.configure(background="white")
        Text1.configure(font=('TkTextFont', 20, 'bold'))
        Text1.configure(foreground="black")

        Text2 = tk.Text(Frame2)
        Text2.place(relx=0.183, rely=0.043, relheight=0.138, relwidth=0.136)
        Text2.configure(background="white")
        Text2.configure(font=('TkTextFont', 20, 'bold'))
        Text2.configure(foreground="black")
        Text2.configure(wrap="word")

        Text3 = tk.Text(Frame2)
        Text3.place(relx=0.345, rely=0.043, relheight=0.138, relwidth=0.134)
        Text3.configure(background="white")
        Text3.configure(font=('TkTextFont', 20, 'bold'))
        Text3.configure(foreground="black")
        Text3.configure(wrap="word")

        Text4 = tk.Text(Frame2)
        Text4.place(relx=0.822, rely=0.043, relheight=0.138, relwidth=0.156)
        Text4.configure(background="white")
        Text4.configure(font=('TkTextFont', 20, 'bold'))
        Text4.configure(foreground="black")
        Text4.configure(wrap="word")

        Text5 = tk.Text(Frame2)
        Text5.place(relx=0.508, rely=0.043, relheight=0.138, relwidth=0.137)
        Text5.configure(background="white")
        Text5.configure(font=('TkTextFont', 20, 'bold'))
        Text5.configure(foreground="black")
        Text5.configure(wrap="word")

        Text6 = tk.Text(Frame2)
        Text6.place(relx=0.66, rely=0.043, relheight=0.138, relwidth=0.136)
        Text6.configure(background="white")
        Text6.configure(font=('TkTextFont', 20, 'bold'))
        Text6.configure(foreground="black")
        Text6.configure(wrap="word")

        Label2 = tk.Label(Frame2)
        Label2.place(relx=0.02, rely=0.194, height=31, width=134)
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=font15)
        Label2.configure(foreground="#000000")
        Label2.configure(relief="raised")
        Label2.configure(text='''Starting Balance''')

        Label3 = tk.Label(Frame2)
        Label3.place(relx=0.183, rely=0.194, height=31, width=134)
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=font15)
        Label3.configure(foreground="#000000")
        Label3.configure(relief="raised")
        Label3.configure(text='''Purchases''')

        Label4 = tk.Label(Frame2)
        Label4.place(relx=0.345, rely=0.194, height=31, width=133)
        Label4.configure(background="#d9d9d9")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(font=font15)
        Label4.configure(foreground="#000000")
        Label4.configure(relief="raised")
        Label4.configure(text='''Sales''')

        Label5 = tk.Label(Frame2)
        Label5.place(relx=0.508, rely=0.194, height=31, width=134)
        Label5.configure(background="#d9d9d9")
        Label5.configure(disabledforeground="#a3a3a3")
        Label5.configure(font=font15)
        Label5.configure(foreground="#000000")
        Label5.configure(relief="raised")
        Label5.configure(text='''Rent/Utilities''')

        Label6 = tk.Label(Frame2)
        Label6.place(relx=0.822, rely=0.194, height=31, width=154)
        Label6.configure(background="#d9d9d9")
        Label6.configure(disabledforeground="#a3a3a3")
        Label6.configure(font=font15)
        Label6.configure(foreground="#000000")
        Label6.configure(relief="raised")
        Label6.configure(text='''Profit''')

        Label7 = tk.Label(Frame2)
        Label7.place(relx=0.66, rely=0.194, height=31, width=137)
        Label7.configure(background="#d9d9d9")
        Label7.configure(disabledforeground="#a3a3a3")
        Label7.configure(font=font15)
        Label7.configure(foreground="#000000")
        Label7.configure(relief="raised")
        Label7.configure(text='''Other Expenses''')

        Entry1 = tk.Entry(Frame2)
        Entry1.place(relx=0.061, rely=0.473, height=30, relwidth=0.187)
        Entry1.configure(background="white")
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")

        Entry2 = tk.Entry(Frame2)
        Entry2.place(relx=0.061, rely=0.667, height=30, relwidth=0.187)
        Entry2.configure(background="white")
        Entry2.configure(font="TkFixedFont")
        Entry2.configure(foreground="#000000")

        Entry3 = tk.Entry(Frame2)
        Entry3.place(relx=0.284, rely=0.473, height=30, relwidth=0.187)
        Entry3.configure(background="white")
        Entry3.configure(font="TkFixedFont")
        Entry3.configure(foreground="#000000")

        Entry4 = tk.Entry(Frame2)
        Entry4.place(relx=0.284, rely=0.667, height=30, relwidth=0.187)
        Entry4.configure(background="white")
        Entry4.configure(font="TkFixedFont")
        Entry4.configure(foreground="#000000")

        Entry5 = tk.Entry(Frame2)
        Entry5.place(relx=0.508, rely=0.473, height=30, relwidth=0.187)
        Entry5.configure(background="white")
        Entry5.configure(font="TkFixedFont")
        Entry5.configure(foreground="#000000")

        Label8 = tk.Label(Frame2)
        Label8.place(relx=0.091, rely=0.538, height=21, width=116)
        Label8.configure(background="#d9d9d9")
        Label8.configure(disabledforeground="#a3a3a3")
        Label8.configure(font=font14)
        Label8.configure(foreground="#000000")
        Label8.configure(text='''Starting Balance''')

        Entry6 = tk.Entry(Frame2)
        Entry6.place(relx=0.508, rely=0.667, height=30, relwidth=0.187)
        Entry6.configure(background="white")
        Entry6.configure(font="TkFixedFont")
        Entry6.configure(foreground="#000000")

        Label9 = tk.Label(Frame2)
        Label9.place(relx=0.091, rely=0.731, height=21, width=125)
        Label9.configure(background="#d9d9d9")
        Label9.configure(disabledforeground="#a3a3a3")
        Label9.configure(font=font14)
        Label9.configure(foreground="#000000")
        Label9.configure(text='''Salaries Expense''')

        Label10 = tk.Label(Frame2)
        Label10.place(relx=0.325, rely=0.731, height=21, width=109)
        Label10.configure(background="#d9d9d9")
        Label10.configure(disabledforeground="#a3a3a3")
        Label10.configure(font=font14)
        Label10.configure(foreground="#000000")
        Label10.configure(text='''Utilities''')

        Label11 = tk.Label(Frame2)
        Label11.place(relx=0.548, rely=0.731, height=21, width=105)
        Label11.configure(background="#d9d9d9")
        Label11.configure(disabledforeground="#a3a3a3")
        Label11.configure(font=font14)
        Label11.configure(foreground="#000000")
        Label11.configure(text='''Rent''')

        Label12 = tk.Label(Frame2)
        Label12.place(relx=0.325, rely=0.538, height=21, width=109)
        Label12.configure(background="#d9d9d9")
        Label12.configure(disabledforeground="#a3a3a3")
        Label12.configure(font=font14)
        Label12.configure(foreground="#000000")
        Label12.configure(text='''Sales''')

        Label13 = tk.Label(Frame2)
        Label13.place(relx=0.548, rely=0.538, height=21, width=108)
        Label13.configure(background="#d9d9d9")
        Label13.configure(disabledforeground="#a3a3a3")
        Label13.configure(font=font14)
        Label13.configure(foreground="#000000")
        Label13.configure(text='''Purchases''')

        Entry7 = tk.Entry(Frame2)
        Entry7.place(relx=0.731, rely=0.667, height=30, relwidth=0.187)
        Entry7.configure(background="white")
        Entry7.configure(font="TkFixedFont")
        Entry7.configure(foreground="#000000")

        Entry8 = tk.Entry(Frame2)
        Entry8.place(relx=0.731, rely=0.473, height=30, relwidth=0.187)
        Entry8.configure(background="white")
        Entry8.configure(font="TkFixedFont")
        Entry8.configure(foreground="#000000")

        Label14 = tk.Label(Frame2)
        Label14.place(relx=0.772, rely=0.538, height=21, width=111)
        Label14.configure(background="#d9d9d9")
        Label14.configure(disabledforeground="#a3a3a3")
        Label14.configure(font=font14)
        Label14.configure(foreground="#000000")
        Label14.configure(text='''Other Expenses''')

        Label15 = tk.Label(Frame2)
        Label15.place(relx=0.761, rely=0.731, height=21, width=130)
        Label15.configure(background="#d9d9d9")
        Label15.configure(disabledforeground="#a3a3a3")
        Label15.configure(font=font14)
        Label15.configure(foreground="#000000")
        Label15.configure(text='''Inventory Expense''')

        ResBtn = tk.Button(Frame2, command=FEATURES.reset)
        ResBtn.place(relx=0.152, rely=0.86, height=44, width=167)
        ResBtn.configure(background="#ff0000")
        ResBtn.configure(font=font11)
        ResBtn.configure(foreground="#ffffff")
        ResBtn.configure(pady="0")
        ResBtn.configure(text='''Reset''')

        CalBtn = tk.Button(Frame2, command=FEATURES.calculate)
        CalBtn.place(relx=0.345, rely=0.839, height=54, width=317)
        CalBtn.configure(background="#ff0000")
        CalBtn.configure(font=font12)
        CalBtn.configure(foreground="#ffffff")
        CalBtn.configure(pady="0")
        CalBtn.configure(relief="groove")
        CalBtn.configure(text='''Calculate''')

        logoutBtn = tk.Button(Frame2, command=FEATURES.logout)
        logoutBtn.place(relx=0.68, rely=0.86, height=44, width=167)
        logoutBtn.configure(background="#ff0000")
        logoutBtn.configure(font=font11)
        logoutBtn.configure(foreground="#ffffff")
        logoutBtn.configure(pady="0")
        logoutBtn.configure(relief="groove")
        logoutBtn.configure(text='''Sign Out''')

        icon = PhotoImage(file="chaseup.png")
        logo = Label(Frame1, image=icon)
        logo.pack()

        TSeparator1 = ttk.Separator(Frame2)
        TSeparator1.place(relx=0.008, rely=0.372, relwidth=0.986)

        main.mainloop()

    def login(self):
        font11 = "-family {Segoe UI} -size 19 -weight bold"
        font12 = "-family {Segoe UI} -size 16 -weight bold"
        font13 = "-family {Segoe UI} -size 11 -weight bold"
        font15 = "-family {Segoe UI} -size 12 -weight bold"

        global Username, Password, Name, Phone, Entry1, Entry2, main

        main = Tk()

        main.geometry("851x582+324+150")
        main.resizable(0, 0)
        main.title("Login Page")
        main.configure(background="#ff0000")
        main.configure(highlightbackground="#ff0000")
        main.configure(highlightcolor="#c20505")

        Frame1 = tk.Frame(main)
        Frame1.place(relx=0.0, rely=0.361, relheight=0.644, relwidth=0.498)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#d9d9d9")

        Entry1 = tk.Entry(Frame1)
        Entry1.place(relx=0.377, rely=0.347, height=30, relwidth=0.434)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")

        Entry2 = tk.Entry(Frame1)
        Entry2.place(relx=0.377, rely=0.48, height=30, relwidth=0.434)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="TkFixedFont")
        Entry2.configure(foreground="#000000")
        Entry2.configure(show="*")

        Label1 = tk.Label(Frame1)
        Label1.place(relx=0.118, rely=0.347, height=31, width=104)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font15)
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Username''')

        Label2 = tk.Label(Frame1)
        Label2.place(relx=0.118, rely=0.48, height=31, width=106)
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=font15)
        Label2.configure(foreground="#000000")
        Label2.configure(text='''Password''')

        Button1 = tk.Button(Frame1, command=USER.loginAdmin)
        Button1.place(relx=0.401, rely=0.587, height=34, width=157)
        Button1.configure(background="#f5010a")
        Button1.configure(font=font13)
        Button1.configure(foreground="#ffffff")
        Button1.configure(pady="0")
        Button1.configure(text='''LOGIN''')

        Label8 = tk.Label(Frame1)
        Label8.place(relx=0.118, rely=0.053, height=51, width=334)
        Label8.configure(background="#d9d9d9")
        Label8.configure(disabledforeground="#a3a3a3")
        Label8.configure(font=font12)
        Label8.configure(foreground="#000000")
        Label8.configure(text='''RETURNING ADMIN''')

        Frame2 = tk.Frame(main)
        Frame2.place(relx=0.505, rely=0.361, relheight=0.644
                     , relwidth=0.498)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")

        Name = tk.Entry(Frame2)
        Name.place(relx=0.401, rely=0.24, height=30, relwidth=0.41)
        Name.configure(background="white")
        Name.configure(font="TkFixedFont")
        Name.configure(foreground="#000000")

        Phone = tk.Entry(Frame2)
        Phone.place(relx=0.401, rely=0.347, height=30, relwidth=0.41)
        Phone.configure(background="white")
        Phone.configure(font="TkFixedFont")
        Phone.configure(foreground="#000000")

        Username = tk.Entry(Frame2)
        Username.place(relx=0.401, rely=0.453, height=30, relwidth=0.41)
        Username.configure(background="white")
        Username.configure(font="TkFixedFont")
        Username.configure(foreground="#000000")

        Password = tk.Entry(Frame2)
        Password.place(relx=0.401, rely=0.56, height=30, relwidth=0.41)
        Password.configure(background="white")
        Password.configure(font="TkFixedFont")
        Password.configure(foreground="#000000")

        Label3 = tk.Label(Frame2)
        Label3.place(relx=0.165, rely=0.24, height=31, width=94)
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=font15)
        Label3.configure(foreground="#000000")
        Label3.configure(text='''Name''')

        Label4 = tk.Label(Frame2)
        Label4.place(relx=0.165, rely=0.453, height=31, width=94)
        Label4.configure(background="#d9d9d9")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(font=font15)
        Label4.configure(foreground="#000000")
        Label4.configure(text='''Username''')

        Label5 = tk.Label(Frame2)
        Label5.place(relx=0.165, rely=0.56, height=31, width=94)
        Label5.configure(background="#d9d9d9")
        Label5.configure(disabledforeground="#a3a3a3")
        Label5.configure(font=font15)
        Label5.configure(foreground="#000000")
        Label5.configure(text='''Password''')

        Label6 = tk.Label(Frame2)
        Label6.place(relx=0.094, rely=0.347, height=31, width=127)
        Label6.configure(background="#d9d9d9")
        Label6.configure(disabledforeground="#a3a3a3")
        Label6.configure(font=font15)
        Label6.configure(foreground="#000000")
        Label6.configure(text='''Phone Number''')

        Button2 = tk.Button(Frame2, command=USER.createAdmin)
        Button2.place(relx=0.401, rely=0.667, height=34, width=177)
        Button2.configure(background="#f5010a")
        Button2.configure(font=font13)
        Button2.configure(foreground="#ffffff")
        Button2.configure(overrelief="raised")
        Button2.configure(pady="0")
        Button2.configure(text='''REGISTER''')

        Label9 = tk.Label(Frame2)
        Label9.place(relx=0.142, rely=0.053, height=51, width=334)
        Label9.configure(background="#d9d9d9")
        Label9.configure(disabledforeground="#a3a3a3")
        Label9.configure(font=font12)
        Label9.configure(foreground="#000000")
        Label9.configure(text='''NEW ADMIN''')

        Frame3 = tk.Frame(main)
        Frame3.place(relx=0.0, rely=0.0, relheight=0.284, relwidth=1.016)
        Frame3.configure(relief='groove')
        Frame3.configure(borderwidth="2")
        Frame3.configure(relief="groove")
        Frame3.configure(background="#d9d9d9")

        icon = PhotoImage(file="chaseup.png")
        logo = Label(Frame3, image=icon)
        logo.pack()

        Label7 = tk.Label(main)
        Label7.place(relx=0.059, rely=0.292, height=31, width=764)
        Label7.configure(background="#d9d9d9")
        Label7.configure(disabledforeground="#a3a3a3")
        Label7.configure(font=font11)
        Label7.configure(foreground="#000000")
        Label7.configure(text='''WELCOME TO CHASE UP!  Please Login.''')
        main.mainloop()


gui = GUI()
gui.login()
