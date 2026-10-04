from flask import Blueprint,request
from db import conn,cursor
from validations import required,status_check
from flask_jwt_extended import jwt_required,get_jwt_identity
tasks=Blueprint("tasks",__name__)

@tasks.route("/tasks",methods=["POST"])
@jwt_required()
def task():
    users_id=get_jwt_identity()
    data=request.get_json(silent=True)
    if data is None:
        return {
            "Message":"Data Must Be Json"
        },400
    required_field=["title","description","status"]
    field_error=required(required_field,data)
    if field_error:
        return field_error
    status=data["status"].lower()
    status_error=status_check(status)
    if status_error:
        return status_error
    try:
        cursor.execute(""" INSERT INTO tasks (user_id,title,description,status )VALUES (%s,%s,%s,%s) """,(users_id,data["title"],data["description"],status))
        conn.commit()
        return {
            "Message":"Task Created Successfully"
        },201
    except Exception as e:
        conn.rollback()
        print(e)
        return {
            "Message":"Database error"
        },500
@tasks.route("/tasks",methods=["GET"])
@jwt_required()
def get_task():
    users_id=get_jwt_identity()
    try:
        cursor.execute("SELECT * FROM tasks WHERE user_id=%s ",(users_id,))
        tasks=cursor.fetchall()
        if not tasks:
            return {
                "Message":f" There is no task "
            },200
        task_list=[]
        for task in tasks:
            user_task={
                "id":task[0],
                "user_id":task[1],
                "title":task[2],
                'description':task[3],
                "status":task[4],
                "created_at":task[5]
                }
            task_list.append(user_task)
            
        return task_list,200
    except Exception as e:
        print(e)
        return {
            "Message":"Database error"
        },500      
@tasks.route("/tasks/<int:task_id>",methods=["GET"]) 
@jwt_required()  
def get_task_by_id(task_id):
    users_id=get_jwt_identity()
    try:
        cursor.execute("SELECT * FROM tasks WHERE id=%s AND user_id=%s",(task_id,users_id))
        task=cursor.fetchone()
        if task is None:
            return {
                "Message":"The user_id have no tasks"
            },404
        return {
            "id":task[0],
            "user_id":task[1],
            "title":task[2],
            "description":task[3],
            "status":task[4],
            "created_at":task[5]
        },200
    except Exception as e:
        print(e)
        return {
            "Message":"Database error"
        },500
@tasks.route("/tasks/<int:task_id>",methods=["PUT"])
@jwt_required()
def update_tasks(task_id):
    users_id=get_jwt_identity()
    data=request.get_json(silent=True)
    if data is None:
        return {
            "Message":"Data Must Be json"
        },400
    required_fields=["status"]
    field_error=required(required_fields,data)
    if field_error:
        return field_error
    status=data["status"].lower()
    status_error=status_check(status)
    if status_error:
        return status_error
    try:
        cursor.execute("UPDATE tasks SET status=%s WHERE id=%s AND user_id=%s",(status,task_id,users_id))
        if cursor.rowcount>0:
          conn.commit()
          return {
            "Message":"Task Updated successfully"
          },200
        return {
            "Message":"Task Not Found"
        },404
    except Exception as e:
        print(e)
        return {
            "Message":"Database error"
        },500
@tasks.route("/tasks/<int:task_id>",methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    users_id=get_jwt_identity()
    try:
        cursor.execute("DELETE FROM tasks WHERE id=%s AND user_id=%s",(task_id,users_id))
        if cursor.rowcount>0:
           conn.commit()
           return {
            "Message":"Task Deleted Successfully"
          },200
        return {
            "Message":"Task Not Found"
        },404
        
    except Exception as e:
        print(e)
        return {
            "Message":"Database Error"
        },500
    
    