import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from collections import Counter

seaborn.set()

# data = pd.read_csv('data/president_heights.csv')
# heights = np.array(data['height(cm)'])
# print(heights)
#
# print(f"Mean: {heights.mean()}")
# print(f"Std: {heights.std()}")
# print(f"Min: {heights.min()}")
# print(f"Max: {heights.max()}")
#
# print(f"25th percentile: {np.percentile(heights, 25)}")
# print(f"Median: {np.median(heights)}")
# print(f"75th percentile: {np.percentile(heights, 75)}")

# heights
# plt.hist(heights)
# plt.title('height distribution of US presidents')
# plt.xlabel('height(cm)')
# plt.ylabel('number')
# plt.show()

# letters from names histogram
# names = np.array(data['name'])
# letter_array = []
# for name in names:
#     for letter in name:
#         if letter not in  " ,.":
#             letter_array.append(letter.lower())
#
# plt.hist(sorted(letter_array), bins="stone", align="mid")
# plt.title('letter distribution in names of US presidents')
# plt.xlabel('letter')
# plt.ylabel('number of letters')
# plt.show()


# data = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
# plt.hist(data, 40)
# plt.show()
# print(np.sum((data < 100) & (data > 50)))
# print(f"Days without rain: {np.sum(data == 0)}")
# print(f"Days with rain: {np.sum(data != 0)}")
# print(f"Days with more than 150 mm {np.sum(data > 150)}")
# print(f"Days with less than 100 mm {np.sum(data < 100)}")

# mask of rainy days
# rainy = data > 0
# summer days
# summer = (np.arange(365)- 172 < 90) & (np.arange(365) - 172 > 0)
#
# print(f"Median precip on rainy days: {np.median(data[rainy])}")
# print(f"Median precip on summer days: {np.median(data[summer])}")
# print(f"Max precip on summer days: {np.max(data[summer])}")
# print(f"Max precip on non-summer rainy days: {np.max(data[~summer & rainy])}")


# random points selecting
mean = [0, 0]
cov = [[1, 2], [2,5]]
X = np.random.multivariate_normal(mean,cov, 100)
print(X.shape)
print(X)


random_indices = np.random.choice(X.shape[0], 20, replace=False)
print(random_indices)
selected = X[random_indices]
print(selected)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selected[:, 0], selected[:, 1], edgecolors='red', facecolor='none', s=200)
plt.show()