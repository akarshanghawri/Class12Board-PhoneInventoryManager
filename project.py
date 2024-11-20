import mysql.connector
mydb = mysql.connector.connect(host ="localhost",database ="project",user ="root",passwd ="clgws123")
mycursor = mydb.cursor()

import datetime                         #for taking input of the date 

#background functions
# auto generator 
def phone_id_gen() :
    sql = "select phone_id_g from auto_generator"
    mycursor.execute(sql)
    x = mycursor.fetchone()
    sql_update = "update auto_generator set phone_id_g = phone_id_g + 1"
    mycursor.execute(sql_update)
    mydb.commit()
    return x[0] 

def customer_id_gen() :
    sql = "select customer_id_g from auto_generator"
    mycursor.execute(sql)
    x = mycursor.fetchone()
    sql_update = "update auto_generator set customer_id_g = customer_id_g + 1"
    mycursor.execute(sql_update)
    mydb.commit()
    return x[0] 

def order_id_gen() :
    sql = "select order_id_g from auto_generator"
    mycursor.execute(sql)
    x = mycursor.fetchone()
    sql_update = "update auto_generator set order_id_g = order_id_g + 1"
    mycursor.execute(sql_update)
    mydb.commit()
    return x[0] 

def bill_id_gen() :
    sql = "select bill_id_g from auto_generator"
    mycursor.execute(sql)
    x = mycursor.fetchone()
    sql_update = "update auto_generator set bill_id_g = bill_id_g + 1"
    mycursor.execute(sql_update)
    mydb.commit()
    return x[0] 

#additional functions
     
#quantity
#when order is placed run the function to change the quantity
def quantity_update(phone_id) :
    try:       
        sql = "select quantity from inventory where phone_id = %s"
        mycursor.execute(sql,(phone_id,))
        x = mycursor.fetchone()
        current_quantity = x[0]
        if current_quantity >= 0:
            new_quantity = current_quantity - 1
            sql_update = "update inventory set quantity = %s where phone_id = %s"
            mycursor.execute(sql_update, (new_quantity, phone_id))
            mydb.commit()
            print(f"quantity changed to: {new_quantity}")
        else:
            print("out of stock")
            
    except :
        print("enter correct phone id")
        
   
#price
def discount_price(phone_id): 
    try :    
        sqlprice =  "select price from inventory where phone_id=%s"
        mycursor.execute(sqlprice, (phone_id,))
        y = mycursor.fetchall()
        x = int(y[0][0])
        print("Old price:",x)
        discount = int(input("enter discount to be added without percentage sign:"))
        update_price = x-(discount/100)*x 
        sql_update = "update inventory set price = %s where phone_id = %s"
        mycursor.execute(sql_update,(update_price,phone_id))      
        mydb.commit()
        print("new price :",update_price)
    except :
       print("enter correct phone id")
       
# INSERTING RECORDS
def insert_inventory() :
    phone_id = phone_id_gen()
    print("phone id: ",phone_id)
    model = input("Enter model name: ")
    brand = input("Enter brand name: ")
    storage_capacity = int(input("Enter storage(in GB): "))
    quantity = int(input("Enter no. of phones in stock: "))
    color = input("Enter color: ")
    price = int(input("Enter price: "))
    date_added = datetime.datetime(int(input("enter year:")),int(input("enter month:")),int(input("day")))  
    temp = (phone_id,model,brand,storage_capacity,quantity,color,price,date_added)    
    sql = "INSERT INTO inventory VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,temp)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")

def insert_customer():
    customer_id = customer_id_gen()
    print("customer id:",customer_id)
    first_name =  input("enter first name:")    
    last_name =  input("enter last name:")  
    email = input("enter your email address:")
    phone_no =  int(input("enter your phone no:"))
    temp =  (customer_id,first_name,last_name,email,phone_no)    
    sql = "INSERT INTO customer VALUES(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,temp)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")
   
