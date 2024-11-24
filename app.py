from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Grocery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return redirect('/vhod')
    else:
        return render_template('login.html')

@app.route('/vhod')
def vhod():
    return render_template('vhod.html')

@app.route('/infopost')
def infopost():
    return render_template('infopost.html')


@app.route('/zakazi')
def zakazi():
    return render_template('zakazi.html')

@app.route('/index', methods=['GET'])
def index():
    groceries = Grocery.query.all()
    return render_template('index.html', groceries=groceries)

@app.route('/add', methods=['GET', 'POST'])
def add_grocery():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        weight = float(request.form['weight'])
        quantity = float(request.form['quantity'])
        price = request.form['price']
        groceries = Grocery(name=name, description=description, weight=weight, quantity=quantity, price=price)
        db.session.add(groceries)
        db.session.commit()
        return redirect('/index')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_grocery(id):
    grocery = Grocery.query.get_or_404(id)
    if request.method == 'POST':
        grocery.name = request.form['name']
        grocery.description = request.form['description']
        grocery.weight = float(request.form['weight'])
        grocery.quantity = float(request.form['quantity'])
        grocery.price = request.form['price']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', grocery=grocery)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_grocery(id):
    patient = Grocery.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)





