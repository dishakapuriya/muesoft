import sqlite3

try:
    # Database Creation
    con=sqlite3.connect("moviesdb.db")
   
    # Table Creation
    con.execute("create table if not exists Movies (mname text, actor text, actress text, director text, yearofrelease integer)")

    print("Table Created Successfully..!")

except:
    print("Error in Database Creation..!!")


mname=input("Enter Movie Name:")
actor=input("Enter Lead Actor Name:")
actress=input("Enter Actress Name:")
director=input("Enter Director Name:")
yearofrelease=input("Enter Releas Year:")

# Data Insertation

con.execute("insert into Movies values(?,?,?,?,?)",(mname,actor,actress,director,yearofrelease))

# Data Fetch
result= con.execute("select * from Movies")
for i in result:
    print(i)