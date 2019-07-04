# Activity 2: Evaluating tuned model performance

# continuing from Exercise 7:

# generate predicted probabilities of yes
predicted_prob = model.predict_proba(X_test)[:,1]

# generate predicted classes
predicted_class = model.predict(X_test)

# evaluate performance with confusion matrix
from sklearn.metrics import confusion_matrix
import numpy as np
cm = pd.DataFrame(confusion_matrix(y_test, predicted_class))
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted No', 'Predicted Yes', 'Total']
cm = cm.set_index([['Actual No', 'Actual Yes', 'Total']])
print(cm)

# generate a classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, predicted_class))