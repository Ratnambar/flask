
from flask import Flask, jsonify, request
from flask_restful import Resource
from app import db
from models import User




# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String, unique=True, nullable=False)
# 	email = db.Column(db.String)

# 	def __init__(self, id, username, email):
# 		self.id = id
# 		self.username = username
# 		self.email = email

# 	def __repr__(self) -> str:
# 		return f"Id=(id={self.id!r}, email_address={self.email_address!r})"

# 	def to_dict(self):
# 		return {"id": self.id, "username": self.username, "email":self.email}

# with app.app_context():
# 	db.create_all()



# @app.route("/users/create", methods=["GET","POST"])
class UserCreations(Resource):
	def post(self):
		if request.method == "POST":
			user = User(
				id = request.form["id"],
				username = request.form["username"],
				email = request.form["email"])
			db.session.add(user)
			db.session.commit()
			return jsonify({"message":"user created"})


class UsersList(Resource):
	def get(self):
		users = db.session.execute(db.select(User).order_by(User.username)).scalars()
		data = [user.to_dict() for user in users]
		return jsonify(data=data)
