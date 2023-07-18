import sqlite3

cnt=sqlite3.connect("shop.db")

##====================== create "name" table ========================
# sql='''CREATE TABLE product(
#         id INTEGER PRIMARY KEY,
#         pname CHAR(15) NOT NULL,
#         price INTEGER NOT NULL,
#         qnt INTEGER
#         )'''

# cnt.execute(sql)
# print("table has been created!!")


##-============================= insert data into table =========================

# sql='''INSERT INTO product(pname,price,qnt)
#         VALUES("PC","56000","15")'''

# cnt.execute(sql)
# cnt.commit()
# print("data inserted")

##-============================= insert (more) data into table =========================


# user1=input("username: ")
# pas1=input("password: ")
# addr1=input("address: ")
# score1=int(input("score: "))

# sql='''INSERT INTO users(user,pass,addr,score)
#         VALUES(?,?,?,?)'''

# cnt.execute(sql,(user1,pas1,addr1,score1))
# cnt.commit()

#============================== fetch data ========================
# sql='''SELECT * FROM users WHERE addr="rasht"'''    ## THE * SELECTS ALL DATA ##
# result=cnt.execute(sql)
# rows=result.fetchall()
# print(rows)

# addr=input("address: ")
# sql="SELECT user,pass FROM users WHERE addr=?"
# result=cnt.execute(sql,(addr,))
# rows=result.fetchall()
# print(rows)


# user=input("username: ")
# pas=input("password: ")
# sql="SELECT * FROM users WHERE user=? and pass=?"

# result=cnt.execute(sql,(user,pas))
# rows=result.fetchall()
# print(rows)

#====================== update tabl ===========================
# sql='''UPDATE users SET score=20 WHERE user="admin" '''

# cnt.execute(sql)
# cnt.commit()

#====================== delete record ==========================
# sql='''DELETE FROM users WHERE user="reza" '''

# cnt.execute(sql)
# cnt.commit()

#======================sub structur==========================
#user=input("enter username: ")
#user="%"+user+"%"
#sql='''SELECT * FROM users WHERE user LIKE ? '''

#result=cnt.execute(sql,(user,))
#rows=result.fetchall()
#print(rows)



##======================create cart table========================
# sql='''CREATE TABLE cart(
#         ID INTEGER PRIMARY KEY,
#         uid INTEGER NOT NULL,
#         pid INTEGER NOT NULL,
#         qnt INTEGER NOT NULL
#         )'''

# cnt.execute(sql)
# print("table has been created!!")
