from flask import Flask, render_template, request, flash, render_template_string, redirect, Response
import psycopg2
import json
import os


port = int(os.environ.get('PORT', 5000))


dbhost = 'ec2-54-216-17-9.eu-west-1.compute.amazonaws.com'
dbname = 'djrs2mt5np83b'
dbuser = 'womlylvmxosadm'
dbport = '5432'
dbpass = '300cba31baa710789df66e6dbda88f1183d92462e00f8c92ff44687a27ac601c'
con = psycopg2.connect(dbname=dbname, port=dbport, user=dbuser, password=dbpass, host=dbhost)
con.set_session(autocommit=True)
cur = con.cursor()









app = Flask(__name__)



@app.route("/getBook/<id>", methods=["POST", "GET"])
def getBook(id):

    cur.execute(f'select * from books where id={id}')
    book = cur.fetchall()

    if book:
        book = book[0]
        data = {
            'id': book[0],
            'title': book[1],
            'author': book[2],
            'year': book[3],
            'description': book[4]
        }

        return json.dumps(data), 200

    else:
        return {'library': 'book not found'}, 404




@app.route("/getBookList", methods=["POST", "GET"])
def getBookList():

    cur.execute(f'select * from books')
    books = cur.fetchall()
    print(books)
    data = []

    if books:
        for book in books:
            data.append(
                {
                    'id': book[0],
                    'title': book[1],
                    'author': book[2],
                    'year': book[3],
                    'description': book[4]
                }
            )

            return json.dumps(data), 200

    else:
        return {'library': 'library is empty'}, 404

app.run(threaded=True,host='0.0.0.0', port=port)
#app.run(debug=True, host='localhost', port=5001)
