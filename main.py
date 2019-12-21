from tkinter import *


def on_enter(e):
    entrar['background'] = '#ba0601'
    cadastrar['background'] = '#ba0601'


def on_leave(e):
    entrar['background'] = '#eb3b31'
    cadastrar['background'] = '#eb3b31'


janela = Tk()
janela.configure(background='#fbb339')
janela.title('Modelo de Pizzaria')
janela.geometry('800x800')
janela.resizable(False, False)
imagem = PhotoImage(file='image.png')
foto = Label(janela, image=imagem)
foto.grid(row=0, column=0)

Label(janela, text='  Faça o Login ou Cadastre-se', fg='white', bg='#fbb339', font=('Century Gothic bold', 35), pady=30).grid(row=1, column=0)

firstframe = Frame(janela, bg='#fbb339')
Label(firstframe, text='  Usuário', font=('Century Gothic bold', 16), bg='#fbb339', padx=20).grid(row=0, column=0)
user = Entry(firstframe)
user.grid(row=0, column=1)
firstframe.grid(row=2, column=0)

secondframe = Frame(janela, bg='#fbb339')
Label(secondframe, text='Senha', font=('Century Gothic bold', 16), bg='#fbb339', padx=32, pady=10).grid(row=0, column=0)
password = Entry(secondframe, show='*')
password.grid(row=0, column=1)
secondframe.grid(row=3, column=0)

thirdframe = Frame(janela, bg='#fbb339', pady=20)
entrar = Button(thirdframe, text='Entrar', width=20, bg='#eb3b31', font=('Century Gothic bold', 10), fg='white', activeforeground='yellow', activebackground='#347e1f')
entrar.grid(row=0, column=0)
Label(thirdframe, bg='#fbb339', padx=10).grid(row=0, column=1)
cadastrar = Button(thirdframe, text='Cadastrar', width=20, bg='#eb3b31', font=('Century Gothic bold', 10), fg='white', activeforeground='yellow', activebackground='#347e1f')
cadastrar.grid(row=0, column=2)
thirdframe.grid(row=4, column=0)

entrar.bind("<Enter>", on_enter)
entrar.bind("<Leave>", on_leave)
cadastrar.bind("<Enter>", on_enter)
cadastrar.bind("<Leave>", on_leave)

janela.mainloop()
