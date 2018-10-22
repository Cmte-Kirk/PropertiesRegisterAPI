import pymysql
import sys
from Connect import connect


def insert_imovel(imovel):
    conn = connect()
    try:
        id = 0
        with conn.cursor() as cursor:
            sql =  "insert into Imovel (Nome, Endereco, Descricao, Status, Caracteristicas, Tipo, Finalidade, IdImobiliaria) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            finalidade = imovel.finalidade if imovel.finalidade != '' else None
            values = (imovel.nome, imovel.endereco, imovel.descricao, imovel.status, imovel.caracteristicas, imovel.tipo, finalidade, imovel.id_imobiliaria)
            cursor.execute(sql, values)
            id = cursor.lastrowid
        conn.commit()
        return id
    except Exception as e:
        return 0
    finally:
        conn.close()

def update_imovel(imovel):
    conn = connect()
    try:
        with conn.cursor() as cursor:
            sql =  "update Imovel set Nome = %s, Endereco = %s, Descricao = %s, Status = %s, Caracteristicas = %s, Tipo = %s, Finalidade = %s, IdImobiliaria = %s where id = %s"
            values = (imovel.nome, imovel.endereco, imovel.descricao, imovel.status, imovel.caracteristicas, imovel.tipo, imovel.finalidade, imovel.id_imobiliaria, imovel.id)
            cursor.execute(sql, values)
        conn.commit()
        return imovel.id
    except:
        return 0
    finally:
        conn.close()

def delete_imovel(id):
    conn = connect()
    try:
        with conn.cursor() as cursor:
            sql =  "delete from Imovel where id = %s"
            values = (id)
            cursor.execute(sql, values)
        conn.commit()
        return id
    except:
        return 0
    finally:
        conn.close()

def list_imovel(id = 0, nome = None):
    conn = connect()
    try:
        lst = []
        with conn.cursor() as cursor:
            sql =  "select Id, Nome, Endereco, Descricao, Status, Caracteristicas, Tipo, Finalidade, IdImobiliaria from Imovel"
            if id > 0:
                sql = sql + " where Id = {0}".format(id)
            elif nome:
                sql = sql + " where Nome like '%{0}%'".format(nome)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
        for row in cursor._rows:
            imovel = {
                'id': row[0], 
                'nome': row[1], 
                'endereco': row[2], 
                'descricao': row[3], 
                'status': row[4], 
                'caracteristicas': row[5], 
                'tipo': row[6], 
                'finalidade': row[7], 
                'id_imobiliaria': row[8]
            }                
            lst.append(imovel)
        return lst
    except:
        return None
    finally:
        conn.close()