import tkinter
import sqlite3
from users_actions import *
from product_action import *
# ==========================   login   =========================================================
login_strike=0
def login():
   global session
   global login_strike
   user=txt_user.get()
   pas=txt_pass.get()
   result=user_login(user,pas)
   if result:
      lbl_msg.configure(text="Welcome to your account!",fg="green")
      btn_login.config(state="disabled")
      txt_user.delete(0,"end")
      txt_pass.delete(0,"end")
      btn_logout.configure(state="active")
      btn_shop.configure(state="active")
      session=result
      
   if login_strike==2:
      btn_login.config(state="disabled")

   if user=="admin":
      lbl_msg.configure(text="Welcome Admin!!",fg="green")
      btn_login.config(state="disabled")
      btn_admin.config(state="active")
      txt_user.delete(0,"end")
      txt_pass.delete(0,"end")
      btn_logout.configure(state="active")
      btn_shop.configure(state="active")

  
   else:
      lbl_msg.configure(text="wrong username or password",fg="red")
      login_strike+=1


# ===============================  submit   ====================================================

def submit():
   user=txt_user.get()
   pas=txt_pass.get()
   result,errormsg=user_submit(user,pas)
   if result:
      lbl_msg.configure(text="submit done!",fg="green") 
   else:
      lbl_msg.configure(text=errormsg ,fg="red")  

# =============================   logout   ======================================================


def logout():
   btn_login.configure(state="active")
   btn_logout.configure(state="disabled")
   lbl_msg.configure(text="you are logged out",fg="blue")
   btn_shop.configure(state="disabled")
   btn_admin.config(state="disabled")

# ===========================   shop panel  ========================================================

def shop():

   def add_cart():
      pid=pidtxt.get()
      qnt=qnttxt.get()      
      if pid=="" or qnt=="":
         lbl_msg2.configure(text="FILL THE INPUTS !!!!",fg="red")
         return
      result=get_single_product(pid)

      if not result:
         lbl_msg2.configure(text="Wrong product Id",fg="red")
         return
      if int(qnt)>result[3]:
         lbl_msg2.configure(text="Not Enough Products",fg="red")
         return
      if int(qnt)<=0:
         lbl_msg2.configure(text="Cannot compely",fg="red")
         return
      
      save_to_cart(pid,session,qnt)
      lbl_msg2.configure(text="Add To Cart Successfully",fg="green")



   def buy():
      buy_cart()
      lbl_msg2.configure(text="Purches compeleted",fg="green")




   win_shop=tkinter.Toplevel(win)
   win_shop.geometry("400x400")
   win_shop.title("Shopping Panel")

   lst=tkinter.Listbox(win_shop,width=50)
   lst.pack()

   products=get_product()
   
   for product in products:
      text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]} "
      lst.insert("end",text)

   pidlbl=tkinter.Label(win_shop,text="ID= ")
   pidlbl.pack()
   
   pidtxt=tkinter.Entry(win_shop)
   pidtxt.pack()

   qntlbl=tkinter.Label(win_shop,text="QUANTITY= ")
   qntlbl.pack()
   
   qnttxt=tkinter.Entry(win_shop)
   qnttxt.pack()

   btn_add=tkinter.Button(win_shop,text="Add",command=add_cart)
   btn_add.pack()

   btn_buy=tkinter.Button(win_shop,text="Buy",command=buy)
   btn_buy.pack()

   lbl_msg2=tkinter.Label(win_shop,text="")
   lbl_msg2.pack()


   win_shop.mainloop()
# ==========================   admin panel   =========================================================

def admin_panel():
   def update():
      id=txt_id0.get()
      pname=txt_pname0.get()
      price=txt_price0.get()
      qnt=txt_qnt0.get()
   
      if id=="" or qnt=="" or pname=="" or price=="":
         lbl_msg3.configure(text="FILL THE INPUTS !!!!",fg="red")
         return
      result=update_product(id,pname,price,qnt)

   win_admin=tkinter.Toplevel(win)
   win_admin.geometry("400x400")
   win_admin.title("Admin Panel")
   
   lst=tkinter.Listbox(win_admin,width=50)
   lst.pack()

   products=get_product()
   
   for product in products:
      text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]} "
      lst.insert("end",text)
   

   lbl_id0=tkinter.Label(win_admin,text="ID")
   lbl_id0.pack()

   txt_id0=tkinter.Entry(win_admin)
   txt_id0.pack()

   lbl_pname0=tkinter.Label(win_admin,text="Name")
   lbl_pname0.pack()

   txt_pname0=tkinter.Entry(win_admin)
   txt_pname0.pack()

   lbl_price0=tkinter.Label(win_admin,text="Price")
   lbl_price0.pack()

   txt_price0=tkinter.Entry(win_admin)
   txt_price0.pack()

   lbl_qnt0=tkinter.Label(win_admin,text="Quantity")
   lbl_qnt0.pack()
   
   txt_qnt0=tkinter.Entry(win_admin)
   txt_qnt0.pack()

   lbl_msg3=tkinter.Label(win_admin,text="")
   lbl_msg3.pack()

   btn_update=tkinter.Button(win_admin,text="Update",command=update)
   btn_update.pack()



   win_admin.mainloop()


#=========================================================================================================================
session=""



win=tkinter.Tk()
win.geometry("300x300")


lbl_user=tkinter.Label(win,text="Username")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="Password")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()


lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()


btn_login=tkinter.Button(win,text="Login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="Submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="Logout",state="disabled",command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="Shop",state="disabled",command=shop)
btn_shop.pack()

btn_admin=tkinter.Button(win,text="Admin Panel",state="disabled",command=admin_panel)
btn_admin.pack()

win.mainloop()
