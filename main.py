# Решение 1
'''
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

print(pd.get_dummies(data['whoAmI']))
'''

# Решение 2
'''
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

unique_values = data['whoAmI'].unique()

for i in unique_values:
    data.loc[:, i] = (data['whoAmI'] == i).astype(int)

data.drop('whoAmI', axis=1, inplace=True)
print(data.head())
'''
