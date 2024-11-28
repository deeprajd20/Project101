import psycopg2
import json
class user_model:
    def __init__(self):
        try:
           
            self.conn = psycopg2.connect(
                database="test_database", user='postgres', password='root', host='127.0.0.1', port= '5432'
                )
            self.cur = self.conn.cursor()
            print("Connection established")

        except:
            print("Coneection Failed")

    def sql_query(self):
        self.cur.execute("SELECT * FROM public.tab")
        result = self.cur.fetchall()
        return json.dumps(result)
