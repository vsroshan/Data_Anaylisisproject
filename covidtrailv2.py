#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Project Title: Covid- Analytics 2.0
# importing required Packages


from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing Mysql connector package
import mysql.connector

from tkinter import messagebox 

# Creating Main Screen- Home Page

master = Tk() 
master.geometry('350x350')
master.title("Welcome to Covid-19 Analysis Project")
#canvas = Canvas(width=900, height=100,bg='#F6CE76')
canvas = Canvas(width=250, height=500,bg='white')
canvas.pack(side=TOP,expand=YES, fill=BOTH)
gif1 = PhotoImage(file='homescreen.png')

#canvas.create_image(500,100, image=gif1, anchor=NW)
canvas.create_image(200,3, image=gif1, anchor=NW)
pane = Frame(master,background="white") 
pane.pack(fill=BOTH)

#Creating Function for showing Description about the Project

def clickabout():
    master.destroy()
    global about1
    about1= Tk() 
    about1.geometry('350x350')
    about1.title("About Our Project Analytics 2.0")
    canvas = Canvas(width=250, height=500, bg='#EAD7C0')
    canvas.pack(expand=YES,fill=BOTH)
    gif5 = PhotoImage(file='about.png')
    canvas.create_image(200,3,image=gif5,anchor=NW)
     
    pane = Frame(about1) 
    pane.pack(fill=BOTH)
    about = Button(pane, text = "Proceed",background = "mediumvioletred", fg = "white", font=("Arial Bold", 20),command=loginscreen)
    about.pack(side = TOP,expand = True,fill=BOTH)
    #about.pack(side = TOP, expand = True, fill = BOTH)
    #about.pack(side = TOP, expand = True)
    mainloop()
#creating Login Screen

def loginscreen():
    about1.destroy()
    global tkWindow
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Login Form')

#username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name")
    usernameLabel.pack()
    usernameEntry = Entry(tkWindow) 
    usernameEntry.pack()

#password label and password entry box
    passwordLabel = Label(tkWindow,text="Password")
    passwordLabel.pack()
    passwordEntry = Entry(tkWindow, show='*')
    passwordEntry.pack()


#login button
    
    def validateLogin():
        
#Retrieving details entered in username and password textbox      

     user=usernameEntry.get()
     pwd=passwordEntry.get()
        
#Establishing connection with Mysql Database

     mydb = mysql.connector.connect(host="localhost", user="root",passwd="1234",database="covid")
     mycursor = mydb.cursor()
     sql = "Select * from users where uname=%s and pwd= %s"
     val = (user, pwd)
     mycursor.execute(sql, val)
     result=mycursor.fetchall()
        
#checking Validity of details entered with database Record      
    
     if(int(mycursor.rowcount)==1):
# if it is valid user call the clicked function to show menu screen
       clicked() 
     else:
#Message box showing the user to enter valid details
    
       messagebox.showerror("Invalid Values", "Enter valid Username and Password ")  
        
    loginButton = Button(tkWindow, text="Login", command=validateLogin)
    loginButton.pack()
    mainloop()
   
def clicked():
    tkWindow.destroy()
    master1 = Tk() 
    master1.geometry('800x800')
    master1.title("Visualizing the impact of  Covid-19")
    pane1 = Frame(master1) 
    pane1.pack(fill=BOTH)
    
#Analyis #1   

    def click1():
        
#Displaying Top 5 mostly affected countries    
# info1=['USA','India','Brazil','France','Russia']
# data1=[11789012,9095806,6020164,2071499,2064748]


#Reading details from csv file containing top 5 mostly affected countries
    
     top5= pd.read_csv("top5.csv",names=['country','data'],skiprows=1,nrows=5)
     info1=top5.country
     data1=top5.data        
     fig1=plt.figure(figsize=(9, 2))
     plt.bar(info1,data1,color=['#2CBDFE','#47DBCD','blue','#9D2EC5','pink','#661D98','cyan','#F5B14C','orange','#00FF00'])
     plt.xlabel('Countries')
     plt.ylabel('Confirmed Cases')
     plt.title('TOP 5 MOSTLY AFFECTED COUNTRIES AS ON 22.11.2020', weight='bold')
     plt.show()
     fig1.savefig('top5.png', bbox_inches='tight', dpi=150)
     gif1 = PhotoImage(file='top5.png')
     canvast.delete(ALL)   
     canvast.create_image(40, 40, image=gif1, anchor=NW)    
     mainloop() 
    
#button to display Top 5 Most Affected Countries     
    
    b1 = Button(pane1, text = "Top 5 Most Affected Countries",  
            background = "red", fg = "white",font=("Arial Bold", 20),command=click1) 
    b1.pack(side = TOP, expand = True, fill = BOTH) 

#Analyis #2

    def click2():
        
