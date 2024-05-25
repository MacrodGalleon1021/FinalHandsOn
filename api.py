from flask import Flask, make_response, jsonify, request

import pymysql

app = Flask(__name__)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "macrod"
app.config["MYSQL_DB"] = "sampledb"

def get_connection():
    return pymysql.connect(
        host="localhost",
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        db=app.config["MYSQL_DB"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
@app.route("/")
def hello_world():
    return "<p> HELLO WORLD!</p>"

@app.route("/branches", methods=["GET"])
def get_branches():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM branches"
            cursor.execute(query)
            data = cursor.fetchall()

        return make_response(jsonify(data), 200)
    finally:
        connection.close()
        
@app.route("/branches/<int:branch_id>", methods=["GET"])
def get_branch_by_id(branch_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM branches WHERE branch_id = %s"
            cursor.execute(query, (branch_id,))
            data = cursor.fetchone()

        if data:
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({"error": "branch not found"}), 404)
    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=True)