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
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Pedidos em Andamento', padx=5, pady=5, command=PedidosAtuais).grid(row=1, column=0, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Todos os Pedidos', padx=5, pady=5, command=self.front_and_back_end_pedidos).grid(row=1, column=1, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastros', padx=5, pady=5, command=self.cadastros).grid(row=2, column=0, padx=20, pady=20)
            botao.HoverButton(self.layout, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Cadastrar Novo Administrador', padx=5, pady=5, command=self.front_end_adm).grid(row=2, column=1, padx=20, pady=20)
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

    def back_end_adm(self):
        listanomes = []
        listaauxiliar = []
        busca = projeto.conexao.registros_usuarios()
        for registros in busca:
            listaauxiliar.append(registros['nome'])
            listaauxiliar.append(registros['senha'])
            listanomes.append(listaauxiliar[:])
            listaauxiliar.clear()
        self.verifica = False
        for comparacoes in listanomes:
            if self.n.get() == comparacoes[0] and self.s.get() == comparacoes[1]:
                self.verifica = True
        if len(self.n.get()) == 0 or len(self.s.get()) == 0 or len(self.sex.get()) == 0 or len(self.e.get()) == 0:
            messagebox.showinfo('Erro', 'Algum(ns) do(s) campo(s) está(ão) vazio(s)')
        elif len(self.s.get()) <= 3:
            messagebox.showinfo('Erro', 'A senha deve conter ao menos quatro caracteres')
        elif self.verifica:
            messagebox.showinfo('Erro', 'Este usuário e senha já está cadastrado no banco de dados. Por favor, digite algum(ns) do(s) dado(s) diferente(s)')
        else:
            try:
                self.genero = self.sex.get()[0].upper()
                print(self.genero)
            except:
                messagebox.showinfo('Erro', 'O campo sexo deve ser preenchido com [M/F]')
            else:
                if self.genero != 'M' and self.genero != 'F':
                    messagebox.showinfo('Erro', 'O campo sexo deve ser preenchido com [M/F]')
                else:
                    projeto.conexao.cadastro_adm(self.n.get(), self.s.get(), self.genero, self.e.get())
                    self.tela.destroy()

    def front_end_adm(self):
        self.tela = Toplevel()
        self.tela.configure(background='#fbb339')
        self.tela.title('Cadastro de um Novo Administrador')
        self.tela.geometry('340x300')
        self.tela.resizable(False, False)

        self.encapsular = Frame(self.tela, bg='#fbb339')
        self.encapsular.grid(row=0, column=0)

        Label(self.encapsular, font=('Century Gothic bold', 16), text='Nome', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=0, column=0)
        self.n = Entry(self.encapsular)
        self.n.grid(row=0, column=1)

        Label(self.encapsular, font=('Century Gothic bold', 16), text='Senha', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=1, column=0)
        self.s = Entry(self.encapsular, show='*')
        self.s.grid(row=1, column=1)

        Label(self.encapsular, font=('Century Gothic bold', 16), text='Sexo', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=2, column=0)
        self.sex = Entry(self.encapsular)
        self.sex.grid(row=2, column=1)

        Label(self.encapsular, font=('Century Gothic bold', 16), text='Endereço', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=3, column=0)
        self.e = Entry(self.encapsular)
        self.e.grid(row=3, column=1)

        Label(self.encapsular, bg='#fbb339').grid(row=4, column=0)
        botao.HoverButton(self.encapsular, font=('Century Gothic bold', 16), text='Cadastrar', pady=5, padx=5, fg='white', bg='#d32016', command=self.back_end_adm, activebackground='#1960a6', activeforeground='white').grid(row=4, column=1, pady=10, padx=30)

        self.tela.mainloop()

    def front_and_back_end_pedidos(self):
        self.pedidos = Toplevel()
        self.pedidos.title('Todos os pedidos já realizados')
        self.pedidos.geometry('1200x400')

        self.arvore = ttk.Treeview(self.pedidos, selectmode='browse', column=('id', 'namepe', 'namepro', 'user', 'password', 'place', 'obs'), show='headings')
        self.arvore.pack(expand=True, fill='both')

        self.arvore.column('id', width=10, minwidth=50)
        self.arvore.heading('#1', text='Id')

        self.arvore.column('namepe', width=100, minwidth=50)
        self.arvore.heading('#2', text='Nome da Pessoa')

        self.arvore.column('namepro', width=150, minwidth=50)
        self.arvore.heading('#3', text='Produto')

        self.arvore.column('user', width=40, minwidth=50)
        self.arvore.heading('#4', text='Usuário')

        self.arvore.column('password', width=30, minwidth=50)
        self.arvore.heading('#5', text='Senha')

        self.arvore.column('place', width=100, minwidth=50)
        self.arvore.heading('#6', text='Local de Entrega')

        self.arvore.column('obs', width=200, minwidth=50)
        self.arvore.heading('#7', text='Observações')

        self.buscas = projeto.conexao.registros_pedidos()

        valores = []

        for e in self.buscas:
            for dql in e.values():
                valores.append(dql)
            self.arvore.insert("", END, values=valores, tag='1')
            valores.clear()

        self.pedidos.mainloop()


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


class PedidosAtuais():
    def __init__(self):
        self.interface = Tk()
        self.interface.title('Todos os pedidos ainda não entregues')
        self.interface.geometry('1045x250')
        self.interface.configure(background='#fbb339')

        botao.HoverButton(self.interface, width=25, bg='#1960a6', fg='white', font=('Century Gothic bold', 14), text='Colocar Produto como Entregue', padx=5, pady=5, command=self.entregue).grid(row=0, column=0, padx=20, pady=20)

        self.arvorepedido = ttk.Treeview(self.interface, selectmode='browse', column=('id', 'datehour', 'id_product', 'id_request'), show='headings')

        self.arvorepedido.column('id', width=10, minwidth=50)
        self.arvorepedido.heading('#1', text='Id')

        self.arvorepedido.column('datehour', width=250, minwidth=50)
        self.arvorepedido.heading('#2', text='Data e Hora que o pedido foi realizado')

        self.arvorepedido.column('id_product', width=200, minwidth=50)
        self.arvorepedido.heading('#3', text='Produto')

        self.arvorepedido.column('id_request', width=250, minwidth=50)
        self.arvorepedido.heading('#4', text='Pessoa que fez o pedido')

        preencher = projeto.conexao.registros_pedidos_atuais()
        lista = list()
        for consultas in preencher:
            principal_id = consultas['id']
            for valores in consultas.values():
                lista.append(valores)
            self.arvorepedido.insert("", END, values=lista, iid=principal_id, tag='1')
            lista.clear()

        self.arvorepedido.grid(row=0, column=1, columnspan=12)

        self.interface.mainloop()

    def entregue(self):
        try:
            iddeletar = int(self.arvorepedido.selection()[0])
        except IndexError:
            messagebox.showinfo('Erro', 'Nenhum pedido selecionado')
        except Exception as error:
            messagebox.showinfo('Erro', f'Não foi possível realizar a operação. Erro: {error}')
        else:
            projeto.conexao.deletar_produto(iddeletar)
            self.interface.destroy()
            PedidosAtuais()

