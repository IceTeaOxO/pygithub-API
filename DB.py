import sqlite3

#data type
# data = [
#     ('John', 'ProjectA', 'https://github.com/john/projecta', 10, 20, '2022-04-17', '/path/to/readme1'),
#     ('Jane', 'ProjectB', 'https://github.com/jane/projectb', 30, 40, '2022-04-16', '/path/to/readme2'),
#     ('Bob', 'ProjectC', 'https://github.com/bob/projectc', 50, 60, '2022-04-15', '/path/to/readme3')
# ]

class GithubDB:
    def __init__(self,dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
    def create_table(self,table_name):
        create_query = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                            AuthName TEXT,
                            RepoName TEXT,
                            URL TEXT,
                            Issues INTEGER,
                            Stars INTEGER,
                            UpdateDate TEXT,
                            ReadmePath TEXT,
                            Language TEXT,
                            PRIMARY KEY (AuthName,RepoName)
                          )'''
        self.cursor.execute(create_query)
        
        
    # def insert_data(self,table_name,data):
    #     insert_query = f'''INSERT INTO {table_name} (AuthName, RepoName, URL, Issues, Stars, UpdateDate, ReadmePath, Language) 
    #                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    #     self.cursor.executemany(insert_query, data)
    #     self.conn.commit()
    def insert_data(self, data):
        for row in data:
            self.cursor.execute("INSERT OR IGNORE INTO github (AuthName, RepoName, URL, Issues, Stars, UpdateDate, ReadmePath, Language) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row)
        self.conn.commit()
    
    def select_data(self,table_name,fields=None,condition=None,limit=10,offset=0):
        if fields is None:
            fields = ['*']
        select_query = f'''SELECT {", ".join(fields)} FROM {table_name}'''
        if condition is not None:
            select_query += f' WHERE {condition} '
        select_query += f' LIMIT {limit} OFFSET {offset};'
        # print(select_query)
        self.cursor.execute(select_query)
        return self.cursor.fetchall()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def clear_table(self,table_name):
        self.cursor.execute('''DELETE FROM {}'''.format(table_name))
        self.conn.commit()
        



#清空資料庫
# db = GithubDB('github.db')
# db.clear_table('github')


# print((db.select_data('github',limit=5,offset=0)))


# dbfile = "github.db"
# conn = sqlite3.connect(dbfile)

# cursor = conn.cursor()

# #建立table
# tableName = "github"
# create_table_sql = f'''CREATE TABLE IF NOT EXISTS {tableName} 
# (ID INTEGER PRIMARY KEY AUTOINCREMENT,
# AuthName TEXT NOT NULL,
# RepoName TEXT NOT NULL,
# URL TEXT NOT NULL,
# Issues INTEGER,
# Stars INTEGER,
# UpdateDate TEXT,
# ReadmePath TEXT,
# Language TEXT);'''

# cursor.execute(create_table_sql)

# #提交資料庫變更
# conn.commit()

# # 關閉 cursor 物件與資料庫連線
# cursor.close()
# conn.close()


