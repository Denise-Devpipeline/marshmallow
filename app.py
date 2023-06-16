from flask import Flask, request, jsonify
from organizations import Users, users_schema, user_schema
import os #talk directly to computer
from flask_marshmallow import Marshmallow
import marshmallow as ma
from users import Users



database_uri = os.environ.get("DATABASE_URI")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")
database_name = 'marshmallow'

app = Flask(__name__)


#enviroment Variables in square brackets
app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_uri}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
    with app.app_context():
        print("Creating Tables")
        db.create_all()
        print("All done.")

@app.route("/users/get", methods=['GET'])
def get_all_orgs():
    orgs = db.session.query(Users).filter(Users.active == True).all()
    if not orgs:
        return jsonify("There is no user by that ID"), 404
    else:
        return jsonify(users_schema.dump(orgs)), 200


@app.route("/users/get/<id>", methods=['GET'])
def get_all_orgs_by_id():
    orgs = db.session.query(Users).filter(Users.active == True).all()
    if not orgs:
        return jsonify("That user does not exist"), 404
    else:
        return jsonify(users_schema.dump(orgs)), 200   

# user_schema = UsersSchema()
# users_schema = UsersSchema(many=True)


if __name__ == "__main__":
    create_all()
    app.run(port="8086", host="0.0.0.0", debug=True)

