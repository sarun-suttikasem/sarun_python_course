""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

"""

def create_user_profile(username, age=18, premium=False):
    if premium == True:
        return f"{username} {age} are Premium user "
    else:
        return f"{username} {age} are Standard user "

print(create_user_profile("Sarun", 19, True))