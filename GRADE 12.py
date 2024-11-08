#creating empty series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
#Creating Series using list
l1=[1,2,3,4,5,6,7,8,9]
s=pd.Series(l1)
#printing first 2 characters
print(s.head(2))
printing last 2 characters
print(s.tail(2))
print(s)
#printing series with index
l1=['A','B','C','D']
sal=[1000.1,2000.2,3000.3,4000.4]
s=pd.Series(sal,index=l1)
print(s)
print(s>2000)
s[2000.2]=101
print(s.empty)
s=range(1,27,1)
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=pd.Series(alpha,s)
print(s)
print(s.head(5))
print(s*2)
print(s.sort_index(ascending=False))
print(s.sort_values())
print(s.sort_index())
input()

w1={'day1':20,'day2':21,'day3':22,'day4':23,'day5':24,'day6':25,'day7':26}
s1=pd.Series(w1)
print(s1)

s2=s1
s3=s2
s4=s3
x=(s1+s2+s3+s4)
print(x/4)

ar=np.array([1,2,3,4])
ar2=np.array(['a','b','c','d'])
ar3=np.array(['one','two','three','four'])
df=pd.DataFrame([ar,ar2,ar3])
print(df)

l1=[1,2,3,4]
l2=['one','two','three','four']
df=pd.DataFrame([l1,l2])
print(df)

l1=[1,2,3,4,5]
l2=['one','two','three','four']
df=pd.DataFrame([l1,l2],['a','b'],columns=['a','b','c','d','e'])
print(df)

Smaple DataFrame

d1={'rollno.':[1,2,3,4,5,6],'name':['Prerna Singh','Manish Arora','Tanish Goel','Falguni Jain','Kanika Bhatnagar','Ramandeep Kaur'],'UT1':[24,18,20,22,15,20],'UT2':[24,17,22,20,20,15],'UT3':[20,19,18,24,18,22],'UT4':[22,22,24,20,22,24]}
df=pd.DataFrame(d1)
print(df)

df=pd.DataFrame([['Toyota',23845,141],['Honda',17995,80],['BMW',135925,182],['Audi',71400,160]],columns=['Company','Price','Horsepower'])
print(df)

d1=np.array([103,203,403])
d2=np.array([503,603,703])
d3=np.array([803,903,1003])
df=pd.DataFrame([d1,d2,d3])
print(df)

staff=pd.Series([20,36,44])
salaries=pd.Series([279000,396800,563000])
avg=salaries/staff
org={'People':staff,'Amount':salaries,'Average':avg}
df=pd.DataFrame(org)
print(df)
print('Transpose:')
print(df.T)
print('shape attribute:')
print(df.shape[0])
print('value attribute(Giving list inside list)')
print(df.values)
print(df['Amount'])

#
l1=[10927986,12691836,4631392,4328063]
l2=[189,208,149,157]
l3=[7916,8508,7226,7617]
x={'Population':l1,'Hospitals':l2,'Schools':l3}
df=pd.DataFrame(x,index=['Delhi','Mumbai','Kolkata','Chennai'])
print(df)

print('selecting one column:')
print(df.Population)
print('Selecting multiple columns')
print(df[['Population','Schools']])
print('CW:')
print(df.iloc[0:2,0:3:2])
print('Selectiing Rows/Columns based on boolean conditions:')
print(df.loc[:,'Population':'Population'][df.loc[:,'Population']>4328063])
print('accessing specific element in a table:')
print(df.at['Delhi','Population'])
print('accessing specific element in a table(using index(iat)):')
print(df.iat[0,0])
print('adding in a scalar manner')
df['Density']=1234
print(df)
#df['Banks']=20000
print(df)
df.at['Delhi':'Kolkata','Banks']=20000,30000,40000
print(df)

print(df)
print('Adding a row')   
#with at it will not work
df.loc['Hyderabad','Population':'Schools']=2200,1200,3200
print(df)
df.at['w',:]=ww
print(df)

