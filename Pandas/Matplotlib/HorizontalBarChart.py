import matplotlib.pyplot as plt
countries = ["Pakistan", "India", "China", "Iran"]
population = [230, 1400, 1440, 85]
plt.barh(countries, population)
plt.title("Country Populations")
plt.show()