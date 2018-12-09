import pandas as pd
import os 

path_global = r'C:\Users\Joel Mbouwe\Documents\Machine Learning\PUBG Finish Placement'
os.chdir(path_global)
path_train = 'Donnees/train_V2.csv'

df = pd.read_csv(path_train, sep = ',')

columns = df.columns.tolist()

data_per_match = df.groupby(['matchId'])

data_per_match['Id'].head(10)

groups = data_per_match.groups

group_id = list(groups.keys())[4]

data = data_per_match.get_group(group_id)
