from flask import Blueprint,request
from db import conn,cursor
from validations import required,email_validation,password_validation
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
users=Blueprint("users",__name__)
@users.route("/users/register",methods=["POST"])
def register():
    data=request.get_json(silent=True)
    if data is None:
        return {
            "Message":"Data Must be json"
        },400
    required_fields=["username","email","password"]
    field_error=required(required_fields,data)
    if field_error:
        return field_error
    username=data["username"].strip()
    email=data["email"].strip().lower()
    email_error=email_validation(email)
    if email_error:
        return email_error
    password=data["password"]
    password_error=password_validation(password)
    if password_error:
        return password_error
    try:
        hashed_password=generate_password_hash(password)
        cursor.execute("""SELECT email FROM users wHERE email=%s""",(email,))
        user=cursor.fetchone()
        if user is not None:
            return {
                    "Message":"Email is already existed"
                },409
        cursor.execute("""INSERT INTO users(username,email,password) VALUES (%s,%s,%s)""",(username,email,hashed_password))
        conn.commit()
        return {
            "Message":"User registered Successfully"
        },201
    except Exception as e:
        conn.rollback()
        print(e)
        return {
            "Message":"Database error"
        },500

@users.route("/users/login",methods=["POST"])
def login():
    data=request.get_json(silent=True)
    if data is None:
        return {
            "Message":"Data Must Be json"
        },400
    required_fields=["email","password"]
    field_error=required(required_fields,data)
    if field_error:
        return field_error
    email=data["email"].strip().lower()
    email_error=email_validation(email)
    if email_error:
        return email_error
    password=data["password"]
   
    try:
        cursor.execute(""" SELECT * FROM users WHERE email=%s""",(email,))
        user=cursor.fetchone()
        if user is None:
            return {
                "Message":"Invalid email or password"
            },401
        if check_password_hash(user[3],password):
            access_token=create_access_token(identity=str(user[0]))
            return{
                "Message":"User login Successfully",
                "access_token":access_token
            },200
        return{
            "Message":"Invalid Email or password"
        },401
    except Exception as e:
        print(e)
        return {
            "Message":"Database error"
        },500
