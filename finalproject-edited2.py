import mysql.connector
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
cnx1=mysql.connector.connect(user='root', password='Wrqgwjkp@967@#5',
                              host='127.0.0.1',
                              database='finalproject')
cursor1=cnx1.cursor()
cursor1.execute("select* from newcars")
allresults=cursor1.fetchall()
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
#x7=[]
x0=[]
y=[]
x=[]
ans=[]
dadekar=[]
count=0
count1=0
for item in allresults:
    itvar=0
    itvar=item[0]
    itvar=itvar.replace(",","")
    x2.append(itvar) #x2 price 
for item in allresults:
    itvar=0
    itvar=item[1]
    itvar=itvar.replace(",","")
    x3.append(itvar) #x3 km

for item in allresults:
    if item[3]=="INFINITI":
        x6.append("apple")
    else:
        x6.append(item[3])
        
    
for item in allresults:
    x=[]
    x.append(x3[count])
    x.append(item[2])
    #x.append(x6[count])
    #x4.append(x6[count]) #x4 brand
    x.append(item[4])
    x5.append(item[4]) #x5 model
    x1.append(x)        #x1 [km,sal,brand,model]
    y.append(x2[count]) #y gheymat 
    count+=1
'''print(x1[0])
print(y[0])
print("***************************************")
print(x4)
print(x5)'''
#le.fit(x4)
le.fit(x5)
#le.transform(x4)
x7=le.transform(x5)
#print("***********************************************************")
#print(le.transform(x5))
for item in allresults:
    x=[]
    x.append(x3[count1])
    x.append(item[2])
    #x.append(x6[count1])
    x.append(x7[count1])
    x0.append(x)
    count1+=1
#print(x0[0],x0[1])
#print(y[0],y[1])
'''newdata=[['33988','2010','ExpeditionXLT']]
newdata1=newdata[0]
uv=le.transform([newdata1[2]])
del newdata1[2]
newdata1.append(str(uv[0]))
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x0,y)
answer=clf.predict([newdata1])
print(answer)'''
dade1=input("lotfan km maschin khod ra vared konid(nemune:sotun 2 database)")
dadekar.append(dade1)
dade2=input("lotfan sal sakht maschin khod ra vared konid(nemune:sotun 3 database)")
dadekar.append(dade2)
dade3=input("lotfan model maschin khod ra vared konid((nemune:sotun 5 database)mesl:JettaS,C-ClassC,VersaSV,....)")
dadekar.append(dade3)
newdata=[dadekar]
newdata1=newdata[0]
uv=le.transform([newdata1[2]])
del newdata1[2]
newdata1.append(str(uv[0]))
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x0,y)
answer=clf.predict([newdata1])
print("gheymat takhmini:",answer)

    
