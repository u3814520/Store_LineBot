import pymysql
host = '127.0.0.1'
port = 3306
user = 'ting'
passwd = '123456'
db = 'Store'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = conn.cursor()

storename=str(input('請輸入7-11或全家:'))
if storename == '7-11':
    a='seveneleven'

elif storename == '全家':
    a='familymart'

else:
    print('請輸入7-11或全家')

cityname=str(input('請輸入輸入查詢縣市:'))
townname=str(input('請輸入輸入查詢區域:'))
road=str(input('請輸入輸入街道名稱:'))

sql = f"""
    SELECT city, dist,no,noname,address
    from {a}
    where city='{cityname}' and dist='{townname}' and address like '%{road}%';
    """
cursor.execute(sql)
data = cursor.fetchall()

cursor.close()
conn.close()

for r in data:
    print(r)





