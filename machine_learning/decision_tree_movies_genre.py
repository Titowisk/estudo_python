import panda as pd

names = ['Gender', 'Age', 'Genre']

df = pd.read_csv('movies.data', names=names)

print("Linhas: {}, Colunas: {}".format(len(df), len(df.columns)))

df.head()