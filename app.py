import sys
from flask import Flask, url_for, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = "webstore.db"
# -------------helper functions-------#
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    print("RV: ", rv)
    cur.close()
    return (rv[0] if rv else None) if one else rv


# def log_the_user_in(username):
#     return render_template('profile.html', username=username)


def valid_login(email, password):
    user = query_db(
        "select * from user where email = ? and pwd = ?", [email, password], one=True
    )
    if user is None:
        return False
    else:
        return True


# function ends here-------#
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/abc", methods=["GET"])
def helloworl():
    return render_template("hello.html")


@app.route("/showSignUp")
def showSignUp():
    return render_template("signup.html")


# @app.route("/login", methods=["POST"])
# def login():
#     try:
#         email = request.form["email"]
#         pwd = request.form["inputPassword"]
#         conn = sqlite3.connect("webstore.db")
#         curs = conn.cursor()
#         curs.execute(
#             "SELECT * FROM user where email = {} AND pwd = {}".format(email, pwd)
#         )
#         user = list(curs.fetchone())
#         if user is None:
#             return render_template("signup.html")
#         return render_template("profile.html", username=email)
#     except Exception as e:
#         print(
#             "Error occured: {} at line {}".format(str(e), sys.exc_info()[1].tb_lineno)
#         )
#         msg = "error in login operation"


@app.route("/signup", methods=["POST"])
def signup():
    try:

        username = request.form["inputName"]
        email = request.form["inputEmail"]
        phone = request.form["inputPhone"]
        card = request.form["inputCard"]
        pwd = request.form["inputPassword"]

        conn = sqlite3.connect("webstore.db")
        conn.execute(
            "INSERT INTO user (name,email,phone,card,pwd) \
      VALUES ('{}', '{}', '{}','{}','{}' )".format(
                username, email, phone, card, pwd
            )
        )
        conn.commit()

        msg = "Record successfully added"
        print("Message is : {}".format(msg))

    except Exception as e:
        print(
            "Error occured: {} at line {}".format(str(e), sys.exc_info()[1].tb_lineno)
        )
        msg = "error in insert operation"

    finally:
        conn.close()
        return render_template("profile.html", username=username)


@app.route("/showLogin")
def showLogin():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    try:
        print("In login function...")
        error = None
        email = request.form["email"]
        password = request.form["inputPassword"]
        if valid_login(email, password):
            return render_template("profile.html", username=email)
        else:
            print("Invalid username pwd")
            error = "Invalid username/password"

        return render_template("login.html", error=error)
    except Exception as e:
        # msg = "error in Login operation"
        print("Error msg: ", str(e))
        return {"Error": str(e)}

    # finally:
    #    return render_template("result.html",msg = msg)
    #    con.close()


@app.route("/male")
def malePage():
    return render_template("male.html")


@app.route("/kids")
def kidsPage():
    return render_template("kids.html")


@app.route("/female")
def femalePage():
    return render_template("female.html")


@app.route("/contactPage")
def showcontactPage():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
