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
    server = '192.168.1.189'
    database = 'master'
    username = 'SA'
    password = 'Passw0rd$123'

    #Connection String
    connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = connection.cursor()

    #Sample select query
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
          print (row[0])
          row = cursor.fetchone()

    return 'Hello, world!'

if __name__ == '__main__':  # Script executed directly?
    print("Hello, World. Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
