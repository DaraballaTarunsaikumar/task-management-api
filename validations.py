import re
email_pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
symbol="!@#$%^&*"
def required(required_fields,data):
    for field in required_fields:
        if field not in data:
            return {
                "Message":f"{field} is missing"
            },400
        if not isinstance(data[field],str):
            return {
                "Message":f"{field} must be string"
            },400
        if not data[field].strip():
            return {
                "Message":f"{field}  must not  be empty"
            },400
    return None
def email_validation(email):
    if not  re.match(email_pattern,email):
        return {
            "Message":"Invalid Email Pattern"
        },400
    return None
def password_validation(password):
    if len(password)<8:
        return {
            "Message":"Password must contain at least 8 characters"
        },400
    if not any(ch.isupper() for ch in password):
        return {
            "Message":"Password must  contain at least one upper character"
        },400
    if not any(ch.islower() for ch in password):
        return {
            "Message":"Password must  contain at least one lower letter"
        },400
    if not any(ch.isdigit() for ch in password):
        return {
            "Message":"Password must contain at least one digit"
            
        },400
    if not any(ch in symbol for ch in password):
        return {
            "Message":"Password must contain at least one symbol"
        },400
    return None
list_status=["pending","in_progress","completed"]
def status_check(status):
    if status not in list_status:
        return {
            "Message":"Invalid Status"
        },400
    return None   
        
