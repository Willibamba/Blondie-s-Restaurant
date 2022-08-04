import os 

# Imports libraries, functions and database
from flask import Flask, flash, render_template, redirect, request, session
from flask_session import Session
from functools import wraps
from mailer import Mailer
import sqlite3

# Configure app
app = Flask(__name__)

# Configure Templates to auto-rload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connects the database 
db = sqlite3.connect("database.db", check_same_thread=False)
con = db.cursor()


# Configure session 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure Mail settings
mail = Mailer(email=os.environ["EMAIL"], password=os.environ["PASSWORD"])
mail.settings(provider=mail.MICROSOFT)


# The route to the homepage  
@app.route("/")
def home():
    return render_template("index.html")

# The route to the menu page 
@app.route("/menu")
def menu():
    return render_template("menu.html")

# The route to the submit for form and store data in the database
@app.route("/order", methods=["GET", "POST"])
def order():
    
    
    if request.method == "POST":
        name = request.form.get("name")
        contact_number = request.form.get("contact_number")
        people = request.form.get("people")
        address = request.form.get("address")
        message = request.form.get("message")

        # Checks if form fields are filled and print error massage
        error = None
        if not name:
            error = "Please fill in the Name"
        elif not contact_number:
            error = "Please fill in the Contact number"
        elif not people:
            error = "Please fill in the amount of People"
        elif not address:
            error = "Please fill in the Address"
        elif not message:
            error = "Please fill in the Message"
        else:
            # Store customer data into the database 
            con.execute("INSERT INTO ORDERS (name, contact_number, people, address, message) VALUES (?, ?, ?, ?, ?)", (name, contact_number, people, address, message))
            db.commit()

            # Send email notification of orders
            mail.send(receiver=os.environ["EMAIL"], subject="New Order", message="You have a new order!")
            
            # Validate confirmation
            return render_template("successful_order.html")
        return render_template("order.html", error=error)

    else:
        return render_template("order.html")

# The login required function
def login_required(f):

    # Decorates route to require login
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Route for the query data of orders 
@app.route("/orders")
@login_required
def orders():   

    # Updates the orders and bookings made
    con.execute('SELECT name, contact_number, people, address, message, time FROM ORDERS ORDER BY time DESC')
    Orders = con.fetchall()
  
    return render_template("orders.html", Orders=Orders)

# The route to the About page
@app.route("/about")
def about():
    return render_template("about.html")

# The route to the Login page
@app.route("/login", methods=["GET", "POST"])
def login():

    # Clear any user
    session.clear()

    # Declare a variable for error messages 
    error = None

    if request.method == "POST":
        
        # Fetch username and password from the database
        con.execute("SELECT username FROM users")
        username = con.fetchone()
        con.execute("SELECT password FROM users")
        password =con.fetchone()

        # Checks if the username and password match is in the database and prints error message
        if request.form.get("username") != username[0] or request.form.get("password") != password[0]:
            error = "Invalid username and/or password"

            return render_template("login.html", error=error)

        # If match is found establish session and redirects to orders page
        else:
            session["user_id"] = username[0]
        
        return redirect("/orders")
        

    else:
        return render_template("login.html")

# Route to logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



