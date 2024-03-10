import sqlite3

def import_db(df):
    conn = sqlite3.connect('dbc.db')
    cursor = conn.cursor()
    

    #finalized table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS finalized_table (
        Tweet TEXT,
        Tweet_result TEXT
    )
    ''')

    for index, row in df.iterrows():
        cursor.execute('''
            INSERT INTO finalized_table VALUES (?, ?)
        ''', tuple(row))


    conn.commit()
    conn.close() 
