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

