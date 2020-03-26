import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
with sqlite3.connect('Music.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL,email TEXT NOT NULL);')
c.execute("""CREATE TABLE IF NOT EXISTS MusicLib(
		song TEXT NOT NULL,
		genre TEXT NOT NULL,
		singer TEXT NOT NULL
	)""")
db.commit()
db.close() 
	


def lib():
	top=Toplevel()
	top.geometry('600x300+250+200')
	top.title("MUSIC LIBRARY")
	top.configure(bg="BLACK")
	top.maxsize(1100,800)
	top.minsize(600,300)
	
	title_frame = Frame(top, height=25, bg="BLACK")
	title_frame.pack(side=TOP)
	title = Label(title_frame, text="ONLINE MUSIC LIBRARY", font=('Times New Roman',30,'bold'), bg="YELLOW", fg="GREEN")
	title.config(anchor=CENTER)
	title.pack(side=TOP,pady=10)

	with sqlite3.connect('Music.db') as db:
            c = db.cursor()

	c.execute("SELECT * from MusicLib")
	rows=c.fetchall()
	tree= ttk.Treeview(top, column=("column1", "column2", "column3"), show='headings')
	tree.heading("#1", text="Song")
	tree.heading("#2", text="Genre")
	tree.heading("#3", text="Singer")
	tree.pack()
	for row in rows:
		#Libcontect_label = Label(title_frame, text= row  ,font=('Times New Roman',15,'bold'), bg="YELLOW", fg="GREEN")
		#Libcontect_label.pack(padx=5,pady=5)
		tree.insert("", tk.END, values=row)
