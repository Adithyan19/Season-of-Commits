from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/notification')
def notification():
    return render_template('notification.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

if __name__ == '__main__':
    app.run(debug=True)
