# Install pandas from terminal - pip install pandas
import pandas as pd

dataFrame = pd.read_csv('people.csv')
# we are printing the original data frame
print(dataFrame)
# histogram for one column - default value of hist is 10- horizontal through orientation
# hist = dataFrame['Age'].hist(bins=2, orientation='horizontal')
# hist.set_title('my histogram')
# hist.set_xlabel('Ages')
# hist.set_ylabel('Frequency')

# histogram for all column
hist = dataFrame.hist(bins=10, grid='false')

# show histogram
import matplotlib.pyplot as plt

plt.show()
