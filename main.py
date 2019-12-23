from tkinter import *
from tkinter import messagebox


def destruir():
    exit()


class Principal():
    def entrar(self):
        if len(self.user.get()) == 0 and len(self.password.get()) == 0:
            messagebox.showinfo('Erro', 'Ambos campos estão vazios')
        elif len(self.user.get()) == 0:
            messagebox.showinfo('Erro', 'O campo do usuário está vazio')
        elif len(self.password.get()) == 0:
            messagebox.showinfo('Erro', 'O campo da senha está vazio')
        else:
            import projeto.window_adm as new
            if new.verifica_login(self.user.get(), self.password.get()):
                self.janela.destroy()
                new.Window()

    def criar(self):
        import projeto.window_user as usuario
        usuario.Criacao()

    def on_enter(self, e):
        self.entrar['background'] = '#ba0601'
        self.cadastrar['background'] = '#ba0601'

    def on_leave(self, e):
        self.entrar['background'] = '#eb3b31'
        self.cadastrar['background'] = '#eb3b31'

    def __init__(self):
        prin = self.janela = Tk()
        prin.protocol("WM_DELETE_WINDOW", destruir)
        self.janela.configure(background='#fbb339')
        self.janela.title('Modelo de Pizzaria')
        self.janela.geometry('800x800')
        self.janela.resizable(False, False)
        self.imagem = PhotoImage(file='image.png')
        self.foto = Label(self.janela, image=self.imagem)
        self.foto.grid(row=0, column=0)

        Label(self.janela, text='  Faça o Login ou Cadastre-se', fg='white', bg='#fbb339', font=('Century Gothic bold', 35), pady=30).grid(row=1, column=0)

        self.firstframe = Frame(self.janela, bg='#fbb339')
        Label(self.firstframe, text='  Usuário', font=('Century Gothic bold', 16), bg='#fbb339', padx=20).grid(row=0, column=0)
        self.user = Entry(self.firstframe)
        self.user.grid(row=0, column=1)
        self.firstframe.grid(row=2, column=0)

        self.secondframe = Frame(self.janela, bg='#fbb339')
        Label(self.secondframe, text='Senha', font=('Century Gothic bold', 16), bg='#fbb339', padx=32, pady=10).grid(row=0, column=0)
        self.password = Entry(self.secondframe, show='*')
        self.password.grid(row=0, column=1)
        self.secondframe.grid(row=3, column=0)

        self.thirdframe = Frame(self.janela, bg='#fbb339', pady=20)
        self.entrar = Button(self.thirdframe, text='Entrar', width=20, bg='#eb3b31', font=('Century Gothic bold', 10), fg='white', activeforeground='yellow', activebackground='#347e1f', command=self.entrar)
        self.entrar.grid(row=0, column=0)
        Label(self.thirdframe, bg='#fbb339', padx=10).grid(row=0, column=1)
        self.cadastrar = Button(self.thirdframe, text='Cadastrar', width=20, bg='#eb3b31', font=('Century Gothic bold', 10), fg='white', activeforeground='yellow', activebackground='#347e1f', command=self.criar)
        self.cadastrar.grid(row=0, column=2)
        self.thirdframe.grid(row=4, column=0)

        self.entrar.bind("<Enter>", self.on_enter)
        self.entrar.bind("<Leave>", self.on_leave)
        self.cadastrar.bind("<Enter>", self.on_enter)
        self.cadastrar.bind("<Leave>", self.on_leave)

        self.janela.mainloop()


Principal()
