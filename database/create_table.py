from database.connect_db import create_connection

def create_tables():
    
        con = create_connection()
        cur = con.cursor()

        
        con.commit()
        
        print("Tables created successfully.")
    
                                                                       