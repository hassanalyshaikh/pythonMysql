import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import mysql.connector

#Database connection with Mysql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
database="bahriare_bra"
)
#mysql Query using python

mycursor = mydb.cursor()
select_employee=mycursor.execute("SELECT count(*) as cnt, ta.reqid, tbl.id,`date_apply` FROM tblapply ta RIGHT join `tblrequis` tbl ON ta.reqid= tbl.id GROUP BY date_apply limit 50,55")
myresult = mycursor.fetchall()

for x in myresult:
      df=pd.DataFrame(print(x), columns=list('ABC'))
      xaxis= (x[0])
      yaxis=(matplotlib.dates.date2num(x[3]))
      yaxis=(matplotlib.dates.num2date(yaxis))
      plt.bar(yaxis,xaxis)
      plt.title("Number of Cvs aginst ech job")
      plt.xlabel("Date")
      plt.ylabel("CV Count")
plt.show()