def insert_order():
    try :
        order_id = order_id_gen()
        print("order id :",order_id)
        
        model = input("enter model :")
        sql = "select phone_id from inventory where model = %s"
        mycursor.execute(sql,(model,))
        phone_id = mycursor.fetchone()
        print("phone id :",phone_id[0])
        
        order_date = datetime.datetime(int(input("enter year:")),int(input("enter month:")),int(input("enter today's date:")))
        
        sql = "select total_amount from inventory where model = %s"
        mycursor.execute(sql,(model,))
        total_amount = mycursor.fetchone()
        
        payment_status = input("Enter payment_status(cancelled,paid,unpaid): ")
        temp = (order_id,model,phone_id,order_date, total_amount, payment_status)
        sql = "INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,temp)
        mydb.commit()
        print(mycursor.rowcount, "order record inserted")
        
        quantity_update(phone_id)    #quantity updated automatically after every buy 
        
    except :
        print("model out of stock")
        
insert_order()
   
def insert_bill():
    # auto bill_id
    order_id = int(input("Enter order_id: "))
    model = input("enter model name :")
    total_amount = int(input("Enter total_amount: "))
    payment_date = datetime.datetime(int(input("enter year:")),int(input("enter month:")),int(input("day")))
    temp = (order_id,model,total_amount, payment_date)
    sql = "INSERT INTO bill VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,temp)
    mydb.commit()
    print(mycursor.rowcount, "bill record inserted")
   
#MODIFYING RECORDS
def modify_inventory() :                                
    phone_id =  int(input("enter phone_id:"))
    sql = "select * from inventory where phone_id=%s"%(phone_id,)
    mycursor.execute(sql)
    rec = mycursor.fetchall()
    print("old values",rec)    
    print("enter new values :")
    model = input("Enter model name: ")
    brand = input("Enter brand name: ")
    storage_capacity = int(input("Enter storage(in GB): "))
    color = input("Enter color: ")  
    temp = (model,brand,storage_capacity,color)
    sql = "update inventory set model=%s,brand=%s,storage_capacity=%s color=%s,date_added=%s where phone_id=%s"
    mycursor.execute(sql,temp)
    print(mycursor.rowcount,"record updated")
    mydb.commit()
    
def modify_customer() :                                
    customer_id =  int(input("enter customer_id:"))
    sql = "select * from customer where customer_id=%s"%(customer_id,)
    mycursor.execute(sql)
    rec = mycursor.fetchall()
    print("old values",rec)    
    print("enter new values :")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter new email: ")
    phone_no = int(input("Enter new phone no.: "))
    temp = (first_name,last_name,email,phone_no)       #problem
    sql = "update customer set first_name=%s, marks=%s where rollno=%s" #incomplete
    mycursor.execute(sql,temp)
    print(mycursor.rowcount,"record updated")
    mydb.commit()
    
#DELETING RECORDS
def del_inventory() :
    phone_id =  int(input("enter phone_id:"))
    sql = "delete from inventory where phone_id=%s"%(phone_id,)
    print(sql)
    mycursor.execute(sql)
    print(mycursor.rowcount,"record deleted")
    
def del_customer() :
    customer_id =  int(input("enter customer_id:"))
    sql = "delete from customer where customer_id=%s"%(customer_id,)
    print(sql)
    mycursor.execute(sql)
    print(mycursor.rowcount,"record deleted")
    
def del_orders() :
    order_id =  int(input("enter order_id:"))
    sql = "delete from inventory where order_id=%s"%(order_id,)
    print(sql)
    mycursor.execute(sql)
    print(mycursor.rowcount,"record deleted")

#Functions for menu options
def display_menu():
    print("Inventory Management System Menu:")
    print("1. Insert Inventory")
    print("2. Modify Inventory")
    print("3. Delete Inventory")
    print("4. Insert Customer")
    print("5. Modify Customer")
    print("6. Delete Customer")
    print("7. Insert Order")
    print("8. Exit")

#Main menu loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        insert_inventory()
    elif choice == '2':
        modify_inventory()
    elif choice == '3':
        del_inventory()
    elif choice == '4':
        insert_customer()
    elif choice == '5':
        modify_customer()
    elif choice == '6':
        del_customer()
    elif choice == '7':
        insert_order()
    elif choice == '8':
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")