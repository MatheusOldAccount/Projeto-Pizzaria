from tkinter import *
import projeto.conexao
from tkinter import messagebox
valnivel = 0
user_now = ''


class Window():
    def __init__(self):
        if valnivel == 2:
            self.novajanela = Tk()
            self.novajanela.title('Administrador')
            self.novajanela.geometry('800x800')
            self.novajanela.resizable(False, False)
            self.novajanela.configure(background='#1960a6')
            self.img = PhotoImage(file='adm.png')
            Label(self.novajanela, image=self.img).grid(row=0, column=0)
            self.layout = Frame(self.novajanela, width=800, height=400, bg='#1960a6')
            Label(self.layout, text=f'Usuário Logado: {user_now}', fg='white', bg='#1960a6', font=('Century Gothic bold', 16), pady=20).grid(row=0, column=0, columnspan=2)
            Button(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Pedidos em Andamento', padx=5, pady=5).grid(row=1, column=0, padx=20, pady=20)
            Button(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Todos os Pedidos', padx=5, pady=5).grid(row=1, column=1, padx=20, pady=20)
            Button(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastros', padx=5, pady=5).grid(row=2, column=0, padx=20, pady=20)
            Button(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastrar Novo Administrador', padx=5, pady=5).grid(row=2, column=1, padx=20, pady=20)
            Button(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Voltar', padx=5, pady=5, command=self.sair).grid(row=3, column=0, columnspan=2, padx=20, pady=20)
            self.layout.grid(row=1, column=0)
            self.novajanela.mainloop()
        else:
            print('tchau')
            exit()

    def sair(self):
        self.novajanela.destroy()
        import projeto.main
        projeto.main.Principal()


def verifica_login(usuario, senha):
    global valnivel, user_now
    registros = projeto.conexao.registros_usuarios()
    verifica = usuariofalso = senhafalsa = False
    for elementos in registros:
        if elementos['nome'] == usuario and elementos['senha'] == senha:
            verifica = usuariofalso = senhafalsa = True
            valnivel = int(elementos['nivel'])
            user_now = elementos['nome']
        elif elementos['nome'] == usuario:
            usuariofalso = True
        elif elementos['senha'] == senha:
            senhafalsa = True
    if not usuariofalso:
        messagebox.showinfo('Erro', 'Não existe este usuário cadastrado no banco de dados')
    elif not senhafalsa:
        messagebox.showinfo('Erro', 'Senha incorreta')
    return verifica
