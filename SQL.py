import pymysql

conn = pymysql.connect(user="ting",
                          passwd="123456",
                          host="127.0.0.1",
                          local_infile=1)
conn.set_charset('utf8')
cur = conn.cursor()
cur.execute("DROP DATABASE Store")
cur.execute("CREATE DATABASE IF NOT EXISTS Store")
conn = pymysql.connect(user="ting",
                        passwd="123456",
                        db="Store",
                        host="127.0.0.1",
                        local_infile=1)
cur = conn.cursor()
with cur as cursor:
    sevensql="""
        CREATE TABLE `seveneleven` (
  `StoreName` varchar(200) DEFAULT NULL,
  `City` varchar(200) DEFAULT NULL,
  `Dist` varchar(200) DEFAULT NULL,
  `No` int NOT NULL,
  `Noname` varchar(200) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
   PRIMARY KEY (`No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """
    cursor.execute(sevensql)
    Familysql = """
            CREATE TABLE `FamilyMart` (
      `StoreName` varchar(200) DEFAULT NULL,
      `City` varchar(200) DEFAULT NULL,
      `Dist` varchar(200) DEFAULT NULL,
      `No` int NOT NULL,
      `Noname` varchar(200) DEFAULT NULL,
      `address` varchar(200) DEFAULT NULL,
       PRIMARY KEY (`No`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
        """
    cursor.execute(Familysql)
    conn.connect()
conn.close()