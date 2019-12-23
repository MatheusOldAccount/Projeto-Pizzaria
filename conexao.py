from tkinter import messagebox
import pymysql as database


def registros_usuarios():
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute('select * from usuario;')
            resultado = sql.fetchall()
    except:
        messagebox.showinfo('Erro', 'Não foi possível se conectar ao banco de dados')
        exit()
    else:
        return resultado


def cadastro_adm(nome, senha, sexo, endereco):
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute(f'insert into usuario values (default, "{nome}", "{senha}", "{sexo}", "2", "{endereco}");')
            conexao.commit()
    except Exception as erro:
        messagebox.showinfo('Erro', 'Não foi possível se conectar ao banco de dados')
        print(erro)
        exit()
    else:
        messagebox.showinfo('Notificação', f'Usuário {nome} cadastrado com sucesso !')


def registros_pedidos():
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute('select * from pedido;')
            result = sql.fetchall()
    except:
        messagebox.showinfo('Erro', 'Não foi possível se conectar ao banco de dados')
        exit()
    else:
        return result


def registros_pedidos_atuais():
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute('select pd.id, pd.data_hora, p.nome, ped.nome_pessoa_pedido from ProdutoPedidos pd join produto p on p.id = pd.id_produto join pedido ped on ped.id = pd.id_pedido;')
            query = sql.fetchall()
    except Exception as erro:
        messagebox.showinfo('Erro', f'Não foi possível se conectar ao banco de dados: {erro}')
        exit()
    else:
        return query


def deletar_produto(id):
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute(f'delete from ProdutoPedidos where id = {id}')
            conexao.commit()
    except Exception as erro:
        messagebox.showinfo('Erro', f'Não foi possível se conectar ao banco de dados: {erro}')
        exit()
    else:
        messagebox.showinfo('Notificação', f'Pedido deletado')


def registros_produtos():
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute('select * from produto;')
            r = sql.fetchall()
    except:
        messagebox.showinfo('Erro', 'Não foi possível se conectar ao banco de dados')
        exit()
    else:
        return r


def operations_products(nome, grupo, preco):
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute(f'insert into produto values (default, "{nome}", "{grupo}", "{preco}");')
            conexao.commit()
    except Exception as error:
        messagebox.showinfo('Erro', f'Não foi possível se conectar ao banco de dados: {error}')
        exit()
    else:
        messagebox.showinfo('Notificação', f'Produto {nome} cadastrado com sucesso!')

def delete_products(unique):
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute(f'delete from produto where id = {unique}')
            conexao.commit()
    except Exception as error:
        messagebox.showinfo('Erro', f'Não foi possível se conectar ao banco de dados: {error}')
        exit()
    else:
        messagebox.showinfo('Notificação', f'Produto excluído com sucesso!')


def truncate_products():
    conexao = database.connect(
        host='localhost',
        user='root',
        password='',
        db='projeto_db',
        charset='utf8mb4',
        cursorclass=database.cursors.DictCursor
    )

    try:
        with conexao.cursor() as sql:
            sql.execute(f'truncate table produto;')
            conexao.commit()
    except Exception as error:
        messagebox.showinfo('Erro', f'Não foi possível se conectar ao banco de dados: {error}')
        exit()
    else:
        messagebox.showinfo('Notificação', f'Todos produtos foram excluídos com sucesso!')
