from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import messagebox

dat=Tk()
dat.geometry('550x450')
dat.title('Number of Days between Two Dates')
dat.config(background='#ff00ff')

#---------heading--------
label1= Label(dat, text='''      NUMBER OF DAYS BETWEEN     
TWO DATES       ''',anchor='center', font=('times new roman',24,'bold'), fg='#990000')
label1.place(x=0,y=10)

#--------commands--------
def diff():
    l31=[1,3,5,7,8,10,12]
    l30=[4,6,9,11]
    if drop_day1.get()==opt_day[0] or drop_day2.get()==opt_day[0]:
        messagebox.showwarning('Warning','Please Select the Day from the dropdown')
        return
    elif drop_mon1.get()==opt_mon[0] or drop_mon2.get()==opt_mon[0]:
        messagebox.showwarning('Warning','Please Select the Month from the dropdown')
        return
    elif text1.get()=='' or text2.get()=='':
        messagebox.showwarning('Warning','Please Enter the Year in the Textbox')
        return
    else:
        try:
            dat1=str(text1.get())+','+str(drop_mon1.get())+','+str(drop_day1.get())
            dat2=str(text2.get())+','+str(drop_mon2.get())+','+str(drop_day2.get())

            dat_format='%Y,%m,%d'

            date1=datetime.strptime(dat1, dat_format).date()
            date2=datetime.strptime(dat2, dat_format).date()
            
            if date1> date2:
               messagebox.showwarning('Warning','Date 2 selected is smaller than Date 1. Please select accordingly.')
            elif date1==date2:
               messagebox.showinfo('Result','Same Date Selected')
        
            else:
               total=date2-date1
               tot=total.days
               msg='The number of days between given dates is:' + str(tot)
               messagebox.showinfo('Result',msg)

        except ValueError:
            messagebox.showwarning('Warning','Invalid Date Format')
            return
#-------instructions------
label2= Label(dat, text='''INSTRUCTIONS:
*Select date 1 by selecting day and month from dropdown and entering
the year in the text box.
*Similarly, select date 2 by selecting day and month from dropdown
and entering the year in the text box.
*Then, click the 'Number of Days' button.
*Your output will flash on a messagebox.''', font=('times new roman',12),fg='#ff6666')
label2.place(x=60,y=110)

#-------dropdowns---------
opt_day=['Select Day','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
opt_mon=['Select Month','1','2','3','4','5','6','7','8','9','10','11','12']
drop_day1= StringVar(dat)
drop_mon1= StringVar(dat)
drop_day2= StringVar(dat)
drop_mon2= StringVar(dat)

dropdown_day1= OptionMenu(dat,drop_day1,*opt_day)
dropdown_day1.place(x=80,y=280)
dropdown_mon1= OptionMenu(dat,drop_mon1,*opt_mon)
dropdown_mon1.place(x=270,y=280)

drop_day1.set(opt_day[0])
drop_mon1.set(opt_mon[0])

dropdown_day2= OptionMenu(dat,drop_day2,*opt_day)
dropdown_day2.place(x=80,y=330)
dropdown_mon2= OptionMenu(dat,drop_mon2,*opt_mon)
dropdown_mon2.place(x=270,y=330)

drop_day2.set(opt_day[0])
drop_mon2.set(opt_mon[0])

#---labels and textboxes--
label3= Label(dat, text='Day:', font=('times new roman', 12))
label3.place(x=30,y=280)
label4= Label(dat, text='Month:', font=('times new roman',12))
label4.place(x=200,y=280)
label5= Label(dat, text='Year:', font=('times new roman',12))
label5.place(x=400,y=280)

label6= Label(dat, text='Day:', font=('times new roman', 12))
label6.place(x=30,y=330)
label7= Label(dat, text='Month:', font=('times new roman',12))
label7.place(x=200,y=330)
label8= Label(dat, text='Year:', font=('times new roman',12))
label8.place(x=400,y=330)

text1= Entry(dat, width=10)
text1.place(x=450,y=280)
text2= Entry(dat, width=10)
text2.place(x=450,y=330)

#----------button---------
button1= Button(dat, text='NUMBER OF DAYS',font=('times new roman',12),command=diff)
button1.place(x=230,y=380)








dat.mainloop()
