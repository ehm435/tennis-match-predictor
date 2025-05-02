import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('tennis_matches.csv')

# categória surface en columnas binarias
df = pd.get_dummies(df, columns=['surface'])

# X contiene las características para predecir.
# y es lo que queremos predecir (si gana A).
X = df.drop('A_wins', axis=1)
y = df['A_wins']

# Dividir el dataset para tener partidos para entrenar el modelo y partidos para probarlo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)

# intenta predecir los resultados del conjunto de test
preds = model.predict(X_test)

# porcentaje de aciertos del modelo
print('Accuracy:', accuracy_score(y_test, preds))
# tabla con los verdaderos positivos, falsos positivos, etc
print('Confusion matrix:\n', confusion_matrix(y_test, preds))

