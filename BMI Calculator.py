from tkinter import *
from tkinter import messagebox

bmi=Tk()
bmi.geometry('700x500')
bmi.title('BMI Calculator')
bmi.config(bg='#ffdab9')

#--------heading---------
label1= Label(bmi, text='''         BODY MASS INDEX (BMI)           
         CALCULATOR         ''',anchor='center', font=('times new roman',30,'bold'), fg='#4a1c7a')
label1.place(x=0,y=10)

#-------instructions------
label2= Label(bmi, text='''INSTRUCTIONS:
*Firstly, choose the unit of weight and height from the respective radio buttons
'Unit of Weight' and 'Unit of Height'.
*Then, insert the values of your weight and height.
*Finally, press the 'Calculate BMI' button and view your analysis.
''', font=('times new roman',14), fg='#468499')
label2.place(x=50,y=130)

#-------commands---------
def bmi_cal():
    if text1.get()=='' or text2.get()=='':
        messagebox.showwarning('Warning','All Particulars are Compulsory')
    elif var_m.get()=='' or var_h.get()=='':
        messagebox.showwarning('Warning','Radio Button/s not selected')
    else:
        mass= float(text1.get())
        hei= float(text2.get())
        if var_m.get()=='kg':
            if var_h.get()=='m':
                tot=mass/(hei*hei)
            elif var_h.get()=='cm':
                h= hei*0.01
                tot=mass/(h*h)
            elif var_h.get()=='inches':
                h= hei*0.0254
                tot=mass/h*h
        elif var_m.get()=='pounds':
            if var_h.get()=='m':
                h=hei/0.0254
                tot= (mass*703)/h*h
            elif var_h.get()=='cm':
                h= hei/2.54
                tot= mass*703/h*h
            elif var_h.get()=='inches':
                tot=(mass*703)/(hei*hei)
        total=round(tot,2)
        if total<18.5:
            ana='UNDERWEIGHT'
        elif total>25:
            ana='OVERWEIGHT'
        else:
            ana='HEALTHY'

        msg='Your Body Mass Index is '+str(total)+ '. You are '+ana+'.'
        messagebox.showinfo('BMI Calculation and Analysis',msg)

#------radio buttons------
var_m= StringVar(value='kg')
radio1= Radiobutton(bmi, text='Kilograms', value='kg',variable=var_m)
radio1.place(x=150,y=300)
radio2= Radiobutton(bmi, text='Pounds',value='pounds',variable=var_m)
radio2.place(x=250,y=300)

var_h= StringVar(value='m')
radio3= Radiobutton(bmi, text='Metres', value='m',variable=var_h)
radio3.place(x=450,y=300)
radio4= Radiobutton(bmi, text='Centimetres', value='cm',variable=var_h)
radio4.place(x=520,y=300)
radio5= Radiobutton(bmi, text='Inches', value='inches',variable=var_h)
radio5.place(x=620,y=300)

#---labels and textboxes---
label3= Label(bmi, text='Unit for Weight', font=('times new roman',12))
label3.place(x=20,y=300)
label4= Label(bmi, text='Unit for Height', font=('times new roman',12))
label4.place(x=350,y=300)

label5= Label(bmi, text='Your Weight:', font=('times new roman',12))
label5.place(x=150,y=350)
label6= Label(bmi, text='Your Height:', font=('times new roman',12))
label6.place(x=350,y=350)

text1= Entry(bmi, width=10)
text1.place(x=250,y=350)
text2= Entry(bmi, width=10)
text2.place(x=450,y=350)

#--------buttons----------
button1= Button(bmi, text='Calculate BMI', command=bmi_cal,font=('times new roman',12))
button1.place(x=300,y=400)







bmi.mainloop()

