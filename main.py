#!/usr/bin/env python3
import speedtest
import schedule
from datetime import datetime
import sqlite3
import os 
import pandas
import time



def get_speed():
    wifi = speedtest.Speedtest() # object that can be used for testing download and upload
   
    print("\nLoading Download Speed Using the Best Available Server...\n")
    wifi.get_servers() # get list of servers to test from 
    download_speed = wifi.download() # a function to get the download speed
    speed = int((download_speed / 1024 / 1024)*100)/ 100 # divid result by 1024 twice to get mega bit per second
    return(speed)


def db_record(dt_string,speed):
    db = sqlite3.connect('./speed.db')
    print('*** Database Connected ***')
    c = db.cursor()
    data = [dt_string, speed]
    sql_stat = 'INSERT INTO download_speed_table VALUES (?,?)'
    c.execute(sql_stat, data)
    db.commit()
    c.close()
    print('*** Committed Successfully ***')
    print('*** Closing Database Connection ***\n')

def db_connect(speed):
    # datetime object containing current date and time
    dt_now = datetime.now()  # using now function to get date and time now
    dt_string = dt_now.strftime("%Y-%m-%d %H:%M") # for formatting date and time

    if os.path.isfile('./speed.db'):
        db_record(dt_string,speed)
        return
    else:
        db = sqlite3.connect('./speed.db')
        print('*** Database Created ***')
        c = db.cursor()
        create_table = '''CREATE TABLE download_speed_table (Timestamp text, Speed text)'''
        c.execute(create_table)
        print('*** Speed DB Table Created ***')
        db.commit
        c.close
        db_record(dt_string,speed)

def show_records():
    db = sqlite3.connect('./speed.db')
    query = 'SELECT * FROM download_speed_table'
    result = pandas.read_sql_query(query, db)
    print(result)



def main():
    speed = get_speed()
    db_connect(speed)
    show_records()

if __name__ == "__main__":
    main()

schedule.every(2).hours.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
