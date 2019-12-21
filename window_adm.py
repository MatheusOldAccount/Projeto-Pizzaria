from tkinter import *
import projeto.conexao
from tkinter import messagebox
valnivel = 0


class Window():
    def __init__(self):
        self.novajanela = Tk()
        self.novajanela.title('Administrador')
        projeto.conexao.registros_usuarios()
        Label(self.novajanela, text='AAAAA').grid(row=0, column=0)
        self.novajanela.mainloop()


def verifica_login(usuario, senha):
    global valnivel
    registros = projeto.conexao.registros_usuarios()
    verifica = usuariofalso = senhafalsa = False
    for elementos in registros:
        if elementos['nome'] == usuario and elementos['senha'] == senha:
            verifica = usuariofalso = senhafalsa = True
            valnivel = elementos['nivel']
        elif elementos['nome'] == usuario:
            usuariofalso = True
        elif elementos['senha'] == senha:
            senhafalsa = True
    if not usuariofalso:
        messagebox.showinfo('Erro', 'Não existe este usuário cadastrado no banco de dados')
    elif not senhafalsa:
        messagebox.showinfo('Erro', 'Senha incorreta')
    return verifica
