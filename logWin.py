import tkinter
from tkinter import *
import quickstart

window = Tk()

def loginGmail():
        try:
            quickstart.main()
            login_succes = True
        except:
            window.destroy()
        if(login_succes == True):
            window.destroy()
            import senWind

titulo = tkinter.Label(window, text="Spamador de Emails")
titulo.config(font=("Helvetica", 15))
titulo.place(x=100,y=15)

btn1 = tkinter.Button(window, text="Logar", fg='black', command=lambda: loginGmail())
btn1.config(width=20, height=2)
btn1.place(x=100, y=150)

btn2 = tkinter.Button(window, text="Sair", fg="black", command=lambda: window.destroy())
btn2.config(width=5,height=2)
btn2.place(x=280, y=150)

window.title('Spam Mail')
window.geometry("400x300+10+20")
window.resizable(width=False, height=False)
window.mainloop()