#CSV FILE
marks=pd.read_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv")
print(marks)

#Header change
marks=pd.read_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv",header=None,skiprows=1)
print(marks)

#For Changing column name(Header=none required)
marks=pd.read_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv",names=['a','b','Name','Maths'],header=None,skiprows=1)
print(marks)

#For skipping rows(For odd rows)
marks=pd.read_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv",skiprows=[1,3,5,7,9])
print(marks)

#For selecting max value from a column
print(pd.read_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv").Maths.max())

# WRITING TO CSV
    
#Separator(Before using this please copy the things in the CSV or else Gone! or you can use 
#  this by putting another file's name in the place of the original file's name and that is creation of a csv from another csv in python)
print(marks.to_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv",sep='💣'))

marks.to_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S1.csv",index=False)

marks.loc[2,'Name']=np.NaN
marks.to_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S2.csv")
marks.to_csv("C:\\Users\srini\Desktop\Class 11\Python\CSV files\\S2.csv",na_rep='No value')
print(marks)
'''

#matplotlib line plot
year=[2014,2015,2016,2017,2018]
jnvpasspercentage=[90,92,94,95,97]
kvpasspercentage=[89,91,93,95,98]
plt.plot(year,jnvpasspercentage,color='black',linewidth=4,linestyle=':',marker='d',markersize=5,markeredgecolor='red')
plt.plot(year,kvpasspercentage,color='red',linewidth=5,linestyle='--',marker='D',markersize=4,markeredgecolor='k')

'''
#You can type r+ instead of marker color and marker style for taking the color of marker same as the line but the 
#condition is that the line style must be specified
'''

plt.xlabel('year')
plt.ylabel('Pass Percentage')
plt.title('JNV KV PASS PERCENTAGE TILL 2018')
plt.legend(('jnv','kv'),loc='lower right',frameon=False)
plt.grid(True)
plt.figure(figsize=(10,5))
#plt.savefig('C:\\Users\srini\Desktop\Class 11\Python\\CSV files\)
plt.show()

#Fibonacci series
fib=[0,1,1,2,3,5,8,12,21,34]
sqfib=np.sqrt(fib)
plt.plot(range(1,11),fib,color='k',linewidth=4,linestyle=':',marker='d',markersize=5,markeredgecolor='red')
plt.plot(range(1,11),sqfib,color='blue',linewidth=5,linestyle='-',marker='D',markersize=5,markeredgecolor='green')
plt.figure(figsize=(10,5))
plt.plot()

states=['Delhi','TN','AP','KA']
players=[5,11,10,7]
plt.title('Bar Chart')
plt.xlabel('states')
plt.ylabel('Players')
plt.bar(states,players,width=0.25,color=('red','g','b','black'),fill=False,hatch=['*','-','/','o'])
plt.show()

info=['Gold','Silver','Bronze','Total']
India=[30,40,20,90]
Australia=[40,30,30,100]
England=[30,18,25,73]
Canada=[20,10,15,45]
X=np.arange(len(info))
plt.bar(info,Australia,width=0.15)
plt.bar(X+0.15,India,width=0.15)
plt.bar(X+0.30,England,width=0.15)
plt.bar(X+0.45,Canada,width=0.15)
plt.show()

# You can use kind=barh when reading from csv fot horizontal bar graph

col=[8000,6000,5000,4000,7000,10000,9000]
X=np.arange(7)
plt.bar(X,col,width=0.25,color='red')
plt.title('WolunteerWeekDayCollection')
plt.xlabel('Days')
plt.ylabel('Collection')
plt.xticks(X,['Mon','Tue','Wed','Thr','Fri','Sat','Sun'])
plt.show()

pr=[71.6,68.9,90.2,60.1,58.7]
plt.bar(range(len(pr)),pr,width=0.25,color='black')
plt.xticks(range(11,20))
plt.xlim(-2,10)
plt.title('Stock of abc.co')
plt.xlabel('Vanij')
plt.ylabel('Price')
plt.show()