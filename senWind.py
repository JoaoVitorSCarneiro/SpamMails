import tkinter
from tkinter import *
import SMPTmail

window = Tk()

def sendMail():
    try:
        SMPTmail.gmail_send_message()
        open_popup("Sucesso","Mensagem enviada com sucesso")
    except:
        open_popup("Usuário Não Autorizado","Não foi possivel enviar a mensagem \n Usuário não autorizado")

textCointainer = tkinter.Frame(window)
textCointainer.place(x=20,y=180)


receiverLabel = tkinter.Label(window, text="PARA > " , fg='black')
receiverLabel.config(width=0, height=2)
receiverLabel.place(x=5,y=60)

subjectLabel = tkinter.Label(window, text="ASSUNTO > " , fg='black')
subjectLabel.config(width=0, height=2)
subjectLabel.place(x=5, y=100)

senderMail = tkinter.Label(window,text="Para quem você quer enviar o e-mail", fg='black')
senderMail.pack(expand=True)
senderMail.place(x=55, y=25)

receiverMail = tkinter.Entry(window, fg='black')
receiverMail.config(width=50)
receiverMail.pack(expand=True)
receiverMail.place(x=55, y=65)

subjectMail = tkinter.Entry(window, fg='black')
subjectMail.config(width=35)
subjectMail.pack(expand=True)
subjectMail.place(x=80, y=105)

#inputVal = contentMail.get("1.0",'end-1c')

contentMail = tkinter.Text(textCointainer, fg='black')
contentMail.config(x=10,y=100,width=45, height=10)
contentMail.pack(ipadx=10,ipady=50)


def open_popup(titulo,texto):
   top= Toplevel(window)
   top.resizable(width=False, height=False)
   top.geometry("280x100")
   top.title(titulo)
   Label(top, text= texto, font=('Mistral 10 bold')).place(x=30,y=35)

btn1 = tkinter.Button(window, text="Enviar", fg='black', command=lambda: sendMail())
btn1.config(width=10, height=2)
btn1.place(x=410, y=400)


window.title('Spam Mail')
window.geometry("500x500+10+20")
window.resizable(width=False, height=False)
window.mainloop()