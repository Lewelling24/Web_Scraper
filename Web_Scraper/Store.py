import pandas as pd

def store(movies):
# Store the information in a pandas dataframe
    df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])
    df.to_csv('top-rated-movies.csv', index=False)