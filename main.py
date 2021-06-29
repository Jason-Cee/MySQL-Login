from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import *

# ROOT WINDOW
root = Tk()
root.title("Login Window")
root.geometry("700x400")
root.config(bg="#9b2226")
root.resizable(False, False)

now = datetime.now()

login = Label(root, bg="#9b2226", text="LOGIN", fg="White", font=("bold", 20))
login.place(x=300, y=10)

# USERNAME
username = Label(root, bg="#9b2226", text="Username: ", fg="White", font=("Bold", 15))
username.place(x=10, y=100)
# USERNAME ENTRY
uname = Entry(root, bg="#4895ef", fg="White")
uname.place(x=150, y=100)

# PASSWORD
password = Label(root, bg="#9b2226", text="Password: ", fg="white", font=("Bold", 15))
password.place(x=375, y=100)
# PASSWORD ENTRY
pword = Entry(root, bg="#4895ef", fg="White", show="~")
pword.place(x=510, y=100)


def log():
    mydb = mysql.connector.connect(user="lifechoices",
                                   password="@Lifechoices1234",
                                   host="127.0.0.1", database="hospital",
                                   auth_plugin="mysql_native_password")
    mycursor = mydb.cursor()
    x1 = mycursor.execute("Select * from Login")
    for x in mycursor:
        print("List Of Registered", "\n" + str(x))

    with open("track.txt", "a+") as w:
        w.write("LOGGED IN " + "\n")
        w.write("Username: " + uname.get() + "\n")
        w.write("Password: " + pword.get() + "\n")
        w.write("Logged In At: " + str(now) + "\n")
        w.write("\n")
        w.close()


# BUTTON
logbtn = Button(root, bg="#4895ef", fg="#9b2226", text="LOG IN", command=log)
logbtn.place(x=220, y=150)


def reg():
    if uname == "" or pword == "":
        messagebox.showerror("INVALID", "PLEASE ENTER DETAILS")
    else:
        mydb = mysql.connector.connect(user="lifechoices",
                                       password="@Lifechoices1234",
                                       host="127.0.0.1", database="hospital",
                                       auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login  VALUES (%s, %s)"
        val = (uname.get(), pword.get())
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "Details Recorded.")
        mycursor.execute('Select * from Login')

        # APPENDING TEXT FILE
        with open("track.txt", "a+") as w:
            w.write("REGISTERED" + "\n")
            w.write("Username: " + uname.get() + "\n")
            w.write("Password: " + pword.get() + "\n")
            w.write("Registered at: " + str(now) + "\n")
            w.write("\n")
            w.close()


# REGISTER
regbtn = Button(root, bg="#4895ef", fg="#9b2226", text="REGISTER", command=reg)
regbtn.place(x=400, y=150)


# CLEAR BUTTON DEFINITION
def remove():
    msg = messagebox.askquestion("CLEAR", "Are You Sure You Want To Delete All ?")
    if msg == "yes":
        uname.delete(0, END)
        pword.delete(0, END)


# CLEAR
clearbtn = Button(root, bg="#4895ef", fg="#9b2226", text="CLEAR", command=remove)
clearbtn.place(x=50, y=350)


# EXIT FUNCTION DEFINITION
def outs():
    msg = messagebox.askquestion("ON YOUR WAY OUT", "Are You Sure You Want To Exit ?")
    if msg == "yes":
        root.destroy()


# EXIT
out = Button(root, bg="#4895ef", fg="#9b2226", text="E X I T", command=outs)
out.place(x=600, y=350)

# RUN CODE
root.mainloop()
