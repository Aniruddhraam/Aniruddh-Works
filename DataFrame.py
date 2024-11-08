import pandas as pd
emp={'Name':['Anu','Ram','Raj','Mano','Hari'],'Age':[25,27,35,27,32],'State':['TN','AP','TN','KA','AP'],'Salary':[26000,35000,45000,25000,37000]}
df=pd.DataFrame(emp,index=['E1','E2','E3','E4','E5'])
print(df)