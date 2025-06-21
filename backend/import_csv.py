import csv
import pymysql
import os
import time

time.sleep(10)

conn = pymysql.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    db=os.environ['DB_NAME'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn:
    with conn.cursor() as cursor:
        with open('titanic_full_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute("""
                    INSERT INTO titanic (
                        id, pclass, survived, pname, sex, age, sibsp, parch,
                        ticket, fare, cabin, embarked, boat, body, homedest
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                """, (
                    row['id'], row['pclass'], row['survived'], row['pname'], row['sex'],
                    row['age'] or None, row['sibsp'], row['parch'], row['ticket'], row['fare'] or None,
                    row['cabin'], row['embarked'], row['boat'], row['body'] or None, row['homedest']
                ))
    conn.commit()
