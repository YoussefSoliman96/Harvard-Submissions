import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol",
        user_id,
    )
    cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_db[0]["cash"]

    return render_template("index.html", database=transactions_db, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Must choose a symbol", 400)
        if not shares or not shares.isdigit():
            return apology("Must insert amount of shares", 400)

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Stock not available", 400)

        if int(shares) < 0:
            return apology("Invalid input for shares", 400)

        transaction_cost = int(shares) * stock["price"]
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_money = user_cash_db[0]["cash"]

        if user_money < transaction_cost:
            return apology("Cash unavailable", 400)

        money_after_transaction = user_money - transaction_cost
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", money_after_transaction, user_id
        )

        date = datetime.datetime.now()

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
            user_id,
            stock["symbol"],
            shares,
            stock["price"],
            date,
        )

        flash(f"Bought {shares} of {symbol} for {usd(transaction_cost)}!")
        flash(f"Balance: {usd(money_after_transaction)}!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute(
        "SELECT * FROM transactions WHERE user_id = ?", user_id
    )
    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol.upper())
        if not stock:
            return apology("Must choose a symbol", 400)
        if stock == "None":
            return apology("Stock not available", 400)
        else:
            return render_template(
                "quoted.html",
                name=stock["name"],
                price=stock["price"],
                symbol=stock["symbol"],
            )

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        elif not confirmation:
            return apology("must confirm password", 400)

        if password != confirmation:
            return apology("password and confirmation don't match")

        hash_password = generate_password_hash(password)
        # Query database for username
        try:
            user = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username,
                hash_password,
            )
        except:
            return apology("Username taken")
        # Remember which user has logged in
        session["user_id"] = user

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        select_symbol = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )
        return render_template(
            "sell.html", symbols=[row["symbol"] for row in select_symbol]
        )
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if not symbol:
            return apology("Must choose a symbol")

        stock = lookup(symbol.upper())

        if stock == "None":
            return apology("Stock not available")

        if shares < 0:
            return apology("Invalid input for shares")

        transaction_cost = shares * stock["price"]
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_money = user_cash_db[0]["cash"]

        user_shares = db.execute(
            "SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
            user_id,
            symbol,
        )
        current_user_shares = user_shares[0]["shares"]
        if shares > current_user_shares:
            return apology("Shares unavailable")

        money_after_transaction = user_money + transaction_cost
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", money_after_transaction, user_id
        )

        date = datetime.datetime.now()

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
            user_id,
            stock["symbol"],
            (-1) * shares,
            stock["price"],
            date,
        )

        flash(f"{shares} Shares sold successfully! for {usd(transaction_cost)}")
        flash(f"Balance: {usd(money_after_transaction)}!")
        return redirect("/")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add Cash"""
    if request.method == "POST":
        user_id = session["user_id"]
        new_cash = float(request.form.get("new_cash"))
        if not new_cash:
            return apology("Invalid amount")

        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_money = user_cash_db[0]["cash"]

        money_after_transaction = user_money + new_cash
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", money_after_transaction, user_id
        )

        return redirect("/")
    else:
        return render_template("add.html")