#info2=['USA','Brazil','India','Mexico','UK']
#data2=[258333,168141,132223,100104,53775]
#Displaying Top 5 most Testing done countries  

      testmost= pd.read_csv("testing.csv",names=['country','data'],skiprows=1,nrows=5)
      info2=testmost.country
      data2=testmost.data 
      fig2=plt.figure(figsize=(7, 2))
      plt.bar(info2,data2,color=['#2CBDFE','#47DBCD','blue','#9D2EC5','pink','#661D98','cyan','#F5B14C','orange','#00FF00'])
      plt.title('Top 5 Most Testing done Countries', weight='bold')
      plt.ylabel('Total Tests / Total Population')
      plt.xlabel('Country')
      fig2.savefig('mosttestingdone.png', bbox_inches='tight', dpi=150)
      gif2 = PhotoImage(file='mosttestingdone.png')
      canvast.delete(ALL)  
      canvast.create_image(40, 40, image=gif2, anchor=NW)    
      mainloop()  
    
#button to display Top 5 Most Covid -19 Testing done Countries

    b2 = Button(pane1, text = "Top 5 Most Covid -19 Testing done Countries", 
            background = "blue", fg = "white",font=("Arial Bold", 20),command=click2) 
    b2.pack(side = TOP, expand = True, fill = BOTH) 
 
#Analysis 3
    def click3():  
#info3=['Maharashtra','Karnataka','AP','TamilNadu','Kerala']
#data3=[1774455,871342,861092,768340,557441]
#Displaying Top 5 mostly affected countries    
       topstates= pd.read_csv("topstates.csv",names=['states','data'],skiprows=1,nrows=5)
       info3=topstates.states
       data3=topstates.data 
       fig3=plt.figure(figsize=(7,2), dpi=80)
       plt.bar(info3,data3,color=['#2CBDFE','#47DBCD','blue','#9D2EC5','pink','#661D98','cyan','#F5B14C','orange','#00FF00'])
       plt.ylabel('Number of Confirmed Cases')
       plt.xlabel('States/UnionTerritory')
       plt.title('States with maximum confirmed cases', weight='bold')
       fig3.savefig('top5statesconfirmed.png', bbox_inches='tight', dpi=150)
       gif3 = PhotoImage(file='top5statesconfirmed.png')
       canvast.delete(ALL)   
       canvast.create_image(100, 40, image=gif3, anchor=NW)    
       mainloop() 
    
#button to display Top 5 states in India - Confirmed covid cases

    b3 = Button(pane1, text = "Top 5 states in India - Confirmed covid cases", 
            background = "green", fg = "white",font=("Arial Bold", 20),command=click3) 
    b3.pack(side = TOP, expand = True, fill = BOTH) 
    
#Analysis # 4 

    def click5():
#info5=['Chennai','Coimbatore','Chengalpatu','Thiruvallur','Salem']
#data5=[211555,47380,46717,40265,29199]
#Displaying Top 5 mostly affected districts in TamilNadu   
     topdistrict= pd.read_csv("topdistrict.csv",names=['District','data'],skiprows=1,nrows=5)
     info5=topdistrict.District
     data5=topdistrict.data    
     fig5=plt.figure(figsize=(7,2), dpi=80)
     plt.bar(info5,data5,color=['#2CBDFE','#47DBCD','blue','#9D2EC5','pink','#661D98','cyan','#F5B14C','orange','#00FF00'])
     plt.title("Top 5 Mostly Affected Districts in TamilNadu", weight='bold')
     fig5.savefig('top5districts.png', bbox_inches='tight', dpi=150)
     gif5 = PhotoImage(file='top5districts.png')
     canvast.delete(ALL)  
     canvast.create_image(100, 40, image=gif5, anchor=NW)    
     mainloop()   
    
#button to display Top 5 mostly affected districts in TamilNadu   

    b5 = Button(pane1, text = "Top 5 Mostly Affected Districts in TamilNadu", 
            background = "orange", fg = "white",font=("Arial Bold", 20),command=click5) 
    b5.pack(side = TOP, expand = True, fill = BOTH) 

    canvast = Canvas(width=150, height=800, bg='GREY')
    canvast.pack(expand=YES, fill=BOTH)   

#Analyis #5

    def click4():
     #info4=['USA','Brazil','India','Mexico','UK']
     #data4=[258333,168141,132223,100104,53775]
        
     topdeath= pd.read_csv("topdeath.csv",names=['Country','data'],skiprows=1,nrows=5)
     info4=topdeath.Country
     data4=topdeath.data      
     fig4=plt.figure(figsize=(3,3), dpi=80)
     plt.bar(info4,data4,color=['#2CBDFE','#47DBCD','blue','#9D2EC5','pink','#661D98','cyan','#F5B14C','orange','#00FF00'])
     plt.title("Top 5 Countries with Maximum Death Rate", weight='bold')
     fig4.savefig('top5countrydeath.png', bbox_inches='tight', dpi=150)
     gif4 = PhotoImage(file='top5countrydeath.png')
     canvast.delete(ALL)  
     canvast.create_image(40, 40, image=gif4, anchor=NW)    
     mainloop()   
    
#button to display Maximum Death Covid Cases Details

    b4 = Button(pane1, text = "Top 5 Countries with Maximum Death covid cases", 
            background = "black", fg = "white",font=("Arial Bold", 20),command=click4) 
    b4.pack(side = TOP, expand = True, fill = BOTH) 
b1 = Button(pane, text = "Proceed !",  
            background = "hotpink", fg = "white", font=("Arial Bold", 20),command=clickabout) 

b1.pack(side = TOP, expand = True)

mainloop()



# In[ ]:





# In[ ]:





# In[ ]:




