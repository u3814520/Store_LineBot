import pymysql

def getStore(store,city,dist,address):
    conn = pymysql.connect(user="ting",
                           passwd="123456",
                           db="Store",
                           host="127.0.0.1",
                           local_infile=1)
    cursor = conn.cursor()

    sql = f"""
            SELECT no,noname,address
            from {store}
            where city='{city}' and dist='{dist}' and address like '%{address}%';
            """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

if __name__ == '__main__':
    for s in getStore():
        print(f'店號:{s[0]}\n店名:{s[1]}\n地址:{s[2]}')
        print('====================================')