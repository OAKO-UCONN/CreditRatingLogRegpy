import pandas as pd
data = pd.read_csv('AppleInputData.csv', header = 0)
def isDefault(x):
    if x < 0.01:
        return 1
    return 0
 #create new column 'Default': it is 1 for companies with rating
data['Default'] = data['market return'].apply(lambda x: isDefault(x))
print(data.head(15))