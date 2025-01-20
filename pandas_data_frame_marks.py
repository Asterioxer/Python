import pandas as pd
import numpy as np
import statistics

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
             'attempts': [1,3,2,3,2,3,1,1,2,1], 
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#creation of data frame and counting rows and columns
df = pd.DataFrame(data = exam_data, index=labels)
print(df.shape)
#missing values
missing_values = df.isnull().sum()
print(missing_values)
#unique values
unique_values = df.nunique()
print(unique_values)
#value updation
df.loc['d','score']=11
df.loc['h','score']=8
x = df['score']
#statistics functions
print(statistics.mean(x))
print(statistics.median(x))
print(statistics.mode(x))
 