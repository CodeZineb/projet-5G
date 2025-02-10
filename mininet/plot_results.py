import matplotlib.pyplot as plt

# Simulation des résultats de débit (exemple)
temps = [1, 2, 3, 4, 5]  # secondes
debit = [5.2, 5.5, 5.8, 5.9, 6.0]  # Mbps

plt.figure(figsize=(8, 5))
plt.plot(temps, debit, marker='o', linestyle='-', color='b', label='Débit')

plt.xlabel('Temps (s)')
plt.ylabel('Débit (Mbps)')
plt.title('Évolution du débit réseau')
plt.legend()
plt.grid()

plt.show()
