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
        self.screen = Tk()
        self.screen.configure(background='#fbb339')
        self.screen.title('Interface do Usuário')
        self.screen.geometry('630x600')

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

        botao.HoverButton(self.screen, font=('Century Gothic bold', 16), text='Comprar Produto', pady=5, padx=5, fg='white', bg='#d32016', activebackground='#810e07', width=20, activeforeground='white').grid(row=3, column=0, pady=10, padx=30)
        botao.HoverButton(self.screen, font=('Century Gothic bold', 16), text='Voltar', pady=5, padx=5, fg='white', bg='#d32016', activebackground='#810e07', width=20, activeforeground='white', command=self.sair).grid(row=3, column=1, pady=10, padx=30)

        self.screen.mainloop()

    def sair(self):
        self.screen.destroy()
        import projeto.main as inicial
        inicial.Principal()



class Criacao():
    def __init__(self):
        self.tela = Tk()
        self.tela.configure(background='#fbb339')
        self.tela.title('Cadastro de um Novo Usuário')
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