from sklearn.datasets import make_blobs
import matplotlib
# Usar backend no interactivo para entornos sin Tcl/Tk (evita errores de _tkinter)
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pathlib import Path

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)


ModeloAgrupamiento = KMeans(n_clusters=4, random_state=42)
ModeloAgrupamiento.fit(X)
y_Agrupamiento = ModeloAgrupamiento.predict(X)

plt.scatter(X[:,0], X[:,1], c=y_Agrupamiento, s=50, cmap="viridis")
centros = ModeloAgrupamiento.cluster_centers_
plt.scatter(centros[:,0], centros[:,1], c="red", s=200, alpha=0.75)

# Guardar la figura en la misma carpeta que el script (compatible con entornos sin GUI)
out_file = Path(__file__).parent / "actividad3_kmeans.png"
plt.savefig(out_file, dpi=150)
print(f"Figura guardada en: {out_file}")