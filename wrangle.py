import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

def get_beer():
    '''
    This reads in beer advocate data from data.world, writes data to
    a csv if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('beer.csv'):
        
        # read in data from csv file if one exists
        df = pd.read_csv('beer.csv', index_col=0)
        
    else:
        
        # Read data from db into a DataFrame
        df = pd.read_csv('https://query.data.world/s/4ig7g3rzpqxved7ivs3tvahjti4mzo?dws=00000')
        
        # Cache to .csv
        df.to_csv('beer.csv')
        
    return df

#finds beer types that are not barley and codes them as '0', the remainder is coded as '1'
def find_barley(row):
    if row['beer_style'] == "Hefeweizen":
        val = 0
    elif row['beer_style']  == 'Oatmeal Stout':
        val = 0
    elif row['beer_style']  == 'American Adjunct Lager':
        val = 0
    elif row['beer_style']  == 'Fruit / Vegetable Beer':
        val = 0
    elif row['beer_style']  == 'Weizenbock':
        val = 0
    elif row['beer_style']  == 'Rye Beer':
        val = 0
    elif row['beer_style']  == 'American Pale Wheat Ale':
        val = 0
    elif row['beer_style']  == 'Milk / Sweet Stout':
        val = 0
    elif row['beer_style']  == 'Witbier':
        val = 0
    elif row['beer_style']  == 'Dunkelweizen':
        val = 0
    elif row['beer_style']  == 'Roggenbier':
        val = 0
    elif row['beer_style']  == 'Japanese Rice Lager':
        val = 0
    elif row['beer_style']  == 'Wheatwine':
        val = 0
    elif row['beer_style']  == 'American Dark Wheat Ale':
        val = 0
    elif row['beer_style']  == 'Kristalweizen':
        val = 0
    elif row['beer_style']  == 'Braggot':
        val = 0
    elif row['beer_style']  == 'Berliner Weissbier':
        val = 0
    elif row['beer_style']  == 'Kvass':
        val = 0
    elif row['beer_style']  == 'Happoshu':
        val = 0
    elif row['beer_style']  == 'Sahti':
        val = 0
    else:
        val = 1
    return val

#finds ales and codes them as '0', coding the remainder (lagers) as '1'
def find_lager(row):
    if row['beer_style'] == "Hefeweizen":
        val = 0
    elif row['beer_style']  == 'English Strong Ale':
        val = 0
    elif row['beer_style']  == 'Foreign / Export Stout':
        val = 0
    elif row['beer_style']  == 'American Double / Imperial IPA':
        val = 0
    elif row['beer_style']  == 'Herbed / Spiced Beer':
        val = 0
    elif row['beer_style']  == 'Oatmeal Stout':
        val = 0
    elif row['beer_style']  == 'American Pale Ale (APA)':
        val = 0
    elif row['beer_style']  == 'American Porter':
        val = 0
    elif row['beer_style']  == 'Belgian Strong Dark Ale':
        val = 0
    elif row['beer_style']  == 'American IPA':
        val = 0
    elif row['beer_style']  == 'American Stout':
        val = 0
    elif row['beer_style']  == 'Russian Imperial Stout':
        val = 0
    elif row['beer_style']  == 'American Blonde Ale':
        val = 0
    elif row['beer_style']  == 'English Brown Ale':
        val = 0
    elif row['beer_style']  == 'Scotch Ale / Wee Heavy':
        val = 0
    elif row['beer_style']  == 'Fruit / Vegetable Beer':
        val = 0
    elif row['beer_style']  == 'American Double / Imperial Stout':
        val = 0
    elif row['beer_style']  == 'Belgian Pale Ale':
        val = 0
    elif row['beer_style']  == 'English Bitter':
        val = 0
    elif row['beer_style']  == 'English Porter':
        val = 0
    elif row['beer_style']  == 'American Barleywine':
        val = 0
    elif row['beer_style']  == 'Belgian Strong Pale Ale':
        val = 0
    elif row['beer_style']  == 'Pumpkin Ale':
        val = 0
    elif row['beer_style']  == 'Extra Special / Strong Bitter (ESB)':
        val = 0
    elif row['beer_style']  == 'English India Pale Ale (IPA)':
        val = 0
    elif row['beer_style']  == 'Kölsch':
        val = 0
    elif row['beer_style']  == 'Rye Beer':
        val = 0
    elif row['beer_style']  == 'American Pale Wheat Ale':
        val = 0
    elif row['beer_style']  == 'Milk / Sweet Stout':
        val = 0
    elif row['beer_style']  == 'Scottish Ale':
        val = 0
    elif row['beer_style']  == 'Witbier':
        val = 0
    elif row['beer_style']  == 'American Black Ale':
        val = 0
    elif row['beer_style']  == 'Saison / Farmhouse Ale':
        val = 0
    elif row['beer_style']  == 'Irish Dry Stout':
        val = 0
    elif row['beer_style']  == 'English Barleywine':
        val = 0
    elif row['beer_style']  == 'English Dark Mild Ale':
        val = 0
    elif row['beer_style']  == 'English Pale Ale':
        val = 0
    elif row['beer_style']  == 'Belgian IPA':
        val = 0
    elif row['beer_style']  == 'Tripel':
        val = 0
    elif row['beer_style']  == 'Flanders Oud Bruin':
        val = 0
    elif row['beer_style']  == 'American Brown Ale':
        val = 0
    elif row['beer_style']  == 'Winter Warmer':
        val = 0
    elif row['beer_style']  == 'Smoked Beer':
        val = 0
    elif row['beer_style']  == 'Dubbel':
        val = 0
    elif row['beer_style']  == 'Flanders Red Ale':
        val = 0
    elif row['beer_style']  == 'Dunkelweizen':
        val = 0
    elif row['beer_style']  == 'Belgian Dark Ale':
        val = 0
    elif row['beer_style']  == 'Bière de Garde':
        val = 0
    elif row['beer_style']  == 'Irish Red Ale':
        val = 0
    elif row['beer_style']  == 'English Stout':
        val = 0
    elif row['beer_style']  == 'Cream Ale':
        val = 0
    elif row['beer_style']  == 'American Wild Ale':
        val = 0
    elif row['beer_style']  == 'Scottish Gruit / Ancient Herbed Ale':
        val = 0
    elif row['beer_style']  == 'Wheatwine':
        val = 0
    elif row['beer_style']  == 'American Dark Wheat Ale':
        val = 0
    elif row['beer_style']  == 'Baltic Porter':
        val = 0
    elif row['beer_style']  == 'Kristalweizen':
        val = 0
    elif row['beer_style']  == 'English Pale Mild Ale':
        val = 0
    elif row['beer_style']  == 'Lambic - Fruit':
        val = 0
    elif row['beer_style']  == 'Quadrupel (Quad)':
        val = 0
    elif row['beer_style']  == 'Braggot':
        val = 0
    elif row['beer_style']  == 'Lambic - Unblended':
        val = 0
    elif row['beer_style']  == 'Berliner Weissbier':
        val = 0
    elif row['beer_style']  == 'Lambic - Fruit':
        val = 0
    elif row['beer_style']  == 'Kvass':
        val = 0
    elif row['beer_style']  == 'Lambic - Fruit':
        val = 0
    elif row['beer_style']  == 'Faro':
        val = 0
    elif row['beer_style']  == 'Gueuze':
        val = 0
    elif row['beer_style']  == 'Gose':
        val = 0
    elif row['beer_style']  == 'Sahti':
        val = 0
    elif row['beer_style']  == 'Bière de Champagne / Bière Brut':
        val = 0
    else:
        val = 1
    return val

#creates categories of beer ratings from 1-5
def review_categorizer(row):
    if row['review_overall'] <= 1:
        val = 1
    elif row['review_overall']  <= 2:
        val = 2
    elif row['review_overall']  <= 3:
        val = 3
    elif row['review_overall']  <= 4:
        val = 4
    else:
        val = 5
    return val

#performs functions to prepare dataset
def wrangle_beer():
    #acquires datasets from data.world
    df = get_beer()
    #creates columns for lager, barley, and categories of ratings
    df['is_lager'] = df.apply(find_lager, axis=1)
    df['is_barley'] = df.apply(find_barley, axis=1)
    df['review_cat'] = df.apply(review_categorizer, axis=1)
    #fills null mode value into ABV column
    df['beer_abv'].fillna(df['beer_abv'].mode()[0], inplace=True)
    #drops columns that aren't immediately useful to the project
    df = df.drop(columns=['review_profilename', 'brewery_name', 'brewery_id', 'review_time'], axis=1)

   

    return df

def split_data(df, test_size=.2, validate_size=.25, col_to_stratify=None, random_state=7):
    '''
    This splits data into test,train and validate data
    '''
    # This takes in a default variable or a variable to determine target variable for stratification
    if col_to_stratify == None:
    # this splits the data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,)
    else:                                                        
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df[col_to_stratify])
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,
                                       stratify=train_validate[col_to_stratify])
    return train, validate, test


def split_data(df, test_size=.2, validate_size=.25, col_to_stratify=None, random_state=7):
    '''
    This splits data into test,train and validate data
    '''
    # This takes in a default variable or a variable to determine target variable for stratification
    if col_to_stratify == None:
    # this splits the data
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state)
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,)
    else:                                                        
        train_validate, test = train_test_split(df, test_size=test_size, random_state=random_state, stratify=df[col_to_stratify])
        train, validate = train_test_split(train_validate,
                                       test_size=validate_size,
                                       random_state=random_state,
                                       stratify=train_validate[col_to_stratify])
    return train, validate, test