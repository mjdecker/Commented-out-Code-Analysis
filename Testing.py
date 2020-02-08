import letterFreq
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import graphviz

letterFreqData = letterFreq.load_letterFreq()

#print(letterFreqData)

y = letterFreqData["target"]
X = letterFreqData["data"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
dt = DecisionTreeClassifier(min_samples_split=20)
dt = dt.fit(X_train, y_train)

dot_data = export_graphviz(dt, feature_names=letterFreqData["feature_names"], out_file=None, filled=True, class_names=letterFreqData["target_names"])
#graph = graphviz.Source(dot_data) 
#graph.render("comments_decision_tree") 

y_pred = dt.predict(X_test)

results_train_test_split = { "accuracy_train_test_split":  metrics.accuracy_score(y_test, y_pred),
		    "precision_train_test_split": metrics.precision_score(y_test, y_pred),
 		    "recall_train_test_split":    metrics.recall_score(y_test, y_pred),
 		    "F1_train_test_split":        metrics.f1_score(y_test, y_pred)
		  }

[print(key + ":", results_train_test_split[key]) for key in results_train_test_split]

print("\n-----------------------------------------------------------------\n")


y = letterFreqData["target"]
X = letterFreqData["data"]
kf = KFold(n_splits=5, random_state=None, shuffle=True)
for train_index, test_index in kf.split(X) :
	X_train_kfold, X_test_kfold = X[train_index], X[test_index]
	y_train_kfold, y_test_kfold = y[train_index], y[test_index]
	dt_kfold = DecisionTreeClassifier(min_samples_split=20)
	dt_kfold = dt_kfold.fit(X_train_kfold, y_train_kfold)



	y_pred_kfold = dt_kfold.predict(X_test_kfold)

	results_kfold = { "accuracy_kfold":  metrics.accuracy_score(y_test_kfold, y_pred_kfold),
		    	"precision_kfold": metrics.precision_score(y_test_kfold, y_pred_kfold),
 		    	"recall_kfold":    metrics.recall_score(y_test_kfold, y_pred_kfold),
 		    	"F1_kfold":        metrics.f1_score(y_test_kfold, y_pred_kfold)
		  	}

	[print(key + ":", results_kfold[key]) for key in results_kfold]
dot_data = export_graphviz(dt, feature_names=letterFreqData["feature_names"], out_file=None, filled=True, class_names=letterFreqData["target_names"])
#graph = graphviz.Source(dot_data) 
#graph.render("comments_decision_tree") 