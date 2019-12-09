import pandas as pd
import matplotlib.pyplot as plt
from pandas_ml import ConfusionMatrix

# Read a csv file to a dataframe with delimiter as space or tab
data =  pd.read_csv('test_results',  sep='\s+', engine='python')
#print(data)
data = data.drop(['INFO:tensorflow:===','IMAGES','==='], axis=1)
data.columns = ['actual','predicted']
data['actual'] = data['actual'].apply(lambda x: x.split('/')[2])
#print(data)

confusion_matrix = pd.crosstab(data['actual'], data['predicted'], rownames=['Actual'], colnames=['Predicted'])
print (confusion_matrix)

confusion_matrix2 = ConfusionMatrix(data['actual'], data['predicted'])
confusion_matrix2.plot(normalized=True)
plt.show()