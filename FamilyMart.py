import  requests
from fake_useragent import UserAgent
import pandas as pd
import time
import json
fruit_list = []
FamilyMart = pd.DataFrame(fruit_list, columns = ['StoreName' , 'City', 'Dist','No', 'NoName', 'Address'])
iocno=0
citylist=['台北市','基隆市','新北市','桃園市','新竹市','台中市','嘉義市','台南市','高雄市','新竹縣','苗栗縣', '彰化縣', '南投縣', '宜蘭縣', '花蓮縣', '雲林縣', '嘉義縣', '台東縣','屏東縣','澎湖縣','金門縣','連江縣']
for city in citylist:
    url = f'https://api.map.com.tw/net/familyShop.aspx?searchType=ShowTownList&type=&city={city}&fun=storeTownList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'
    userAgent = UserAgent().random
    headers={'Referer': 'https://www.family.com.tw/','User-Agent':userAgent}
    res = requests.get(url,headers=headers)
    citytext=res.text
    cityjson=json.loads(citytext.replace('storeTownList(','').replace(')','')) #變為list
    for c in range(len(cityjson)):
        Dist=cityjson[c]['town']  #區域
        new_url=f'https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city={city} &area={Dist}&road=&fun=showStoreList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC'
        new_res = requests.get(new_url, headers=headers)
        town_text = new_res.text
        townjson=json.loads(town_text.replace('showStoreList(','').replace(')','')) #變為list
        for t in range(len(townjson)):
            NoName=townjson[t]['NAME'].split('家')[1]  #店名
            No=townjson[t]['pkey']    #店號
            Address=townjson[t]['addr'].replace('臺','台')  #地址
            FamilyMart.loc[iocno] = ['FamilyMart',city,Dist, No, NoName, Address]
            iocno += 1
            print(Address)
    print(f'===={city}====')
    time.sleep(8)
FamilyMart.to_csv("./FamilyMart.csv",encoding='utf-8-sig',index=False)






