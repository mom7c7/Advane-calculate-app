from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry('300x600')
root.resizable(0,0)
root.title('Calc App')
root.configure(bg='#00AEDB')
# Frame
frm1 = Frame(root,bg='#00AED8',width=300,height=100)
frm1.pack()
frm2 = Frame(root,bg='#00AED8',width=300,height=100)
frm2.pack()
frm3 = Frame(root,bg='#00AED8',width=300,height=100)
frm3.pack()
frm4 = Frame(root,bg='#00AED8',width=300,height=100)
frm4.pack()
frm5 = Frame(root,bg='#00AED8',width=300,height=100)
frm5.pack()
frm6 = Frame(root,bg='#00AED8',width=300,height=100)
frm6.pack()
# Vars
num = StringVar()
nums = ''
pl = 0
st = ''
num.set(nums)
# Entry
ent1 = Entry(frm1,width=30,font=('Boulder',38),textvariable=num)
ent1.pack(fill='x',pady=10)

# Def
def clear():
    global nums
    nums = ''
    num.set(nums)
def equ():
    global nums , st
    mynum = num.get()
    st = st + str(mynum)
    nums = ''
    num.set(nums)
    allt = st.split(' ')
    first = str(allt[0])
    sec = str(allt[2])
    tata = str(allt[1])
    res = 0
    if tata == '+':
        res = int(first) + int(sec)
    elif tata == '-':
        res = int(first) - int(sec)
    elif tata == '*':
        res = int(first) * int(sec)
    elif tata == '/':
        if int(sec) == 0:
            tkinter.messagebox.showerror('ERROR','Can`t Divide Zero')
        else :
            res = int(first) / int(sec)            
    num.set(res)
def plus():
    global nums , pl , st
    mynum = num.get()
    st = str(mynum) + ' + '
    nums = ''
    num.set(nums)
def min():
    global nums , pl , st
    mynum = num.get()
    st = str(mynum) + ' - '
    nums = ''
    num.set(nums)
def mult():
    global nums , pl , st
    mynum = num.get()
    st = str(mynum) + ' * '
    nums = ''
    num.set(nums)
def div():
    global nums , pl , st
    mynum = num.get()
    st = str(mynum) + ' / '
    nums = ''
    num.set(nums)
def seven():
    global nums
    nums = nums + '7'
    num.set(nums)
def eight():
    global nums
    nums = nums + '8'
    num.set(nums)
def nine():
    global nums
    nums = nums + '9'
    num.set(nums)
def four():
    global nums
    nums = nums + '4'
    num.set(nums)
def five():
    global nums
    nums = nums + '5'
    num.set(nums)
def six():
    global nums
    nums = nums + '6'
    num.set(nums)
def one():
    global nums
    nums = nums + '1'
    num.set(nums)
def two():
    global nums
    nums = nums + '2'
    num.set(nums)
def three():
    global nums
    nums = nums + '3'
    num.set(nums)
def zero():
    global nums
    nums = nums + '0'
    num.set(nums)
# def nine():


# Button

btn7 = Button(frm2,text='7',width=6,height=3,command=seven)
btn7.pack(side='left',padx=10)
btn8 = Button(frm2,text='8',width=6,height=3,command=eight)
btn8.pack(side='left',padx=10)
btn9 = Button(frm2,text='9',width=6,height=3,command=nine)
btn9.pack(side='left',padx=10)
btnp = Button(frm2,text='+',width=6,height=3,command=plus)
btnp.pack(side='left',padx=10)
#
btn4 = Button(frm3,text='4',width=6,height=3,command=four)
btn4.pack(side='left',padx=10,pady=10)
btn5 = Button(frm3,text='5',width=6,height=3,command=five)
btn5.pack(side='left',padx=10,pady=10)
btn6 = Button(frm3,text='6',width=6,height=3,command=six)
btn6.pack(side='left',padx=10,pady=10)
btnm = Button(frm3,text='-',width=6,height=3,command=min)
btnm.pack(side='left',padx=10,pady=10)
#
btn1 = Button(frm4,text='1',width=6,height=3,command=one)
btn1.pack(side='left',padx=10,pady=10)
btn2 = Button(frm4,text='2',width=6,height=3,command=two)
btn2.pack(side='left',padx=10,pady=10)
btn3 = Button(frm4,text='3',width=6,height=3,command=three)
btn3.pack(side='left',padx=10,pady=10)
btnd = Button(frm4,text='/',width=6,height=3,command=div)
btnd.pack(side='left',padx=10,pady=10)
#
btnc = Button(frm5,text='C',width=6,height=3,command=clear)
btnc.pack(side='left',padx=10,pady=10)
btn0 = Button(frm5,text='0',width=6,height=3,command=zero)
btn0.pack(side='left',padx=10,pady=10)
btnmu = Button(frm5,text='*',width=6,height=3,command=mult)
btnmu.pack(side='left',padx=10,pady=10)
btne = Button(frm5,text='=',width=6,height=3,command=equ)
btne.pack(side='left',padx=10,pady=10)
print()
root.mainloop()