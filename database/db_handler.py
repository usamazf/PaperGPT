"""PaperGPT database handler module."""

import sqlite3
import multiprocessing

class DatabaseHandler:
    
    # create a mutex lock since DB calls can happen
    # from different processes
    __lock = multiprocessing.Lock()

    def __init__(self) -> None:
        self.conn = sqlite3.connect("test.db")
        self.curr = self.conn.cursor()
        # create tables if they done already exist
        self.db_lock()
        self.curr.execute("CREATE TABLE IF NOT EXISTS APPROVED_PAPERS(serial INTEGER PRIMARY KEY AUTOINCREMENT, title, publish_date, abstract, pdflink, author, entry_date, source, gpt_summary)")
        self.curr.execute("CREATE TABLE IF NOT EXISTS GPT_SUMMARIZED(serial INTEGER PRIMARY KEY AUTOINCREMENT, title, publish_date, abstract, pdflink, author, entry_date, source, gpt_summary)")
        self.curr.execute("CREATE TABLE IF NOT EXISTS RAW_SCRAPE(serial INTEGER PRIMARY KEY AUTOINCREMENT, title, publish_date, abstract, pdflink, author, entry_date, source)")
        self.db_unlock()

    def db_lock(self) -> None:
        type(self).__lock.acquire()
    
    def db_unlock(self) -> None:
        type(self).__lock.release()
    
    def insert_raw(self, data: list[tuple]) -> None:
        self.db_lock()
        self.curr.executemany("INSERT INTO RAW_SCRAPE VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
        self.db_unlock()
        
    def insert_gpt(self, data: list[tuple]) -> None:
        self.db_lock()
        self.curr.executemany("INSERT INTO GPT_SUMMARIZED VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
        self.db_unlock()
        
    def insert_approve(self, data: list[tuple]) -> None:
        self.db_lock()
        self.curr.executemany("INSERT INTO APPROVED_PAPERS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()
        self.db_unlock()