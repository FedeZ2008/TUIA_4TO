import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corpus = [ 
    "el perro ladra fuerte", 
    "el gato maulla suave",  
    "el perro y el gato juegan", 
    "el pájaro canta bonito", 
    "el caballo corre rápido", 
    "la vaca muge despacio", 
    "el pez nada tranquilo", 
    "la abeja zumba cerca", 
    "el ratón corre pequeño", 
    "el gallo canta temprano", 
    "el lobo aúlla de noche", 
    "la rana salta alto", 
    "el león ruge fuerte", 
    "la oveja bala bajito", 
    "el pato nada contento", 
    "el burro rebuzna fuerte", 
    "el tigre acecha sigiloso", 
    "la tortuga camina lento", 
    "el mono grita alegre", 
    "el perro duerme tranquilo" 
] 
#def pandas_one_hot_manual(corpus): 
    # 1. Crear vocabulario único
    frase = corpus.split()
    print(frase)
    # 2. Asignar índice a cada palabra
    palabra2idx = {palabra: idx for idx, palabra in enumerate(vocabulario)}
    # 3. Crear matriz one-hot para cada documento
    matriz = np.zeros((len(corpus), len(vocabulario)), dtype=int)
    for i, doc in enumerate(corpus):
        for palabra in doc.split():
            matriz[i, palabra2idx[palabra]] = 1
    # 4. Retornar matriz y vocabulario
    return matriz, palabra2idx

def crear_one_hot_manual(corpus): 
    # 1. Crear vocabulario único
    vocabulario = sorted(set(" ".join(corpus).split()))
    # 2. Asignar índice a cada palabra
    palabra2idx = {palabra: idx for idx, palabra in enumerate(vocabulario)}
    # 3. Crear matriz one-hot para cada documento
    matriz = np.zeros((len(corpus), len(vocabulario)), dtype=int)
    for i, doc in enumerate(corpus):
        for palabra in doc.split():
            matriz[i, palabra2idx[palabra]] = 1
    # 4. Retornar matriz y vocabulario
    return matriz, palabra2idx

# Generar matriz y vocabulario
matriz, vocabulario = crear_one_hot_manual(corpus)

# Visualización requerida
print("Vocabulario con índices:")
for palabra, idx in vocabulario.items():
    print(f"{idx}: {palabra}")

print("\nMatriz One-Hot:")
print(matriz)

# Heatmap con seaborn
plt.figure(figsize=(12, 8))
sns.heatmap(matriz, cmap="YlGnBu", cbar=True, xticklabels=list(vocabulario.keys()), yticklabels=False)
plt.title("One-Hot Encoding Manual del Corpus")
plt.xlabel("Palabras")
plt.ylabel("Documentos")
plt.tight_layout()
plt.show()