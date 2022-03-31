from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'mydata'
mysql = MySQL(app)



@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO register VALUES(%s,%s,%s,%s,%s)''',(username,password,fname,lname,email))
        mysql.connection.commit()
        cursor.close()
    return render_template('register.html')


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO login VALUES(%s,%s)''',(username,password))
        mysql.connection.commit()
        cursor.close()
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact',methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        messege = request.form.get('messege')
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO contact VALUES(%s,%s,%s)''',(name,contact,messege))
        mysql.connection.commit()
        cursor.close()
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug = True)