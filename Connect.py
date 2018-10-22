import pymysql
import sys


#REGION = 'us-east-1'

rds_host  = "localhost"
name = "root"
password = ""
db_name = "imoveis"

def connect():
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)    
    return conn

