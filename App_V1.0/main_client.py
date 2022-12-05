from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')





@app.route('/about.html')
def about():
    return render_template('about.html')






@app.route('/product.html')
def product():
    return render_template('product.html')


#config db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'ms_database'

mysql = MySQL(app)

@app.route('/order_place.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        orderDetails = request.form
        Client_code = orderDetails['Client_code']
        Client_name = orderDetails['Client_name']
        Consignee = orderDetails['Consignee']
        Order_quantity = orderDetails['Order_quantity']
        Order_status = orderDetails['Order_status']
        Order_date = orderDetails['Order_date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO order_details(Client_code, Client_name, Consignee, Order_quantity, Order_status, Order_date) VALUES(%s, %s, %s, %s, %s, %s)",(Client_code, Client_name, Consignee, Order_quantity, Order_status, Order_date))
        mysql.connection.commit()
        cur.close()
        return render_template('success_msg.html')
    return render_template('order_place.html')




@app.route('/all_details.html')
def all_details():
    cur = mysql.connection.cursor()
    result=cur.execute("SELECT * FROM order_details")
    if result>0:
        orderDetails = cur.fetchall()
        return render_template('all_details.html', orderDetails=orderDetails)

    

    

@app.route('/order_status.html', methods=['GET', 'POST'])
def search():
    if request.method == 'POST' :
        result=request.form
        Client_code = result['Client_code']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM order_details where Client_code = '{}' ".format(Client_code))
        searchDetails = cur.fetchall()

        mysql.connection.commit()
        cur.close()
        return render_template('order_status.html', searchDetails = searchDetails)
    return render_template('order_status.html')









if __name__=='__main__':
    app.run(debug=True)