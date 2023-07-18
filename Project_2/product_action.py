import sqlite3

cnt=sqlite3.connect("shop.db")

def get_product():
    sql='''SELECT * FROM product'''
    result=cnt.execute(sql)
    rows=result.fetchall()
    return rows


def get_single_product(id1):
    sql='''SELECT * FROM product WHERE id=?'''
    result=cnt.execute(sql,(id1,))
    row=result.fetchone()
    return row
    

def save_to_cart(pid,uid,qnt1):
    sql='''INSERT INTO cart (pid,uid,qnt)
            VALUES(?,?,?)'''
    cnt.execute(sql,(pid,uid,qnt1))
    cnt.commit()


def buy_cart():
    sql='''DELETE FROM cart WHERE qnt>0'''
    cnt.execute(sql)
    cnt.commit()
    

def update_product(id,pname,price,qnt):
    sql='''INSERT INTO product (id,pname,price,qnt)
            VALUES(?,?,?,?)'''
    cnt.execute(sql,(id,pname,price,qnt))
    cnt.commit()
