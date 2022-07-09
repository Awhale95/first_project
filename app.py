
from distutils.log import debug
from flask import Flask, request, render_template
import mysql.connector
import datab
app = Flask(__name__, template_folder="templates")

def conn():
    con=mysql.connector.connect(host="localhost",user="root",password="Awhale", database="flask1")
    cur=con.cursor()
    return con,cur

@app.route('/', methods=['GET','POST'])

def hello_world():
    if request.method =='POST':
        fname=request.form.get("fname")
        lname=request.form.get("lname")
        con,cur=conn()
        query="INSERT INTO namedata(name,address) VALUES (%s,%s)"
        cur.execute (query,(fname,lname))
        con.commit()
        con.close()
        cur.close()
        show_d=datab.showdb()
        return ("you")
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)