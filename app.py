'''
Created on 04-Sep-2019
@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
import pyodbc

from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    print("step1 ")  
   
    server = '192.168.1.189'
    database = 'TestDB'
    username = 'SA'
    password = 'Passw0rd$123'
    try: 
        #Connection String
        print("step2 ")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';port=1433;UID='+username+';PWD='+ password)
        print(connection)
        cursor = connection.cursor()
        print("step3 ")
        #Sample select query
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        print("step4 ")
        while row:
              print (row[0])
              row = cursor.fetchone()
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
    return 'Hello, world! v1'

if __name__ == '__main__':  # Script executed directly?
    print("Hello, World. Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
