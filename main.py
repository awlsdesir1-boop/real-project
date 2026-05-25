from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import sqlite3
#opens database and creates if it does not yet exist 
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()#cursor is used to execute sql commands


cursor.execute("""CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
height REAL,
weight REAL,
age INTEGER,
goal TEXT)
"""
)
#saves database changes
conn.commit()
#instance of fastapi
app = FastAPI()

class UserMetrics(BaseModel):
    height: float
    weight: float
    age: int
    goal: str


#path 
#http://127.0.0.1:8000
@app.get("/")
def root():
    return {"Backend created hooray!"}

users =[]

#endpoint to recieve metrics from user
@app.post("/metrics")
def Recieve_Metrics(metrics: UserMetrics):
    print("recieved metrics",{metrics})

    #acessing individual metrics
    UserHeight = metrics.height
    UserWeight = metrics.weight
    UserAge = metrics.age
    UserGoal = metrics.goal


    #saving data into database
    cursor.execute("""
    INSERT INTO USERS(height,weight,age,goal)
    VALUES(?,?,?,?)
    """
    (
    UserHeight,
    UserWeight,
    UserAge,
    UserGoal
    ))
    #save database changes
    conn.commit()

    #currently just returning a message
    #will later be used to pass data into ai prompt generator 
    return{
        "status": "success",
        "message": "metrics recieved and saved successfully"
    }



#used to retrieve data fom database

@app.get("/users")
def GetUsers():

    #get all rows form users table
    cursor.execute("SELECT * FROM users")
    #store query results
    users =cursor.fetchall()

    #send data to front end
    return{
        "users":users
    }

#need odin to add this so that backend and frontend are connected 
""" fetch("http://127.0.0.1:8000/test")
  .then(res => res.json())
  .then(data => {
    console.log(data.message);
  });
 """

""" flow:
fontend uses fetch
request Sent 
backend returns json 
frontend recieves data """
