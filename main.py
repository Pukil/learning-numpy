import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from collections import Counter

seaborn.set()

data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
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
names = np.array(data['name'])
letter_array = []
for name in names:
    for letter in name:
        if letter not in  " ,.":
            letter_array.append(letter.lower())

plt.hist(sorted(letter_array), bins="stone", align="mid")
plt.title('letter distribution in names of US presidents')
plt.xlabel('letter')
plt.ylabel('number of letters')
plt.show()