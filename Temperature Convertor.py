from tkinter import *
from tkinter import messagebox

temp=Tk()
temp.geometry('700x400')
temp.config(background='#ccffcc')
temp.title('Temperature Convertor')
temp.resizable(False,False)
#--------commands----------
def convert():
    temp1=float(text1.get())
    temp2=None
    if drop_one.get()==options[0] or drop_two.get()==options[0]:
        messagebox.showwarning('Warning','Please select the unit of temperature in both the dropdowns.')
    elif drop_one.get()==drop_two.get():
        messagebox.showwarning('Warning','Same unit selected in both dropdowns')
        temp2=temp1
    else:
        #----converting c to f or k--------
        if drop_one.get()=='Celsius':
            if drop_two.get()=='Farhenheit':
                temp2=temp1*1.8 +32
            elif drop_two.get()=='Kelvin':
                temp2=temp1 +273.15
            else:
                messagebox.showwarning('Warning',"Dropdown 'Temperature to Convert' not selected")

        #----converting f to c or k--------
        elif drop_one.get()== 'Farhenheit':
            if drop_two.get()=='Celsius':
                temp2=(temp1-32)/1.8
            elif drop_two.get()=='Kelvin':
                temp2=(temp1+459.67)*5/9
            else:
                messagebox.showwarning('Warning',"Dropdown 'Temperature to Convert' not selected")

        #----converting k to f or c--------
        elif drop_one.get()=='Kelvin':
            if drop_two.get()=='Farhenheit':
                temp2=temp1*1.8-459.67
            elif drop_two.get()=='Celsius':
                temp2=temp1-273.15
            else:
                messagebox.showwarning('Warning',"Dropdown 'Temperature to Convert' not selected")
        else:
                messagebox.showwarning('Warning',"Dropdown 'Temperature to Convert' not selected")
        if text2.get()=='':
            text2.insert(END,temp2)
        elif text2.get() is not None:
            text2.delete(0,END)
            text2.insert(END,temp2)
#--------heading-----------
label1=Label(temp,text='TEMPERATURE CONVERTOR',anchor='center',font=('times new roman',36,'bold'),fg='#731631')
label1.place(x=0,y=10)

#-------instructions-------
label2=Label(temp,text='''INSTRUCTIONS:
* To convert temperature from one unit to another, select the current unit
of temperature in dropdown 'Current Unit of Temperature' and the wanted
unit in dropdown 'Converted Unit of Temperature'.
* Next, enter the temperature to be converted in text box 'Temperature to Convert'.
* Then, press the 'Convert' button.
* The converted temperature will appear in 'Converted Temperature' text box.''',font=('times new roman',14),fg='#230f73')
label2.place(x=50,y=90)

#-------dropdowns---------
options=['Select Unit','Celsius','Farhenheit','Kelvin']
drop_one=StringVar(temp)
dropdown1=OptionMenu(temp,drop_one,*options)
dropdown1.place(x=215,y=260)
drop_one.set(options[0])

drop_two=StringVar(temp)
dropdown2=OptionMenu(temp,drop_two,*options)
dropdown2.place(x=560,y=260)
drop_two.set(options[0])

#----labels and textboxes--
label3= Label(temp, text='Current Unit of Temperature:',font=('times new roman',12))
label3.place(x=20,y=260)
label4= Label(temp, text='Converted Unit of Temperature:', font=('times new roman',12))
label4.place(x=350,y=260)

label5= Label(temp, text='Temperature to Convert:',font=('times new roman',12))
label5.place(x=20,y=300)
label6= Label(temp, text='Converted Temperature:',font=('times new roman',12))
label6.place(x=350,y=300)

text1= Entry(temp,width=10)
text1.place(x=215,y=300)
text2= Entry(temp,width=10)
text2.place(x=560,y=300)

#----convert button--------
button1= Button(temp,text='CONVERT TEMPERATURE',font=('times new roman',14), command=convert)
button1.place(x=250,y=350)

#----voice instructions----













temp.mainloop()
