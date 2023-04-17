import traceback

import pymysql

dados = []
conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='senac@123',
                                    database='classicmodels',
                                    charset='utf8mb4',
                                    port=6556,
                                    cursorclass=pymysql.cursors.DictCursor)


def listarDoacao():
    try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM customers")
            result = cur.fetchone()
            for i in result:
                print(i)
    except:
        print("Erro ao tentar listar doacoes")
    finally:
        conn.close()
listarDoacao()
