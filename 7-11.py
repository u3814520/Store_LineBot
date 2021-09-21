import  requests
from bs4 import BeautifulSoup
import pandas as pd
import time

fruit_list = []
SevenEleven = pd.DataFrame(fruit_list, columns = ['StoreName' , 'City', 'Dist','No', 'NoName', 'Address'])
iocno=0
cityid= {'01':'台北市','02':'基隆市','03':'新北市','04':'桃園市','05':'新竹市','08':'台中市','13':'嘉義市','15':'台南市','17':'高雄市',
         '06':'新竹縣','07':'苗栗縣','10':'彰化縣','11':'南投縣','20':'宜蘭縣','21':'花蓮縣','12':'雲林縣','14':'嘉義縣','22':'台東縣','19':'屏東縣',
         '23':'澎湖縣','25':'金門縣','24':'連江縣'
         }
for k,v in cityid.items():
    url = 'https://emap.pcsc.com.tw/EMapSDK.aspx'
    county={'commandid':'GetTown','cityid':k}
    res = requests.post(url,data=county)
    soup = BeautifulSoup(res.text,'html.parser')
    datas=soup.select('townname')   #區域
    for i in range(len(datas)):
        city = datas[i].text
        region={'commandid':'SearchStore','city': v,'town':city}
        new_res = requests.post(url, data=region)
        new_soup = BeautifulSoup(new_res.text, 'html.parser')
        poiids = new_soup.select('poiid')
        for z in range(len(poiids)):
            poiid=poiids[z].text  #店號
            poiname = new_soup.select('poiname')[z].text   #店名
            address = new_soup.select('address')[z].text   #地址
            SevenEleven.loc[iocno] = ['SevenEleven',v,str(city),poiid,poiname,address]
            iocno += 1
            print(str(city))
    print('===={}===='.format(v))
    time.sleep(8)
SevenEleven.to_csv("./SevenEleven.csv",encoding='utf-8-sig',index=False)



