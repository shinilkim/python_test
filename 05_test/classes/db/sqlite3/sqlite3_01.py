'''
http://zetcode.com/db/sqlitepythontutorial/
'''
import sqlite3 as lite
import sys, os, json

class Sqlite:
  conn = None
  cursor = None
  db_file = os.path.join('C:\home\dev\workspace_python\python_test\db','test.db3')

  def __init__(self):
    try:
      self.conn = lite.connect(self.db_file)
      self.cursor = self.conn.cursor()
    except lite.Error as e:
      print("Error %s: " % e.args[0])
      sys.exit(1)

  def __del__(self):
    if self.conn:
      self.conn.close()

  def row(self, query, param):
    try:
      if param:
        self.cursor.execute(query, param)
      else:
        self.cursor.execute(query)
    except lite.Error as e:
      print("rows(query) Exception: ",e)
      print(query)
    return self.cursor.fetchone()

  def rows(self, query, param):
    try:
      if param:
        self.cursor.execute(query, param)
      else:
        self.cursor.execute(query)
    except lite.Error as e:
      print("rows(query) Exception: ",e)
      print(query)
    return self.cursor.fetchall()

  def rowsJson(self, query, param):
    data = []
    try:
      if param:
        self.cursor.execute(query, param)
      else:
        self.cursor.execute(query)
      col = [cn[0] for cn in self.cursor.description]
      rows = self.cursor.fetchall()
      for row in rows:
        rs = {}
        for i in range(len(col)):
          rs[col[i]] = row[i]
        data.append(rs)
    except lite.Error as e:
      print("rows(query) Exception: ",e)
      print(query)
    return data

  def datatables(self, query, param, key):
    '''
    json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None,
            separators=None, default=None, sort_keys=False, **kw)
    '''
    data = {}
    data[key] = db.rowsJson(query, param)
    return json.dumps(data, ensure_ascii=False)

  def datatable(self, query, param):
    return self.datatables(query, param, 'data')

  def printDatatable(self, query, param):
    print(json.dumps(db.rowsJson(query, param), ensure_ascii=False))

  def setMode(self, mode):
    if mode and mode.upper() == "FACTORY":
      self.conn.row_factory = lite.Row
    else:
      self.conn.row_factory = lite.Statement
    self.cursor = self.conn.cursor()

  def execute(self, query):
    try:
      self.cursor.execute(query)
      self.conn.commit()
    except lite.Error as e:
      print("execute(query) Exception: ", e)
      self.conn.rollback()
      print(query)
    return self.cursor.rowcount

  def excutemany(self, query, tuple):
    try:
      self.cursor.executemany(query, tuple)
      self.conn.commit()
    except lite.Error as e:
      self.conn.rollback()
      print("excutemany(query) Exception: ", e)
      print(query)
    return self.cursor.rowcount

  def executescript(self, query):
    try:
      self.cursor.executescript(query)
      self.conn.commit()
    except lite.Error as e:
      self.conn.rollback()
      print("executescript(query) Exception: ", e)
      print(query)
    return self.cursor.rowcount

  def version(self):
    return self.row("SELECT SQLITE_VERSION()", None)

  def printRows(self, query, param):
    rows = self.datatable(query, param)
    for row in rows:
      print(row)

if __name__ == '__main__':
  db = Sqlite()
  version = db.version()

  print('\n# 1. 버전 체크')
  print("SQLITE version: %s" % version)

  print('\n# 2. 다중 쿼리 스크립트 실행')
  query = '''
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars VALUES(1,'아우디',52642);
        INSERT INTO Cars VALUES(2,'Mercedes',57127);
  '''
  #db.setMode("FACTORY")
  print(db.executescript(query))
  #rows = db.rows("SELECT * FROM Cars")
  #for row in rows:
  #  print(row["Id"], row[1])
  rows = db.rows("SELECT * FROM Cars", None)
  for row in rows:
    print(row)

  print('\n# 3. parameter mapping')
  query = "select :name, a.* from cars a where Id=:id and name=:name"
  param = {'id':2, 'name':'Mercedes'}
  row = db.row(query, param)
  print(row)

  print('\n# 4. meta')
  query = "PRAGMA table_info(Cars)"
  rows = db.rows(query, None)
  for row in rows:
    print(row)

  print('\n# 5. json')
  query = "select * from cars"
  data = db.datatable(query, None)
  print(data)

  print('\n# 6. 테이블목록 조회')
  db.printDatatable("SELECT * FROM sqlite_master WHERE type='table'",None)

  print('\n# 7. 다중 insert')
  query = "INSERT INTO Cars VALUES(?, ?, ?)"
  cars = (
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
  )
  affected = db.excutemany(query, cars)
  print("{0} insert success".format(affected))
  db.execute("DELETE FROM Cars WHERE Id=7")
  db.printDatatable("select * from cars",None)