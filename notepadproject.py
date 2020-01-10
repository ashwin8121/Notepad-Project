"""just a simple program to do something with tkinter"""


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as ts
import tkinter.filedialog as tf
import tkinter.colorchooser as tc
import tkfontchooser as fc
import tkinter.messagebox as tm
import webbrowser as wb
import os

abttxt="""
This is a project done by ASHWIN.
this is same as a notepad but programmed by me.
"""

crnt_dir=os.getcwd()

def newfile(): #for new file
    import notepadproject

def openfile():#for opening file
    file=tf.askopenfilenames(filetypes=(("text files","*.txt"),("all files","*.*")), initialdir=os.getcwd())
    print(file[0])
    try:
        with open(file[0], 'r') as _file_:
            _txt=_file_.read()
            tp.insert(0.0, _txt)
            
    except:
        tm.showinfo(title="Error", messgae="Could not open file")


def savefile():# for saving
    file_dir_1=tf.asksaveasfilename(initialdir=os.getcwd())
    lst=file_dir_1.split('/')
    file_name=lst[-1]
    lst.pop()
    dir_='/'.join(lst)
    try:
        os.chdir(dir_)
        text=e.get(0.0, END)
        open(file_name, 'x')
        with open(file_name, 'w') as file:
            file.write(text)
            file.close()
        os.chdir(crnt_dir)
    except:
        tm.showinfo(message="Couldn't save file again")


def saveasfile():#for saving another time
    try:
        savefile()
    except:
        tm.showinfo(message="Couldn't save file again")

def ext():#closing file
    root.destroy()	

def reset(): # reseting all values
    tp.config(bg="white",fg="black",font="@ArialUnicodeMS ",width=157, height=42)

def font():
    f=fc.askfont()
    fnt=f["family"]
    fnt1=fnt.replace(" ","")
    siz=f["size"]
    font1=str(fnt1)+" "+str(siz)

    if f["underline"]==1:
        font1=font1+" underline"
    if f["overstrike"]==1:
        font1=font1+" overstrike"
    if f["weight"]=="bold":
        font1=font1+" bold"
    if f["slant"]=="italic":
        font1=font1+" italic"
    
    tp.configure(font=font1)
    
def fgcolor():
    clr=tc.askcolor()
    color=clr[1]
    tp.config(fg=color)
	
	
def bgcolor():
    clr=tc.askcolor()
    color=clr[1]
    tp.config(bg=color)

def about():
    root1=tk.Tk()
    c=tk.Canvas(root1, width=100, height=100, bg="cyan")
    c.pack()
    #c.create_polygon(50,0, 100,100, 0,100, fill="lavender")
    c.create_text(50,50, text="A", font=("colonna MT", 80, "bold"))
    tk.Label(root1, text=abttxt).pack()
    root1.mainloop()
    
def hlp():
    pass

    
#frame creating
root=tk.Tk()
root.title('Notepad') #title
root.geometry('1280x720')  #size

#menubar creating
menubar=tk.Menu(root)

#filemenu
fm=tk.Menu(menubar, tearoff=0)
fm.add_command(label='New File', command=newfile)
fm.add_command(label='Open File', command=openfile)
fm.add_command(label='Save File', command=savefile)
fm.add_command(label='Save as', command=saveasfile)
fm.add_separator()
fm.add_command(label='Exit', command=ext)
menubar.add_cascade(label="File", menu=fm)
#editmenu
em=tk.Menu(menubar, tearoff=0)
em.add_command(label='Font style', command=font)
em.add_separator()
em.add_command(label='Font Color', command=fgcolor)
em.add_command(label='Background Color', command=bgcolor)
em.add_separator()
em.add_command(label="Reset", command=reset)
menubar.add_cascade(label='Edit', menu=em)

#about menu
am=tk.Menu(menubar, tearoff=0)
am.add_command(label="About", command=about)
am.add_command(label="Help", command=hlp)
menubar.add_cascade(label="About", menu=am)

#textpad creating
tp=ts.ScrolledText(root, width=157, height=42)
tp.grid(row=1, column=1) 

root.config(menu=menubar)
root.mainloop()
