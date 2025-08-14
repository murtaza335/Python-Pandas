# what is a dataframe ?
# we can make a dataframe by lists or a dictionary

import pandas as pd
import numpy as np

# creating a dataframe from an array

data = np.array([[1,4],[2,5],[3,5]])


# index refers to the row names and the columns refer to the col names
df = pd.DataFrame(data, index = ['row1', 'row2', 'row3'], columns=['col1' , 'col2'])
print(df)

# doing it without numpy arrays will have the same result

# ------------------

# creating a df from teh dictionary

states = ['california', ' texas', 'florida', 'Newyork']
population = [333,3333,333,333]

dict_states = {'states' : states , 'Population' : population}

df2 = pd.DataFrame(dict_states)
print(df2)