def add_Music():
	top=Toplevel()
	top.geometry('600x300+250+200')
	top.title("MUSIC LIBRARY")
	top.configure(bg="BLACK")
	top.maxsize(1100,800)
	top.minsize(600,300)
	
	title_frame = Frame(top, height=25, bg="BLACK")
	title_frame.pack(side=TOP)
	title = Label(title_frame, text="ADD MUSIC", font=('Times New Roman',30,'bold'), bg="YELLOW", fg="GREEN")
	title.config(anchor=CENTER)
	title.pack(side=TOP,pady=10)	
	
	
	song_frame = Frame(top, bg="BLACK")
	song_frame.pack(side=TOP,pady=20)
        
	song_lbl = Label(song_frame, text="Song",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	song_lbl.pack(side=LEFT)
        
	song_entry = Entry(song_frame,width=30,textvariable=song)
	song_entry.pack(side=LEFT,padx=30)
	
	genre_frame = Frame(top, bg="BLACK")
	genre_frame.pack(side=TOP,pady=20)
        
	genre_lbl = Label(song_frame, text="Genre",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	genre_lbl.pack(side=LEFT)
        
	genre_entry = Entry(song_frame,width=30,textvariable=genre)
	genre_entry.pack(side=LEFT,padx=30)
	
	singer_frame = Frame(top, bg="BLACK")
	singer_frame.pack(side=TOP,pady=5)
        
	singer_lbl = Label(singer_frame, text="Singer",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	singer_lbl.pack(side=LEFT)
        
	singer_entry = Entry(singer_frame,width=30,textvariable=singer)
	singer_entry.pack(side=LEFT,padx=30)
	
	add_frame = Frame(top, bg="BLACK")
	add_frame.pack(side=TOP,pady=20,padx=250)
    
	add1 = Button(add_frame, text='ADD', width=20, bg='GREEN', fg='BLACK',font="none 10 bold",command=add)
	add1.pack(side=RIGHT)	
	

def add():
	song1=song.get()
	genre1=genre.get()
	singer1=singer.get()
	with sqlite3.connect('MUSIC.db') as db:
        	c = db.cursor()
	find_user = 'SELECT * FROM MusicLib WHERE song = ?'
	c.execute(find_user,[(song1)])      
	if c.fetchall():
		messagebox.showerror('Error!','Username Taken Try a Diffrent One.')
	else:
		messagebox.showinfo('Success!','Account Created!')
		lib()

	c.execute('INSERT INTO MusicLib (song,genre,singer) VALUES(?,?,?)',(song1,genre1,singer1))
	db.commit()



def login():
	user=username.get()
	pswd=password.get()
	with sqlite3.connect('Music.db') as db:
		c = db.cursor()
	c.execute('SELECT * from user WHERE username="%s" AND password="%s"' % (user, pswd))
	if c.fetchone() is not None:
		add_Music()
	else:
		messagebox.showerror("Login failed")

def submit():
	#username_entry.delete(0,END)
	#password_entry.delete(0,END)
	username1=username.get()
	password1=password.get()
	email1=email.get()
	with sqlite3.connect('MUSIC.db') as db:
        	c = db.cursor()
	find_user = 'SELECT * FROM user WHERE username = ?'
	c.execute(find_user,[(username1)])      
	if c.fetchall():
		messagebox.showerror('Error!','Username Taken Try a Diffrent One.')
	else:
		messagebox.showinfo('Success!','Account Created!')
		add_Music()

        
	#insert = 'INSERT INTO user(username,password) VALUES(?,?)'
	#c.execute(insert,[(username.get()),(password.get())])
	c.execute('INSERT INTO user (username,password,email) VALUES(?,?,?)',(username1,password1,email1))
	db.commit()
	
def main():
	top=Toplevel()
	top.geometry('600x300+250+200')
	top.title("MUSIC LIBRARY")
	top.configure(bg="BLACK")
	top.maxsize(1100,800)
	top.minsize(600,300)
	title_frame = Frame(top, height=25, bg="BLACK")
	title_frame.pack(side=TOP)
        
	title = Label(title_frame, text="REGISTER", font=('Times New Roman',30,'bold'), bg="BLACK", fg="BLUE")
	title.config(anchor=CENTER)
	title.pack(fill=BOTH,pady=6)
	#username=StringVar()
	#email=StringVar()
	#password = StringVar()
	username_frame = Frame(top, bg="BLACK")
	username_frame.pack(side=TOP,pady=20)
        
	username_lbl = Label(username_frame, text="Username",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	username_lbl.pack(side=LEFT)
        
	username_entry = Entry(username_frame,width=30,textvar=username)
	username_entry.pack(side=LEFT,padx=30)
	
	email_frame = Frame(top, bg="BLACK")
	email_frame.pack(side=TOP,pady=20)
        
	email_lbl = Label(username_frame, text="Email",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	email_lbl.pack(side=LEFT)
        
	email_entry = Entry(username_frame,width=30,textvar=email)
	email_entry.pack(side=LEFT,padx=30)
	
	password_frame = Frame(top, bg="BLACK")
	password_frame.pack(side=TOP,pady=5)
        
	password_lbl = Label(password_frame, text="password",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
	password_lbl.pack(side=LEFT)
        
	password_entry = Entry(password_frame,width=30,show="*",textvar=password)
	password_entry.pack(side=LEFT,padx=30)
	
	submit_frame = Frame(top, bg="BLACK")
	submit_frame.pack(side=TOP,pady=20,padx=250)
    
	submit1 = Button(submit_frame, text='Submit', width=20, bg='GREEN', fg='BLACK',font="none 10 bold",command=submit)
	submit1.pack(side=RIGHT)	
	
	
######MAIN CODE ############
root=Tk()
root.geometry('600x300+250+200')
root.title("MUSIC LIBRARY")
root.configure(bg="BLACK")
root.maxsize(1100,800)
root.minsize(600,300)

username=StringVar()
email=StringVar()
password = StringVar()
song=StringVar()
genre=StringVar()
singer=StringVar()
title_frame = Frame(root, height=25, bg="BLACK")
title_frame.pack(side=TOP)
        
title = Label(title_frame, text="MUSIC", font=('Times New Roman',30,'bold'), bg="BLACK", fg="GREEN")
title.config(anchor=CENTER)
title.pack(fill=BOTH,pady=6)
		
username_frame = Frame(root, bg="BLACK")
username_frame.pack(side=TOP,pady=20)
        
username_lbl = Label(username_frame, text="Username : ",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
username_lbl.pack(side=LEFT)
        
username_entry = Entry(username_frame,width=30,textvar=username)
username_entry.pack(side=LEFT,padx=30)
        
		
password_frame = Frame(root, bg="BLACK")
password_frame.pack(side=TOP,pady=5)
        
password_lbl = Label(password_frame, text="Password : ",font=('Times New Roman',20,'bold'),bg="BLACK",fg="YELLOW")
password_lbl.pack(side=LEFT)
        
password_entry = Entry(password_frame,width=30,show="*",textvar=password)
password_entry.pack(side=LEFT,padx=30)

reg_frame = Frame(root, bg="BLACK")
reg_frame.pack(side=TOP,pady=0,padx=250)
		
reg = Button(reg_frame, text='REGISTER', width=20, bg='GREEN', fg='BLACK',font="none 10 bold",command=main)
reg.pack(side=LEFT)

 
done_frame = Frame(root, bg="BLACK")
done_frame.pack(side=TOP,pady=0,padx=250)
		
done = Button(done_frame, text='DONE', width=20, bg='GREEN', fg='BLACK',font="none 10 bold",command=login)
done.pack(side=LEFT)


    

#submit_frame = Frame(root, bg="BLACK")
#submit_frame.pack(side=TOP,pady=20,padx=250)
    
#submit = Button(submit_frame, text='Submit', width=20, bg='GREEN', fg='BLACK',font="none 10 bold", command=lib)
#submit.pack(side=RIGHT)	
'''tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.pack()
'''


root.mainloop()