#%%
from cgitb import html
import mysql.connector
from IPython.display import HTML
import pandas as pd
def conn():
    con=mysql.connector.connect(host="localhost",user="root",password="Awhale", database="flask1")
    cur=con.cursor()
    return con,cur
def showdb():
    con,cur=conn()
    cur.execute("SELECT * from namedata")
    t_rows=cur.fetchall()
    df=pd.DataFrame(t_rows)
    

