import pandas as pd
path = 'Reto_Sesión_2/spotify_data.csv'
retail_data = pd.read_csv(path, encoding = "latin1")
print(type(retail_data))
print(retail_data)