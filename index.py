from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "uname": "Abhinav",
        "age": 18,
        "password" : "Abhinav123",
        "branch" : "Computer Science",
        "hostel" : "M111"
    },
    {
        "uname": "Bavesh",
        "age": 18,
        "password" : "Bavesh123",
        "branch" : "Computer Science",
        "hostel" : "M112"
    },
    {
        "uname": "Jeethendra",
        "age": 18,
        "password" : "Jeethendra123",
        "branch" : "Civil",
        "hostel" : "M113"
    },

    {
        "uname" : "Chaitanya",
        "age" : 18,
        "password" : "Chaitanya123",
        "branch" : "Aeronutical",
        "hostel" : "M114"
    }
]

class User(Resource):

    # This method is used to login

    def get(self, uname,password):
        for user in users:
            if(uname == user["uname"] and password == user["password"]):
                return "Logged in as {}.".format(user["uname"]), 200
            elif(uname == user["uname"] and password != user["password"]):
                return "Password incorrect."
        return "User not found", 404

    #Used to add a new user

    def post(self, uname, password, age, branch, hostel):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("branch")
        parser.add_argument("password")
        parser.add_argument("hostel")

        for user in users:
            if(uname == user["uname"]):
                return "User with name {} already exists".format(uname), 400

        user = {
            "uname": uname,
            "age": age,
            "branch": branch,
            "hostel" : hostel,
        }
        users.append(user)
        return user, 201
    
    #Used to get the details of a user

    def put(self, uname):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("branch")
        parser.add_argument("password")
        parser.add_argument("hostel")

        for user in users:
            if(uname == user["uname"]):
                return ("""Name : {}   Age : {}  Branch : {}  Hostel Block : {}""".format(str(user["uname"]), str(user["age"]), str(user["branch"]), str(user["hostel"]))), 200
        
        

    #Used to delete an existing user.

    def delete(self, uname, password):
        global users
        for user in users:
            if uname == user["uname"]:
                users = [user for user in users if user["uname"] != uname]
                return "{} is deleted.".format(uname), 200
            else:
                return "No user exists with the username {}.".format(uname)            

api.add_resource(User, "/user/<string:uname>/<string:password>/<string:branch>/<string:age>/<string:hostel>","/user/<string:uname>/<string:password>/<string:branch>/<string:age>", "/user/<string:uname>/<string:password>", "/user/<string:uname>/admin")


app.run(debug=True)