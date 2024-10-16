
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


# We look into the keys of this json file to have a better understanding of the data and then we will use the relevant keys to generate a data frame


iris = load_iris()

iris.keys()


# After visiting the data we have some idea of what key values we are about to use to make the test and train data for this model. So we will create an initial version of data frame use DataFrame functions in pandas with parems as iris.data as the data and columns as iris.feature names for which iris.data is listed

df = pd.DataFrame(iris.data, columns= iris.feature_names)

df.head(10)

# Now we would like to know what are the target names for a flower with certain sepal width, petal len and petal width, For that we would create a categorical data and we will map the code in target key and string categories in target_names key and we will map them to create a memory efficient categorical data.
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.head(10)

 
# Just to divide the data into 20% 80% split. Just so we could use the 8-% data for training and 20% for testing. It is an alternative to train_test_split and provide a better understanding of how splitiing of training and testing data works for the larger dataset.

 
df['divide'] = np.random.uniform(0,1, len(df)) >=0.80

df.head(10)

 
# Now we will asignt the splitted data to 2 data sets as test and train

 
test, train = df[df['divide'] == True], df[df['divide']== False]
print(len(test), len(train))




 
train.head(5)

 
# #### Selecting the First 4 columns for training purpose

 
features = df.columns[:4]
# Converting each specie name to digit so that the computer could differentiate between them. 
Y= pd.factorize(train['species'])[0]
Y

 
model_1 = RandomForestClassifier( random_state = 0)
model_1.fit(train[features], Y)


 
# 

 
prediction = model_1.predict(test[features])

prediction

 
# #### Testing the Prediction Probability of this prediction

 
model_1.predict_proba(test[features])[:20]

 
#mapping names for each predicition target to the name of the flowers

preds = iris.target_names[model_1.predict(test[features])]
preds

 
# Creating a Confussion Matrix to better explain how the Random Tree Forest Works

table = pd.crosstab(test['species'], preds, rownames = ["Actual Species"], colnames= ["Predicted Species"])
table

 
# Checking the Accuracy of Our prediction model. 

 
accuracy =accuracy_score(test['species'], preds)
print(accuracy*100)


