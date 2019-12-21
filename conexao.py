from tkinter import messagebox


def registros_usuarios():
    import pymysql as database

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
        print(resultado)


registros_usuarios()
