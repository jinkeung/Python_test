# oracle 라이브 -> oracledb
import oracledb as db
 # == jdbc interface

 # class.forname() # 내가 어떤 RDBMS 사용 명시 , Python X
   # oracle, mysql, mssql

 # Connection con = DriverManger.connection (url, id, pw )
con = db.connect(dsn="127.0.0.1:1521/xe", user="C##TEST", password="1234")
""" dsn [Domain Service Name ] == Java. url 
                                   jdbc:oracle:thin@192.168.0.0:1521/xe
 
"""
# Statement stat = con.CreateStatement()
  # 로그인 완료했고, 스크립트 실행 준비 완료
# stat.execute(sql)
cursor = con.cursor()

cursor.execute('select * from pytest')
# cursor - 마지막에 실행한 퀘리문의 정보를 자동 저장

#for i in cursor.fetchall():  # == cursor 2차원
 #print(i)

#print(cursor.fetchone()) #hasnext()
#print(cursor.fetchone())
#print(cursor.fetchone())
row = cursor.fetchone();
while(row):
 print(row)
 row = cursor.fetchone()

#print(cursor.fetchmany(size=3))