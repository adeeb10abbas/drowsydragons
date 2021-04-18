'''
Run this on the production server ONCE. 
It will create the database for you 
'''
from project import db, create_app
db.create_all(app=create_app())