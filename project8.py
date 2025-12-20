from tkinter import*
import calendar

def showCal():
    window=Tk()
    window.configure(bg="light blue")
    window.title("Calendar")
    window.geometry("550x600")
    fetchyear=int(year_field.get())

    #calender method
    cal_content=calendar.calendar(fetchyear)

    cal_year=Label(window,text=cal_content,font=("Courier new",10))
    cal_year.grid(row=5,column=1,padx=20)

if __name__== "__main__":
    newwindow=Tk() 
    newwindow.title("Calender")
    newwindow.geometry("550x600")
    cal=Label(newwindow,text="CALENDAR",bg="dark grey",font=("roboto",25,"bold"))

    year=Label(newwindow,text="Enter Year",bg="yellow",font=("roboto",15,"bold"))
     #entry box
    year_field=Entry(newwindow)

    submit=Button(newwindow,text="Show Calendar",fg="light green",bg="red",command=showCal)
    exit=Button(newwindow,text="Exit",fg="light green",bg="red",command=newwindow.destroy)

    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    submit.grid(row=4,column=1)
    exit.grid(row=6,column=1)


    newwindow.mainloop()