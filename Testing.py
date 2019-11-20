import letterFreq
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics
from sklearn.model_selection import train_test_split

letterFreqData = letterFreq.load_letterFreq()

print(letterFreqData)

y = letterFreqData["target"]
X = letterFreqData["data"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt = dt.fit(X_train, y_train)

export_graphviz(dt, feature_names=letterFreqData["feature_names"], out_file=None, filled=True, class_names=letterFreqData["target_names"])

y_pred = dt.predict(X_test)

print("accuracy:", metrics.accuracy_score(y_test, y_pred))
print("F1:", metrics.f1_score(y_test, y_pred))

