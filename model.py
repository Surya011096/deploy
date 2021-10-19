import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
df = pd.read_excel('E:\deploy\deploy.xlsx')
print(df.head())
X=df[['DIM_Area','DIM_BusinessUnit','DIM_Salesmans','DIM_Customer','DIM_Vendor','INVOICEDAY',
       'INVOICEMONTH', 'INVOICEYEAR']]
y=df['LINEAMOUNT']
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(random_state = 0)
model.fit(X, y)
pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
