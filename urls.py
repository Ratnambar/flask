from app import app, api
from index import UserCreations, UsersList


api.add_resource(UserCreations, '/user/create')
api.add_resource(UsersList, '/users')

if __name__ == '__main__':
    app.run(debug=True)