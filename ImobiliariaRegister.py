import pymysql
import sys
from Connect import connect


def insert_imobiliaria(imobiliaria):
    conn = connect()
    try:
        id = 0
        with conn.cursor() as cursor:
            sql =  "insert into Imobiliaria (Nome, Endereco) values (%s, %s)"
            values = (imobiliaria.nome, imobiliaria.endereco)
            cursor.execute(sql, values)
            id = cursor.lastrowid
        conn.commit()
        return id
    except:
        return 0
    finally:
        conn.close()

def update_imobiliaria(imobiliaria):
    conn = connect()
    try:
        with conn.cursor() as cursor:
            sql =  "update Imobiliaria set Nome = %s, Endereco = %s where id = %s"
            values = (imobiliaria.nome, imobiliaria.endereco, imobiliaria.id)
            cursor.execute(sql, values)
        conn.commit()
        return imobiliaria.id
    except:
        return 0
    finally:
        conn.close()

def delete_imobiliaria(id):
    conn = connect()
    try:
        with conn.cursor() as cursor:
            sql =  "delete from Imobiliaria where id = %s"
            values = (id)
            cursor.execute(sql, values)
        conn.commit()
        return id
    except:
        return 0
    finally:
        conn.close()

def list_imobiliaria(id = 0, nome = None):
    conn = connect()
    try:
        lst = []
        with conn.cursor() as cursor:
            sql =  "select Id, Nome, Endereco from Imobiliaria"
            if id > 0:
                sql = sql + " where Id = {0}".format(id)
            elif nome:
                sql = sql + " where Nome like '%{0}%'".format(nome)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
        for row in cursor._rows:
            imobiliaria = {
                'id': row[0], 
                'nome': row[1], 
                'endereco': row[2]
            }                
            lst.append(imobiliaria)
        return lst
    except:
        return 0
    finally:
        conn.close()