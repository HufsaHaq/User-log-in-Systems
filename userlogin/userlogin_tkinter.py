from userlogin_sqlite import *

import sqlite3
import os

from tkinter import *
from tkinter import messagebox

class AdminWindow(Frame):

    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #with that, we want to then run init_window, which doesn't yet exist
        self.show_admin_login()

    #code to ensure users can tab between fields on the GUI
    def focus_next_window(self,event):
        event.widget.tk_focusNext().focus()
        return("break")

    # clear the window of all widgets
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    # exit the python program
    def client_exit(self):
        exit()


    def show_admin_login(self):

        # clear the widow of any previous widgets
        self.clear_window()
        
        # row 1
        self.label = Label(self,text="Admin Login...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row a - one line of text
        
        self.usernameLabel = Label(self, text="Username", font=("Arial Narrow",16))
        self.usernameLabel.grid(row=2, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
        self.usernameTextBox = Entry(self,width=50)
        self.usernameTextBox.grid(row=2, column = 2, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky="w")
        self.usernameTextBox.bind("<Tab>", self.focus_next_window)
        self.usernameTextBox.focus()

        # work around for foriegn characaters
        '''
        self.usernameTextBox.bind("<Control-n>", lambda event: self.usernameTextBox.insert(999,"ñ"))
        self.usernameTextBox.bind("<Control-Shift-N>", lambda event: self.usernameTextBox.insert(999,"Ñ"))
        self.usernameTextBox.bind("<Control-u>", lambda event: self.usernameTextBox.insert(999,"ü"))
        self.usernameTextBox.bind("<Control-Shift-U>", lambda event: self.usernameTextBox.insert(999,"Ü"))
        '''        

        # row3
        self.password1Label = Label(self, text="Password", font=("Arial Narrow",16))
        self.password1Label.grid(row=3, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)       
        self.password1TextBox = Entry(self,show="*",width=50)
        self.password1TextBox.grid(row=3, column = 2, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky="w")
        self.password1TextBox.bind("<Tab>", self.focus_next_window)
        self.password1TextBox.focus()
       
        # row4
        self.loginButton = Button(self,text='Login',command=self.loginadmin,width=20)
        self.loginButton.grid(row=4, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)

        # row 5
        self.welcome = PhotoImage(file = "logo.png")
        self.welcomeimage =Label(self, image=self.welcome).grid(row = 5, column = 1, columnspan=4)

        
    def loginadmin(self):
        
        myname = self.usernameTextBox.get()
        mypassword = self.password1TextBox.get()

        #this uses code from userlogin_sqlite
        results = userlogin(myname, mypassword)

        if results[0] == "Error":
            if results[1] == "Username not found":
                messagebox.showerror("Error", "Username not found")
                self.show_admin_login()
            else:
                messagebox.showerror("Error", "Password incorrect")
                self.show_admin_login()
        else:
            messagebox.showinfo("Information","Logged in " + myname)
            self.show_menu()


    def show_menu(self):
           
        # clear the widow of any previous widgets
        self.clear_window()

        # row 1
        self.label = Label(self,text="Menu...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row 2
        self.showusersButton = Button(self,text='Show users',command=self.show_myshowusers,width=20)
        self.showusersButton.grid(row=2, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)

        # row 3
        self.adduserButton = Button(self,text='Add user',command=self.show_myadduser,width=20)
        self.adduserButton.grid(row=3, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
        self.updateuserButton = Button(self,text='Update user',command=self.show_myupdateuser,width=24)
        self.updateuserButton.grid(row=3, column = 2, columnspan = 1, rowspan = 1, padx=10, pady=10)
        self.deleteuserButton = Button(self,text='Delete user',command=self.show_mydeleteuser,width=20)
        self.deleteuserButton.grid(row=3, column = 3, columnspan = 1, rowspan = 1, padx=10, pady=10)
    
        # buttons at bottom of window
        self.logoutButton = Button(self,text='Log out',command=self.show_admin_login,width=20)
        self.logoutButton.grid(row=20, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)             

    def show_myshowusers(self):
           
        # clear the widow of any previous widgets
        self.clear_window()

        # row 1
        self.label = Label(self,text="Show all users...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row 2
        # create a Text widget
        self.mytextwidget = Text(self, borderwidth=3, relief="sunken", width=30, height=10)
        self.mytextwidget.config(font=("consolas", 12), undo=True, wrap='word', tabs=("4c"))
        self.mytextwidget.grid(row=2, column=1, columnspan = 3, rowspan = 1, sticky="nsew", padx=2, pady=2)
        self.mytextwidget.bind("<Tab>", self.focus_next_window)
        self.mytextwidget.focus()

        
        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(self, command=self.mytextwidget.yview)
        scrollb.grid(row=2, column=4, sticky='nsew')
        self.mytextwidget['yscrollcommand'] = scrollb.set
        mytext = "\nUsername\tPassword\n"
        
        # fetch the data
        results = showmeall()
        for i in range (len(results)):
            mytext = mytext + str(results[i][1]) +"\t"+ str(results[i][2]) +"\n"
        self.mytextwidget.insert(END,mytext)

        # row 3
        self.backButton = Button(self,text='Back to menu',command=self.show_menu,width=20)
        self.backButton.grid(row=3, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
    
        # buttons at bottom of window
        self.logoutButton = Button(self,text='Log out',command=self.show_admin_login,width=20)
        self.logoutButton.grid(row=20, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)             

    def show_myadduser(self):
           
        # clear the widow of any previous widgets
        self.clear_window()

        # row 1
        self.label = Label(self,text="Add user...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row 2 - username

        self.usernameLabel = Label(self, text="Username", font=("Arial Narrow", 16))
        self.usernameLabel.grid(row=2, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.usernameTextBox = Entry(self, width=50)
        self.usernameTextBox.grid(row=2, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.usernameTextBox.bind("<Tab>", self.focus_next_window)
        self.usernameTextBox.focus()

        # row 3 - password 1
        self.password1Label = Label(self, text="Password", font=("Arial Narrow", 16))
        self.password1Label.grid(row=3, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.password1TextBox = Entry(self, show="*", width=50)
        self.password1TextBox.grid(row=3, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.password1TextBox.bind("<Tab>", self.focus_next_window)
        self.password1TextBox.focus()

        # row 4 - password re-enter
        self.password2Label = Label(self, text="Password re-enter", font=("Arial Narrow", 16))
        self.password2Label.grid(row=4, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.password2TextBox = Entry(self, show="*", width=50)
        self.password2TextBox.grid(row=4, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.password2TextBox.bind("<Tab>", self.focus_next_window)
        self.password2TextBox.focus()

        # row 5
        self.loginButton = Button(self, text='Add user', command=self.myadduser, width=20)
        self.loginButton.grid(row=5, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        # row 6
        self.backButton = Button(self,text='Back to menu',command=self.show_menu,width=20)
        self.backButton.grid(row=7, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
    
        # buttons at bottom of window
        self.logoutButton = Button(self,text='Log out',command=self.show_admin_login,width=20)
        self.logoutButton.grid(row=20, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)             

    def myadduser(self):

        myname = self.usernameTextBox.get()
        mypassword1 = self.password1TextBox.get()
        mypassword2 = self.password2TextBox.get()

        # this uses code from userlogin_sqlite
        results = adduser(myname, mypassword1, mypassword2)

        if results[0] == "Error":
            messagebox.showerror("Error", results[1])
            self.show_myadduser()
        else:
            messagebox.showinfo("Information", results[0] +" "+ results[1])
            self.show_menu()

    def show_myupdateuser(self):
           
        # clear the widow of any previous widgets
        self.clear_window()

        # row 1
        self.label = Label(self,text="Update user...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row 2 - username

        self.usernameLabel = Label(self, text="Username", font=("Arial Narrow", 16))
        self.usernameLabel.grid(row=2, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.usernameTextBox = Entry(self, width=50)
        self.usernameTextBox.grid(row=2, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.usernameTextBox.bind("<Tab>", self.focus_next_window)
        self.usernameTextBox.focus()

        # row 3 - password 1
        self.password1Label = Label(self, text="Password", font=("Arial Narrow", 16))
        self.password1Label.grid(row=3, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.password1TextBox = Entry(self, show="*", width=50)
        self.password1TextBox.grid(row=3, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.password1TextBox.bind("<Tab>", self.focus_next_window)
        self.password1TextBox.focus()

        # row 4 - password re-enter
        self.password2Label = Label(self, text="Password re-enter", font=("Arial Narrow", 16))
        self.password2Label.grid(row=4, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.password2TextBox = Entry(self, show="*", width=50)
        self.password2TextBox.grid(row=4, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.password2TextBox.bind("<Tab>", self.focus_next_window)
        self.password2TextBox.focus()

        # row 5
        self.loginButton = Button(self, text='Update password', command=self.myupdateuser, width=20)
        self.loginButton.grid(row=5, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        # row 6
        self.backButton = Button(self,text='Back to menu',command=self.show_menu,width=20)
        self.backButton.grid(row=6, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
    
        # buttons at bottom of window
        self.logoutButton = Button(self,text='Log out',command=self.show_admin_login,width=20)
        self.logoutButton.grid(row=20, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)             

    def myupdateuser(self):

        myname = self.usernameTextBox.get()
        mypassword1 = self.password1TextBox.get()
        mypassword2 = self.password2TextBox.get()

        # this uses code from userlogin_sqlite
        results = adminupdateuser(myname, mypassword1, mypassword2)

        if results[0] == "Error":
            messagebox.showerror("Error", results[1])
            self.show_myupdateuser()
        else:
            messagebox.showinfo("Information", results[0] +" "+ results[1])
            self.show_menu()

        self.show_menu()     

    def show_mydeleteuser(self):
           
        # clear the widow of any previous widgets
        self.clear_window()

        # row 1
        self.label = Label(self,text="Delete...", font=("Arial Narrow",24))
        self.label.grid(row=1, column = 1, columnspan = 4, rowspan = 1, padx=10, pady=10, sticky=W)

        # row 2 - username

        self.usernameLabel = Label(self, text="Username", font=("Arial Narrow", 16))
        self.usernameLabel.grid(row=2, column=1, columnspan=1, rowspan=1, padx=10, pady=10)
        self.usernameTextBox = Entry(self, width=50)
        self.usernameTextBox.grid(row=2, column=2, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        self.usernameTextBox.bind("<Tab>", self.focus_next_window)
        self.usernameTextBox.focus()

        # row 3
        self.loginButton = Button(self, text='Delete user', command=self.mydeleteuser, width=20)
        self.loginButton.grid(row=3, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        # row 5
        self.backButton = Button(self,text='Back to menu',command=self.show_menu,width=20)
        self.backButton.grid(row=4, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)
   
        # buttons at bottom of window
        self.logoutButton = Button(self,text='Log out',command=self.show_admin_login,width=20)
        self.logoutButton.grid(row=20, column = 1, columnspan = 1, rowspan = 1, padx=10, pady=10)             

    def mydeleteuser(self):

        myname = self.usernameTextBox.get()

        # this uses code from userlogin_sqlite
        results = deleteuser(myname,)

        if results[0] == "Error":
            messagebox.showerror("Error", results[1])
            self.show_myadduser()
        else:
            messagebox.showinfo("Information", results[0] + " " + results[1])
            self.show_menu()

        self.show_menu()
        
###############################################
###############################################
# MAIN PROGRAM
if __name__ == "__main__":

    # root window created. Here, that would be the only window, but you can later have windows within windows.
    root = Tk()
    root.geometry("1000x800")

    # invoke the button on the return key
    root.bind_class("Button", "<Key-Return>", lambda event: event.widget.invoke())

    # remove the default behavior of invoking the button with the space key
    root.unbind_class("Button", "<Key-space>")

    # start fullscreen ???
    '''
    root.attributes("-fullscreen", True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    '''

    #creation of an instance
    app = AdminWindow(root)

    #mainloop 
    root.mainloop() 

    
        

    
    
