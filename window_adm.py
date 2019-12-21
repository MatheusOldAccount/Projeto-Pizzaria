from tkinter import *
import projeto.conexao


class Window():
    def __init__(self):
        self.novajanela = Tk()
        self.novajanela.title('Administrador')
        projeto.conexao.registros_usuarios()
        Label(self.novajanela, text='AAAAA').grid(row=0, column=0)
        self.novajanela.mainloop()
