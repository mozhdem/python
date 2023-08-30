import requests
import re
import mysql.connector
from bs4 import BeautifulSoup
for p in range (1,20):
    r=requests.get("https://www.truecar.com/used-cars-for-sale/listings/?page=p")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    brand=[]
    model=[]
    count=0
    soup=BeautifulSoup(r.text,"html.parser")
    res1=soup.find_all(attrs={"class":"vehicle-card-bottom vehicle-card-bottom-top-spacing"})
    res2=soup.find_all(attrs={"class":"margin-top-2_5 padding-top-2_5 border-top w-100"})
    res3=soup.find_all('h3',attrs={"class":"heading-base"})
    for t in res1:
        #print(t.text)
        f=re.findall(r'[pP]rice\$(\d*[.,]?\d*$)',t.text)
        #print(f)
        a.append(f)  #a alan list gheymat maschin hast

    for n in res2:
        #print(n.text)
        h=re.findall(r'(\d*[.,]\d*) miles',n.text)
        #print(h)
        b.append(h)  #b masfat(km) maschine
    for m in res3:
        year=re.findall(r'(\d{4})',m.text)
        c.append(year[0]) #c sal tolid maschine

    for q in res3:
        brand=q.text.split()
        d.append(brand[1])  #d brand maschine(ford,nissan,...)

    
    for z in res3:
        model=z.text.split()
        e.append(model[2])  #d model maschine(ford,nissan,...)
    '''print(a)
    print(b)
    print(c)
    print(d)
    print(e)'''
    cnx = mysql.connector.connect(user='root', password='Wrqgwjkp@967@#5',
                              host='127.0.0.1',
                              database='finalproject')
    cursor=cnx.cursor()
    for i in range (0,len(res1)):
        hazine=a[i]
        estefade=b[i]
        hazinee=hazine[0]
        estefadee=estefade[0]
        saltolid1=c[i]
        brand1=d[i]
        model1=e[i]
        cursor.execute("insert into newcars(price,kilometer,productionyear,brand,model) values(%s, %s,%s,%s,%s)",(hazinee,estefadee,saltolid1,brand1,model1))
    cnx.commit()
    cnx.close()
