from flask import Flask, app
from flask_restful import Api, Resource, reqparse
import sqlite3


app = Flask(__name__)
api = Api(app)

post_args = reqparse.RequestParser()
post_args.add_argument("badge", type=str, help="Bagde ID Number")
post_args.add_argument("fiscal_month", type=str, help="Fiscal Month")
post_args.add_argument("NT_login", type=str, help="NT_login")
post_args.add_argument("manager", type=str, help="manager")
post_args.add_argument("reason", type=str, help="reason")

get_args = reqparse.RequestParser()
get_args.add_argument("badge", type=str, help="Bagde ID Number")


class Stacks_Exceptions_Data(Resource):

    def post(self):
        con = sqlite3.connect('example1.db')
        cur = con.cursor()

        # cur.execute('''CREATE TABLE Stack_Exc
        #        (badge text, fiscal_month text, NT_login text, manager text, reason text)''')

        args = post_args.parse_args()

        cur.execute(
            "INSERT INTO Stack_Exc VALUES (?,?,?,?,?)", (args["badge"], args["fiscal_month"], args["NT_login"], args["manager"], args["reason"]))
        con.commit()
        con.close()

        return 201

    def get(self):
        con = sqlite3.connect('example1.db')
        cur = con.cursor()

        args = get_args.parse_args()

        cur.execute("SELECT * FROM Stack_Exc WHERE badge = :bdg",
                    {"bdg": args["badge"]})
        toReturn = cur.fetchone()
        con.close()

        return toReturn, 200


api.add_resource(Stacks_Exceptions_Data, "/")

if __name__ == "__main__":
    app.run(debug=True)
