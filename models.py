from app import db, app



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String)



	def __init__(self, id, username, email):
		self.id = id
		self.username = username
		self.email = email

	def __repr__(self) -> str:
		return f"Id=(id={self.id!r}, email_address={self.email_address!r})"

	def to_dict(self):
		return {"id": self.id, "username": self.username, "email":self.email}

with app.app_context():
	db.create_all()
