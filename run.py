from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from datasource import load_data
from data_processing import filterdata
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

#Select Datasource
filesource = ["train.csv","test.csv"]

print("Loading Data...")
file = load_data(filesource[0])
#Split the Dataset into train set and test set
file, test_data = train_test_split(file,test_size = 0.2,random_state=42)

#Transform Data into Readable Form
y_train, train_tr = filterdata(file)
y_test, test_tr = filterdata(test_data)

#Select Random Forest As the Model
print("Training...")
forest = RandomForestClassifier(n_estimators=100, random_state=1)
multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)
tree_reg = multi_target_forest.fit(train_tr, y_train)

#Prediction
print("Training Complete")
print("Predicting...")
prediction = tree_reg.predict(test_tr)

#precision_score and recall_score
from sklearn.metrics import precision_score, recall_score
p1 = precision_score(prediction,y_test,average="micro")
print("Precision score: " +p1)
p2 = recall_score(prediction, y_test)
print("Recall score: "+p2)