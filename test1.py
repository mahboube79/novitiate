from mysql.connector import connect,Error
x=input("enter vender mail: ")

# with connect(host="localhost",user="root",password="13799731m",database="db_hooma") as db:
#     myCursor=db.cursor()
#     myCursor.execute(f"select * from vender where marks='{x}'")
#     list1=myCursor.fetchall()
#     for vender in list1:
#         if(vender[4] == x):
#             print(vender)

        
        
        
with connect(host="localhost",user="root",password="13799731m",database="db_hooma") as db:
    myCursor=db.cursor()
    myCursor.execute("select * from vender where marks != 'NULL' ")
    list1=myCursor.fetchall()
    for vender in list1:
        if(vender[4] == x):
            print(vender)

     