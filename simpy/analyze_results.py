import matplotlib.pyplot as plt

# Exemple de temps d’attente simulés (en secondes)
temps_attente = [0.5, 1.2, 2.4, 1.8, 0.9, 1.5, 2.8, 3.0, 1.2, 0.7]

plt.figure(figsize=(8, 5))
plt.hist(temps_attente, bins=5, color='g', edgecolor='black', alpha=0.7)

plt.xlabel('Temps d\'attente (s)')
plt.ylabel('Nombre de requêtes')
plt.title('Distribution des temps d\'attente')

plt.grid()
plt.show()
