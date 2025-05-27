# 🇬🇧 English Version

# Tennis Match Prediction with Logistic Regression

This project aims to predict whether **Player A will win a tennis match**, using **supervised classification** techniques via logistic regression. It uses CSV-formatted historical match data.

Data is preprocessed with `pandas`, turning categorical variables (like **match surface**) into binary variables (one-hot encoding). A logistic regression model is trained with `scikit-learn`, and its performance is evaluated using **accuracy** and a **confusion matrix**.

## 🛠 Technologies Used

- Python 3.x
- pandas
- scikit-learn
- numpy (optional, for array handling)
- matplotlib (optional, for visualization)

## 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/ehm435/tenis-match-predictor.git
   cd tenis-match-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Execution

Run from terminal. Ensure you have a CSV file with match data in the same folder or specify its path.

```bash
python tennis-match-predictor.py tennis_matches.csv
```

## 📊 Example Output

```
Model Accuracy: 0.73
Confusion Matrix:
[[87 15]
 [20 78]]
```

Where:
- Accuracy indicates the percentage of correct predictions.
- The confusion matrix shows true positives, false positives, true negatives, and false negatives.

## 💡 Future Improvements

- Apply cross-validation techniques
- Explore other classifiers (decision trees, SVM)
- Add interactive visualizations for exploratory analysis
- Use GridSearchCV for hyperparameter tuning
- Save/load the model using `joblib`

## 📁 Project Structure

```
tenis-logistic-regression/
│
├── tennis-match-predictor.py     # Main script
├── requirements.txt              # Dependencies list
├── README.md                     # This file
└── tennis_matches.csv            # Example dataset
```


---

# 🇪🇸 Versión en Español

# Predicción de partidos de tenis con regresión logística

Este proyecto tiene como objetivo predecir si el **jugador A ganará un partido de tenis**, utilizando técnicas de **clasificación supervisada** con regresión logística. Para ello, se emplean datos separados por ',' en formato CSV con información histórica de partidos.

Se preprocesan los datos con `pandas`, convirtiendo variables categóricas (como la **superficie del partido**) en variables binarias (one-hot encoding). Posteriormente, se entrena un modelo de regresión logística con `scikit-learn`, evaluando su rendimiento mediante la **exactitud (accuracy)** y la **matriz de confusión**.

---

## 🛠 Tecnologías utilizadas

- Python 3.x
- pandas
- scikit-learn
- numpy (opcional, para manejo de arrays)
- matplotlib (opcional, para visualizaciones)

---

## 📦 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/ehm435/tenis-match-predictor.git
   cd tenis-match-predictor
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución

El proyecto se ejecuta desde consola. Asegúrate de tener un archivo CSV con los datos de partidos en la misma carpeta o especifica la ruta.

```bash
python tennis-match-predictor.py tennis_matches.csv
```

---

## 📊 Ejemplo de salida

```
Precisión del modelo: 0.73
Matriz de confusión:
[[87 15]
 [20 78]]
```

Donde:
- La precisión representa el porcentaje de predicciones correctas.
- La matriz de confusión indica el número de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.

---

## 💡 Mejoras futuras

- Aplicar técnicas de validación cruzada (cross-validation).
- Explorar otras técnicas de clasificación (árboles de decisión, SVM).
- Añadir visualizaciones interactivas para análisis exploratorio.
- Ajuste automático de hiperparámetros (GridSearchCV).
- Guardar y cargar el modelo con `joblib`.

---

## 📁 Estructura del proyecto

```
tenis-logistic-regression/
│
├── tennis-match-predictor.py                 # Script principal
├── requirements.txt        # Lista de dependencias
├── README.md               # Este archivo
└── tennis_matches.csv      # Dataset de ejemplo
```


