from flask import Flask, render_template, jsonify

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

@app.route('/api/dashboard-data')
def dashboard_data():
    data = {
        "sales": {"value": 1200, "change": "+15.27%"},
        "orders": {"value": 236, "change": "+5.5"},
        "customers": {"value": 800, "change": "+11.02"},
        "profits": {"value": 12000, "change": "+7.5"},
        "out_of_stock": [
            {
                "name": "Paracetamol Tablets IP",
                "desc": "FRIZIUM 550 - CIPLA",
                "batch": "F102",
                "expires": "12/12/25",
                "image": "/static/images/medicine1.png"
            }
        ],
        "expiring_soon": [
            {
                "name": "Paracetamol Tablets IP",
                "desc": "FRIZIUM 550 - CIPLA",
                "batch": "F102",
                "expires": "12/12/25",
                "image": "/static/images/medicine1.png"
            }
        ]
    }
    return jsonify(data)

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
