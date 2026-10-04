from flask import Flask
from routes.user_routes import users
from routes.tasks_routes import tasks
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(tasks)
app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
jwt=JWTManager(app)
if __name__=="__main__":
    app.run(debug=True)