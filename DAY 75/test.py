#importing the necessary libraries
from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import mysql.connector

def create_sqlalchemy_engine():
    engine=create_engine('mysql+pymysql://root:@localhost/ai_project_db')
    return engine

def create_connection():
    connection=mysql.connector.connect(
    hostname="localhost",
    user="root",
    password="",
    database="ai_project_db"
    )
    return connection

def setup_database():
    connection=create_connection()
    cursor=connection.cursor()
    
    #create the query for if the database is not exist
    cursor.execute('CREATE DATABASE IF NOT EXIST ai_project_db')
    
    cursor.execute("USE ai_project_db")
    
    cursor.execute("""CREATE TABLE IF NOT EXIST 
                   dataset(
                       id INT AUTO_INCREMENT
                       PRIMARY KEY,
                       feature1 FLOAT,
                       feature2 FLOAT,
                       label INT
                   )""")
    connection.commit()
    cursor.close()
    connection.close()
    
    #fetch data
    def fetch_data():
        engine=create_sqlalchemy_engine()
        query = "SELECT * FROM dataset"
        df = pd.read_sql(query, engine)
        return df
    
    def train_model(df):
        x = df[['feature1', 'feature2']]
        y = df['label']
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
        
        model = DecisionTreeClassifier()
        model.fit(x_train, y_train)
        
        predictions = model.predict(x_test)
        return predictions 
    
    #store the predictions 
    def store_predictions(predictions):
        connection = create_connection()
        cursor = connection.cursor()
        
        #query for inserting
        cursor.execute("CREATE TABLE IF NOTE EXISTS predictions(id INT, prediction INT)")
        
        for i, pred in enumerate(predictions):
            cursor.execute("INSERT INTO predictions(id,prediction) VALUES(%s,%s), (i+1, int(pred))")
            
            
            connection.commit()
            cursor.close()
            connection.close()
            
    def insert_sample_data():
         data = [
             (1.5,2.5,0),
             (2.5,4.5,0),
             (2.0,3.1,1),
             (1.8,2.9,0),
             (1.1,2.1,1),
             
         ]    
         
         
         connection =  create_connection()
         cursor = connection.cursor()
         
         cursor.executemany("INSERT INTO dataset(feature1,feature2, label) VALUES(%s,%s,%s)", data)
         connection.commit()
         cursor.close()
         connection.close()
            
    def main():
        setup_database()
        insert_sample_data()
        
        
        df = fetch_data()
        predictions = train_model(df)
        print("predictions: ", predictions)
        store_predictions(predictions)
        
    if __name__ == "__main__":
        main()
        