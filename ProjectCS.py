#!/usr/bin/env python
# coding: utf-8

# In[43]:


import psycopg2


# In[44]:


con = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="rbdelaa0615")


# In[45]:


#For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False


# In[51]:


try:
    cur = con.cursor()
    depot_headers = ["dep_id","addr", "Volume"]
    product_headers = ["prod_id", "pname", "price"]
    stock_headers = ["prod_id", "dep_id", "quantity_st"]
    q1=("select * from product")
    q2=("select * from depot")
    q3=("select * from stock")
    q4=('''INSERT INTO Product(prod_id, pname, price) VALUES ('p100', 'cd', 5)''')
    q5=('''INSERT INTO Stock(prod_id, dep_id, quantity_st) VALUES ('p100', 'd2', 50)''')
    
    
    cur.execute(q1)

    

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



    


# In[ ]:




