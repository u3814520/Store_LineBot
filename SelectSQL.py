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

citylist=['台北市','基隆市','新北市','桃園市','新竹市','台中市','嘉義市','台南市','高雄市','新竹縣','苗栗縣', '彰化縣', '南投縣', '宜蘭縣', '花蓮縣', '雲林縣', '嘉義縣', '台東縣','屏東縣','澎湖縣','金門縣','連江縣']
cityname=str(input('請輸入輸入查詢縣市:'))
try:
    citylist.index(cityname)
except ValueError:
    print('請重新輸入正確縣市')
    exit()

townname=str(input('請輸入輸入查詢區域:'))
tsql = f"""
    SELECT no,noname,address
    from {a}
    where city='{cityname}' and dist='{townname}';
    """
cursor.execute(tsql)
tdata=cursor.fetchall()
if len(tdata)==0:
    print(f'該區域沒有{storename}商店')
    exit()
dictselect=str(input('是否街道查詢?請輸入是或否:'))
if dictselect== '否':
    dictsql = f"""
        SELECT no,noname,address
        from {a}
        where city='{cityname}' and dist='{townname}';
        """
    cursor.execute(dictsql)
    dictdata = cursor.fetchall()
    cursor.close()
    print(f'▶▶▶總共有{len(dictdata)}間◀◀◀')
    for dr in dictdata:
        dr_no = dr[0]
        dr_noname = dr[1]
        dr_address = dr[2]
        print(f'▶店號:{dr_no}\n▶店名:{dr_noname}\n▶地址:{dr_address}\n================\n', end='')
else:
    road=str(input('請輸入輸入街道名稱:'))
    sql = f"""
        SELECT no,noname,address
        from {a}
        where city='{cityname}' and dist='{townname}' and address like '%{road}%';
        """
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    if len(data)==0:
        print(f'該區域沒有{storename}商店')
    else:
        print(f'▶▶▶總共有{len(data)}間◀◀◀')
        for r in data:
            r_no=r[0]
            r_noname=r[1]
            r_address=r[2]
            print(f'▶店號:{r_no}\n▶店名:{r_noname}\n▶地址:{r_address}\n================\n',end='')






