import pandas as pd
import matplotlib.pyplot as plt
Section=['A','B','C','D']
Contribution=[6700,5600,5000,5200]
S=pd.Series(Contribution,index=Section)
print(S)
print(S[S>5000])

import matplotlib.pyplot as plt
Prog=['Java','Python','PHP','JavaScript','c#','C++']
Popu=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(Prog,Popu)
plt.grid()
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')
plt.title('Some Title')
#plt.savefig("something.jpg")
plt.show()