from tkinter import *
import projeto.button as botao
import projeto.conexao
from tkinter import messagebox
from tkinter import ttk


def destruir():
    exit()


class User():
    def __init__(self):
        self.productos()

    def productos(self):
        from projeto.window_adm import user_now, senha_now
        self.un = user_now
        self.sn = senha_now
        self.screen = Tk()
        self.screen.protocol("WM_DELETE_WINDOW", destruir)
        self.screen.configure(background='#fbb339')
        self.screen.title('Interface do Usuário')
        self.screen.geometry('630x650')

        Label(self.screen, text=f'Usuário Logado: {user_now}', fg='white', bg='#e0a33d', font=('Century Gothic bold', 16), pady=20).grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.screen, text=f'Selecione um produto e clique em \'Comprar Produto\' caso deseje comprá-lo', fg='white', bg='#fbb339', font=('Century Gothic bold', 12), pady=20).grid(row=1, column=0, columnspan=2, pady=5)

        self.treeview = ttk.Treeview(self.screen, selectmode='browse', column=('name', 'group', 'price'), show='headings')

        self.treeview.column('name', width=200, minwidth=50, stretch=NO)
        self.treeview.heading('#1', text='Nome')

        self.treeview.column('group', width=200, minwidth=50, stretch=NO)
        self.treeview.heading('#2', text='Grupo')

        self.treeview.column('price', width=50, minwidth=50, stretch=NO)
        self.treeview.heading('#3', text='Preço')

        busca = projeto.conexao.registros_produtos()
        listaprodutos = list()

        for produto in busca:
            listaprodutos.append(produto['nome'])
            listaprodutos.append(produto['grupo'])
            listaprodutos.append(produto['preco'])
            self.treeview.insert("", END, iid=produto['id'], values=listaprodutos, tag='1')
            listaprodutos.clear()

        self.treeview.grid(row=2, column=0, padx=50, pady=50, columnspan=2)

        botao.HoverButton(self.screen, font=('Century Gothic bold', 16), text='Comprar Produto', pady=5, padx=5, fg='white', bg='#d32016', activebackground='#810e07', width=20, activeforeground='white', command=self.comprar_produto).grid(row=3, column=0, pady=10, padx=30)
        botao.HoverButton(self.screen, font=('Century Gothic bold', 16), text='Voltar', pady=5, padx=5, fg='white', bg='#d32016', activebackground='#810e07', width=20, activeforeground='white', command=self.sair).grid(row=3, column=1, pady=10, padx=30)
        botao.HoverButton(self.screen, font=('Century Gothic bold', 16), text='Histórico de Compras', pady=5, padx=5, fg='white', bg='#d32016', activebackground='#810e07', width=20, activeforeground='white', command=self.historico).grid(row=4, column=0, pady=10, padx=30, columnspan=2)

        self.screen.mainloop()

    def sair(self):
        self.screen.destroy()
        import projeto.main as inicial
        inicial.Principal()

    def historico(self):
        consulta = projeto.conexao.historico(self.un, self.sn)
        self.smallwindow = Toplevel()
        self.smallwindow.geometry('900x400')
        self.smallwindow.title('Todos os Usuários Cadastrados')
        self.smallwindow.grid_rowconfigure(0, weight=1)
        self.smallwindow.grid_columnconfigure(0, weight=1)

        tree = ttk.Treeview(self.smallwindow, selectmode='browse', column=('npp', 'pr', 'le', 'o'), show='headings')
        tree.pack(expand=True, fill='both')

        tree.column('npp', minwidth=50, width=100, stretch=NO)
        tree.heading('#1', text='Nome')

        tree.column('pr', minwidth=50, width=200, stretch=NO)
        tree.heading('#2', text='Produto')

        tree.column('le', minwidth=50, width=300, stretch=NO)
        tree.heading('#3', text='Local de Entrega')

        tree.column('o', minwidth=50, width=300, stretch=NO)
        tree.heading('#4', text='Observações')

        lista_auxiliar = list()
        for registros in consulta:
            lista_auxiliar.append(registros['nome_pessoa_pedido'])
            lista_auxiliar.append(registros['produto_requerido'])
            lista_auxiliar.append(registros['localEntrega'])
            lista_auxiliar.append(registros['observacoes'])
            tree.insert("", END, values=lista_auxiliar, tag='1')
            lista_auxiliar.clear()

        self.smallwindow.mainloop()

    def comprar_produto(self):
        all_products = projeto.conexao.registros_produtos()
        try:
            for elementos in all_products:
                if elementos['id'] == int(self.treeview.selection()[0]):
                    self.nome_produto = elementos['nome']
                    break
        except IndexError:
            messagebox.showerror('Erro', 'Nenhum produto selecionado')
        except Exception as erro:
            messagebox.showerror('Erro', f'Erro: {erro}')
        else:
            self.visual = Toplevel()
            self.visual.configure(background='#fbb339')
            self.visual.title('Menu de Compra')
            self.visual.geometry('500x300')
            self.visual.resizable(False, False)

            self.parte = Frame(self.visual, bg='#fbb339')
            self.parte.grid(row=0, column=0)

            Label(self.parte, font=('Century Gothic bold', 16), text='Nome Completo', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=0, column=0)
            self.noome = Entry(self.parte)
            self.noome.grid(row=0, column=1)

            Label(self.parte, font=('Century Gothic bold', 16), text='Local da Entrega', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=1, column=0)
            self.local = Entry(self.parte)
            self.local.grid(row=1, column=1)

            Label(self.parte, font=('Century Gothic bold', 16), text='Observações (se houverem)', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=2, column=0)
            self.obs = Entry(self.parte)
            self.obs.grid(row=2, column=1)

            botao.HoverButton(self.parte, font=('Century Gothic bold', 16), text='Comprar', pady=5, padx=5, fg='white', bg='#d32016', command=self.back_end_produto, activebackground='#1960a6', activeforeground='white').grid(row=3, column=0, pady=50, padx=50, columnspan=2)

            self.visual.mainloop()

    def back_end_produto(self):
        from datetime import datetime as datahora
        sistem = datahora.now().strftime('%Y-%m-%d %H:%M:%S')
        if len(self.noome.get()) == 0 and len(self.local.get()) == 0 and len(self.obs.get()) == 0:
            messagebox.showinfo('Erro', 'Todos os campos estão vazios')
        elif len(self.noome.get()) == 0 and len(self.local.get()) == 0:
            messagebox.showinfo('Erro', 'Os campos nome e local estão vazios')
        elif len(self.noome.get()) == 0 and len(self.obs.get()) == 0:
            messagebox.showinfo('Erro', 'Os campos nome e observação estão vazios')
        elif len(self.local.get()) == 0 and len(self.obs.get()) == 0:
            messagebox.showinfo('Erro', 'Os campos local e observação estão vazios')
        elif len(self.local.get()) == 0:
            messagebox.showinfo('Erro', 'O campo local está vazio')
        elif len(self.noome.get()) == 0:
            messagebox.showinfo('Erro', 'O campo nome está vazio')
        elif len(self.obs.get()) == 0:
            # print(f'nome pessoa = {self.noome.get()}\nproduto_requerido = {self.nome_produto}\nusuario = {self.un}\nsenha = {self.sn}\nlocal = {self.local.get()}\nobs = \ndatahora = {sistem}')
            try:
                projeto.conexao.cadastro_pedido(self.noome.get(), self.nome_produto, self.un, self.sn, self.local.get(), '')
            except Exception as erro:
                messagebox.showerror('Erro', 'Não foi possível se conectar ao banco de dados')
                exit()
            else:
                try:
                    pedidos = projeto.conexao.registros_pedidos()
                    for linhas in pedidos:
                        if self.noome.get() == linhas['nome_pessoa_pedido'] and self.nome_produto == linhas['produto_requerido'] and self.un == linhas['usuario'] and self.sn == linhas['senha'] and self.local.get() == linhas['localEntrega'] and len(linhas['observacoes']) == 0:
                            self.myid = linhas['id']
                            self.iddoproduto = int(self.treeview.selection()[0])
                    projeto.conexao.cadastro_produto_pedidos(sistem, self.iddoproduto, self.myid)
                except Exception as erro:
                    messagebox.showerror('Erro', f'Não foi possível se conectar ao banco de dados: {erro}')
                    exit()
                else:
                    messagebox.showinfo('Notificação', 'Produto comprado!')
                    self.visual.destroy()
        else:
            # print(f'nome pessoa = {self.noome.get()}\nproduto_requerido = {self.nome_produto}\nusuario = {self.un}\nsenha = {self.sn}\nlocal = {self.local.get()}\nobs = {self.obs.get()}\ndatahora = {sistem}')
            try:
                projeto.conexao.cadastro_pedido(self.noome.get(), self.nome_produto, self.un, self.sn, self.local.get(), self.obs.get())
                pedidos = projeto.conexao.registros_pedidos()
                for linhas in pedidos:
                    if self.noome.get() == linhas['nome_pessoa_pedido'] and self.nome_produto == linhas['produto_requerido'] and self.un == linhas['usuario'] and self.sn == linhas['senha'] and self.local.get() == linhas['localEntrega'] and self.obs.get() == linhas['observacoes']:
                        self.myid = linhas['id']
                        self.iddoproduto = int(self.treeview.selection()[0])
                projeto.conexao.cadastro_produto_pedidos(sistem, self.iddoproduto, self.myid)
            except Exception as erro:
                messagebox.showerror('Erro', f'Não foi possível se conectar ao banco de dados: {erro}')
                exit()
            else:
                messagebox.showinfo('Notificação', 'Produto comprado!')
                self.visual.destroy()



