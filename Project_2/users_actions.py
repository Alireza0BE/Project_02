import sqlite3

cnt=sqlite3.connect("shop.db")

def user_login(user,pas):
   sql='''SELECT * FROM users WHERE user=? and pass=?'''
   result=cnt.execute(sql,(user,pas))
   rows=result.fetchall()
   if len(rows)<1:
      return False
   else:
      return rows[0][0]

def user_submit(user,pas):
  if len(pas)<8:
   return False,"password length error!"
    
  if pas.isalpha() or pas.isdigit():
    return False,"password combination error!"
    
  sql=''' SELECT * FROM users WHERE user=?'''
  result=cnt.execute(sql,(user,))
  rows=result.fetchall()
  if len(rows)>0:
    return False,"username already exist!"
  
  sql='''INSERT INTO users (user,pass) VALUES (?,?)'''
  cnt.execute(sql,(user,pas))
  cnt.commit()
  return True,""


