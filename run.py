from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from datasource import load_data
from data_processing import filterdata
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

filesource = ["train.csv","test.csv"]

file = load_data(filesource[0])
file, test_data = train_test_split(file,test_size = 0.2,random_state=42)

y_train, train_tr = filterdata(file)
y_test, test_tr = filterdata(test_data)

forest = RandomForestClassifier(n_estimators=100, random_state=1)
multi_target_forest = MultiOutputClassifier(forest, n_jobs=-1)
tree_reg = multi_target_forest.fit(train_tr, y_train)