class Criacao():
    def __init__(self):
        self.tela = Tk()
        self.tela.configure(background='#fbb339')
        self.tela.title('Cadastro de um Novo Usuário')
        self.tela.geometry('340x300')
        self.tela.resizable(False, False)

        self.encapsular = Frame(self.tela, bg='#fbb339')
        self.encapsular.grid(row=0, column=0)

        Label(self.encapsular, font=('Century Gothic bold', 16), text='Usuário', bg='#fbb339', fg='white', padx=30, pady=10).grid(row=0, column=0)
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
        botao.HoverButton(self.encapsular, font=('Century Gothic bold', 16), text='Cadastrar', pady=5, padx=5, fg='white', bg='#d32016', command=self.back_end_user, activebackground='#1960a6', activeforeground='white').grid(row=4, column=1, pady=10, padx=30)

        self.tela.mainloop()

    def back_end_user(self):
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
            except:
                messagebox.showinfo('Erro', 'O campo sexo deve ser preenchido com [M/F]')
            else:
                if self.genero != 'M' and self.genero != 'F':
                    messagebox.showinfo('Erro', 'O campo sexo deve ser preenchido com [M/F]')
                else:
                    projeto.conexao.cadastro_user(self.n.get(), self.s.get(), self.genero, self.e.get())
                    self.tela.destroy()