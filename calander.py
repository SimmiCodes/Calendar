from tkinter import*
import calendar

def showcall():
    gui=Tk()
    gui.config(background="#dfe6e9")
    gui.title("Calender")
    gui.geometry("550x600")

    f_year=int(year_field.get())
    content=calendar.calendar(f_year)
    c_year=Label(gui,text=content,font="consolas 10 bold")
    c_year.grid(row=5,column=1,padx=20)
    gui.mainloop()

if __name__ == "__main__" :
    gui=Tk()
    gui.config(background="#ffeaa7")
    gui.title("Calender")
    gui.geometry("300x250")
    cal=Label(gui,text="Calender",bg="#ffeaa7",font=("Elephant",27,"bold"))
    year=Label(gui,text="Enter Year",bg="#fdcb6e",font=("times",12,"bold"))
    year_field=Entry(gui)
    Show=Button(gui,text="Show Calender",fg="black",bg="#fdcb6e",command=showcall)
    Exit=Button(gui,text="Exit",fg='black',bg="#fdcb6e",command=exit)
    cal.grid(row=1,column=1,padx=50)
    year.grid(row=2,column=1,pady=20)
    year_field.grid(row=3,column=1,pady=5)
    Show.grid(row=4,column=1,pady=10)
    Exit.grid(row=5,column=1,pady=20)
    gui.mainloop()




