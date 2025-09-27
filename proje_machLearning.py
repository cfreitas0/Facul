# Passo 1: Importar Bibliotecas e Carregar Dados
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# Visualizar as primeiras linhas dos dados para entendimento
print("Primeiras 5 linhas dos dados de entrada (X):")
print(X[:5])
print("\nPrimeiras 5 linhas dos rótulos (y):")
print(y[:5])



# Passo 2: Pré-processamento dos Dados

# Dividir os dados em conjuntos de treinamento e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
# A normalização é importante para que o modelo aprenda de forma mais eficiente
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nShape dos dados de treinamento (X_train):", X_train.shape)
print("Shape dos dados de teste (X_test):", X_test.shape)



# Passo 3: Construir o Modelo

# O modelo é uma rede neural sequencial com duas camadas densas
# A camada de entrada tem 4 neurônios (uma para cada característica)
# A camada de saída tem 3 neurônios (uma para cada espécie de Iris) com ativação softmax
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
# Usamos o otimizador 'adam' e a função de perda 'sparse_categorical_crossentropy'
# pois os rótulos não estão em formato one-hot encoded
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Visualizar a arquitetura do modelo
model.summary()



# Passo 4: Treinar o Modelo

# Treinar o modelo com 50 épocas (iterações sobre os dados)
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))



# Passo 5: Avaliar o Modelo

# Avaliar a precisão final do modelo no conjunto de teste
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nPrecisão do modelo no conjunto de teste: {accuracy:.4f}")



# Passo 6: Fazer Previsões

# Fazer previsões para os primeiros 5 exemplos do conjunto de teste
predictions = model.predict(X_test[:5])

# Mostrar as probabilidades de cada classe para os primeiros 5 exemplos
print("\nProbabilidades de previsão para as 5 primeiras amostras de teste:")
print(predictions)

# Encontrar a classe prevista (o índice com a maior probabilidade)
predicted_classes = np.argmax(predictions, axis=1)

# Comparar as previsões com os rótulos reais
print("\nPrevisões do modelo (índice da classe):", predicted_classes)
print("Rótulos reais (índice da classe):", y_test[:5])

# Mapear os índices para os nomes das espécies para uma melhor interpretação
species_names = iris.target_names
predicted_species = [species_names[i] for i in predicted_classes]
true_species = [species_names[i] for i in y_test[:5]]

print("\nPrevisões do modelo (nome da espécie):", predicted_species)
print("Espécies reais:", true_species)