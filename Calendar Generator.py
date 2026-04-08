from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

cal=Tk()
cal.geometry('600x400')
cal.title("Calender Generator")
cal.config(background='#c6e2ff')
cal.resizable(False,False)

#----------heading---------------
label1= Label(cal, text='CALENDAR GENERATOR', anchor='center',font=('times new roman',36,'bold'), fg='#800080')
label1.place(x=0,y=10)

#---------instructions-----------
label2= Label(cal, text='''INSTRUCTIONS:
* To generate calendar of a particular month of a particular year,
select the suitable month from the dropdown 'Month' and enter the
suitable year in the 'Year' text box.
* Then, press the 'Generate Calendar' button.
* The calendar generated will appear on a new page.''',font=('times new roman',14),fg='#ffc700')
label2.place(x=50,y=90)


#-----------commands-------------
def generate():
    m=drop.get()
    y=int(text1.get())
    if m==opt[0]:
        messagebox.showwarning('Warning','Select Month from the Dropdown')
    elif y<=0 :
        messagebox.showwarning("Warning",'Enter a suitable year to generate calendar')
    else:    
        if m=='January':
           mon=1
        elif m=='February':
           mon=2
        elif m=='March':
           mon=3
        elif m=='April':
           mon=4
        elif m=='May':
           mon=5
        elif m=='June':
           mon=6
        elif m=='July':
           mon=7
        elif m=='August':
           mon=8
        elif m=='September':
           mon=9
        elif m=='October':
           mon=10
        elif m=='November':
           mon=11
        elif m=='December':
           mon=12
        
        new=Tk()
        new.geometry('300x300')
        new.config(background='white')
        new.title('Calendar')
        new.resizable(False,False)

        head= ' Calendar for '+m+' '+str(y)
        heading=Label(new, text=head, font=('times new roman',16,'bold'),fg='#065535')
        heading.place(x=0,y=10)

        l31=[1,3,5,7,8,10,12]
        l30=[4,6,9,11]

        if mon in l31:
           d=31
        elif mon in l30:
           d=30
        elif mon==2:
           if y%4==0:
              d=29
           else:
              d=28

        cal= Calendar(new, year=y,month=mon,day=d)
        cal.place(x=30,y=70)

        messagebox.showinfo('Information','Calendar Generated')

        new.mainloop()

#------------dropdowns-----------
opt=['Select Month','January','February','March','April','May','June','July','August','September','October','November','December']
drop=StringVar(cal)
dropdown1=OptionMenu(cal,drop,*opt)
dropdown1.place(x=150,y=250)
drop.set(opt[0])


#------labels and textboxes------
label3= Label(cal, text='Month:',font=('times new roman',14))
label3.place(x=50,y=250)
label4= Label(cal, text='Year:',font=('times new roman',14))
label4.place(x=350,y=250)

text1= Entry(cal,width=10)
text1.place(x=400,y=250)

#-----------button---------------
button1= Button(cal, text='GENERATE CALENDAR', font=('times new roman',12),command=generate)
button1.place(x=230,y=300)

#----------voice instructions----
















cal.mainloop()
