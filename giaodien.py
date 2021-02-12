from tkinter import *
from requests import session
import re
window = Tk()
window.title("Check Mail")
lbl=Label(window, text="Nhap Hotmail")
lbl.grid(column=0, row="0")
hot_mail= Entry(window)
hot_mail.grid(column="1", row=0)
def checkMail(s, email):
    DL = s.get('https://signup.live.com/signup?username='+email+'@hotmail.com&lic=1')
    x = (DL.text)
    kq = re.search("isAvailable", x)
    if kq == None:
        print("Email đã được sử ")
    else:dụng
        file = open('pp.txt', 'a').write(email+'@hotmail.com'+'\n')
def Run():
    s = session()
    email= hot_mail.get()
    for i in range(1, 101):
        new_email = email + str(i)

        checkMail(s, new_email)


b1=Button(window, text="Check", width="10", height="1", command=Run)
b1.grid(column=3, row=0)
window.mainloop()
