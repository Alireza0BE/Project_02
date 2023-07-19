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

  

def update_product(pname,price,qnt):
    sql='''INSERT INTO product (pname,price,qnt)
            VALUES(?,?,?)'''
    cnt.execute(sql,(pname,price,qnt))
    cnt.commit()



def update_quantity_of_products(qnt,pid):
    result=get_single_product(pid)
    lst=list(result)
    x=lst[3] - int(qnt)

    sql=''' UPDATE product SET qnt=? WHERE id=? '''
    cnt.execute(sql,(x,pid))
    cnt.commit()
    print ("database has been updated !!!")
