# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 00:47:09 2017

@author: ranveer
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:30:04 2017

@author: ranveer
"""
import	sqlite3
import pandas as pd

db = sqlite.connect('dbase1')
curs = db.cursor()
curs.execute('''DROP TABLE IF EXISTS customer''')
#sqlcmd = 'create table customer2 ( name char(2), rating float, comment char(500))'
#curs.execute(sqlcmd)	
        
        
def connect(dbase1): 
    """ Make connection to an SQLite database file """
    conn = sqlite.connect(dbase1)
    c = conn.cursor()
    return conn, c

def close(conn):
    """ Commit changes and close connection to the database """
    conn.commit()
    conn.close()

def See_rating() :
    db1 = sqlite.connect('dbase1')
    print(pd.read_sql_query("select * from restaurant", db1))
    
def Give_Rating() :   
    while True:
       
        try:
            conn	=	 sqlite.connect('dbase1')
            curs	=	conn.cursor()	
            curs.execute("INSERT INTO customer2 (name, rating,comment) values (?,?,?)", (Name,new_rating,comment))
            print("Record successfully Inserted ....!!!\n")
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
            print('********** Problem while Inserting records in table *********')
        finally:
            close(conn)
            
        
conn	=	 sqlite.connect('dbase1')
curs	=	conn.cursor()	
#tblcmd	= 'create table	restaurant (serial_no int(4) NOT NULL, res_name char(30), address char(10), phone_no int(10), no_of_visitors int(4), rating int(2) primary key (serial_no))'
#curs.execute(tblcmd)	
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (102, 'AZAD HIND', 'sector-2', 9878005691, 100, 4.6))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (103, 'THE SILVER SPOON', 'sector-3', 9868005621, 100, 4.2))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (104, 'CALIBER', 'sector-4', 9878005521, 100, 4.4))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (105, 'THE SILVER FORK', 'sector-5', 8978005631, 100, 3.5))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (106, 'MEHAK- E - PUNJAB', 'sector-1', 8578005621, 100, 3.5))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (107, 'CHOWMAN', 'sector-2', 8478005621, 100, 4.5))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (108, 'DOMINOS', 'sector-3', 8678005621, 100, 4.9))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (109, 'PIZZA HUT', 'sector-4', 8978005621, 100, 4.7))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (110, 'KFC', 'sector-5', 7878005621, 100, 4.3))
#curs.execute('insert into restaurant values (?, ?, ?, ?, ?, ?)', (111, 'RASOI', 'sector-1', 8878005621, 100, 4.5))
#print(pd.read_sql_query("select * from restaurant", conn))

print('=============================\n')
print('Welcome To Online Restaurant Rating System \n')
print('=============================\n')
print(' Please choose from the following option : ')
print()
while True:
	print('1. To See Rating \n' )
	print('2. To Give the Rating \n')
	print('3. To EXIT the program \n')

	choice = int(input("Please Enter your option : "))
	if choice == 1:
		See_rating()
	elif choice == 2:
         db1 = sqlite.connect('dbase1')
         print(pd.read_sql_query("select serial_no,res_name from restaurant",db1))
         print ('\n please select Restaurant serial no. in which you want to give Rating')
         A = input("serial n0 ---")
         print('=============================\n')
         print(' Welcome Sir/Madam  \n')
         print('=============================\n')
         conn	=	 sqlite.connect('dbase1')
         curs	=	conn.cursor()	    
         print('\n Please enter your detail : \n')
         Name = str(input("Mr./Mrs.")).upper()
         print ('\n please enter the Rating you want to give it')
         new_rating = float(input())
         conn	=	 sqlite.connect('dbase1')
         curs = conn.cursor()
         print ('please enter your comment on it')
         comment = str(input())
         conn	=	 sqlite.connect('dbase1')
         curs = conn.cursor()
         curs.execute("INSERT INTO customer2 values (?,?,?)", (Name,new_rating,comment))
        ## print(pd.read_sql_query("select res_name from restaurant WHERE serial_no = A",db1))
         print(pd.read_sql_query("select * from customer2",conn))
         #Give_Rating()
	elif choice == 3:
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")



