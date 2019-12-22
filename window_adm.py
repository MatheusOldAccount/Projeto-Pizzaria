from tkinter import *
from tkinter import ttk
import projeto.conexao
from tkinter import messagebox
import projeto.button as botao
valnivel = 0
user_now = ''


def destruir():
    exit()


class Window():
    def __init__(self):
        if valnivel == 2:
            tela = self.novajanela = Tk()
            tela.protocol("WM_DELETE_WINDOW", destruir)
            self.novajanela.title('Administrador')
            self.novajanela.geometry('800x800')
            self.novajanela.resizable(False, False)
            self.novajanela.configure(background='#1960a6')
            self.img = PhotoImage(file='adm.png')
            Label(self.novajanela, image=self.img).grid(row=0, column=0)
            self.layout = Frame(self.novajanela, width=800, height=400, bg='#1960a6')
            Label(self.layout, text=f'Usuário Logado: {user_now}', fg='white', bg='#1960a6', font=('Century Gothic bold', 16), pady=20).grid(row=0, column=0, columnspan=2)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Pedidos em Andamento', padx=5, pady=5).grid(row=1, column=0, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Todos os Pedidos', padx=5, pady=5).grid(row=1, column=1, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastros', padx=5, pady=5, command=self.cadastros).grid(row=2, column=0, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastrar Novo Administrador', padx=5, pady=5).grid(row=2, column=1, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Gerar Estatísticas', padx=5, pady=5).grid(row=3, column=0, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Voltar', padx=5, pady=5, command=self.sair).grid(row=3, column=1, padx=20, pady=20)
            self.layout.grid(row=1, column=0)
            self.novajanela.mainloop()
        else:
            print('tchau')
            exit()

    def sair(self):
        self.novajanela.destroy()
        import projeto.main as inicial
        inicial.Principal()

    def cadastros(self):
        pesquisa = projeto.conexao.registros_usuarios()
        self.smallwindow = Toplevel()
        self.smallwindow.geometry('600x400')
        self.smallwindow.title('Todos os Usuários Cadastrados')
        self.smallwindow.grid_rowconfigure(0, weight=1)
        self.smallwindow.grid_columnconfigure(0, weight=1)

        tree = ttk.Treeview(self.smallwindow, selectmode='browse', column=('name', 'sex', 'address', 'level'), show='headings')
        tree.pack(expand=True, fill='both')

        tree.column('name', minwidth=50, width=200, stretch=NO)
        tree.heading('#1', text='Nome')

        tree.column('sex', minwidth=50, width=50, stretch=NO)
        tree.heading('#2', text='Sexo')

        tree.column('address', minwidth=50, width=300, stretch=NO)
        tree.heading('#3', text='Endereço')

        tree.column('level', minwidth=50, width=50, stretch=NO)
        tree.heading('#4', text='Nível')

        lista_auxiliar = list()
        for registros in pesquisa:
            lista_auxiliar.append(registros['nome'])
            lista_auxiliar.append(registros['sexo'])
            lista_auxiliar.append(registros['endereco'])
            lista_auxiliar.append(registros['nivel'])
            tree.insert("", END, values=lista_auxiliar, tag='1')
            lista_auxiliar.clear()

        self.smallwindow.mainloop()


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
