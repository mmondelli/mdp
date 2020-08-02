import pandas as pd
from bs4 import BeautifulSoup
import requests


def read_data(file, source):
    df = pd.read_csv(file)
    df['Who'] = source
    #print(df[:5])
    return df

def get_genres(df):

    df['Genres'] = ' '
    for movie in df['Movie ID']: 
        print(movie)
        page = requests.get('https://www.netflix.com/title/' + str(movie))

        soup = BeautifulSoup(page.text, 'html.parser')
        genres = ''
        for genre in soup.select("div.more-details-cell.cell-genres span"):
            genres = genres + genre.text
        print(genres)
        
        df['Genres'].loc[df['Movie ID'] == movie] = genres
    df.to_csv('./data/with_genres.csv')
    

if __name__ == '__main__':
    
    #Read data
    file_malu = './data/sample_malu.csv'
    df_malu = read_data(file_malu, 'Malu')
    file_ze = './data/sample_ze.csv'
    df_ze = read_data(file_ze, 'Ze')
    
    #Concatenate the dataframes
    df_both = pd.concat([df_malu, df_ze])
    df_both.to_csv('./data/all_malu_ze.csv', index = False, header=True)

    print(len(df_both))

    #Get genres (movies and tv)
    get_genres(df_both)
    