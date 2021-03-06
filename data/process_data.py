import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    - Take two csv files 
    - Load them and save as pandas dataframe
    - Returns dataframe merged with both files
    
    Args: 
    - messages_filepath: str  
    - categories_filepath: str

    Returns:
    - merged dataframe: pd.DataFrame
    """
    messages = pd.read_csv(messages_filepath)
    
    categories = pd.read_csv(categories_filepath)
    
    df = messages.merge(categories, on='id', how = 'inner')

    return df 


def clean_data(df):
    """
    Clear the dataframe and return it.
    """
    # creating a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';', expand=True)
    #renaming the categories columns
    row = categories.iloc[0,:].copy()
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames

    #converting the values of string to just 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1] 
        categories[column] = categories[column].astype(int)


    # Replace rows with a related value of 2 from the dataset
    categories['related'].replace({2: 0}, inplace=True)

    # Drop child_alone from categories dataframe.
    categories.drop('child_alone', axis = 1, inplace = True)

    df.drop('categories', axis=1, inplace=True)

    df = pd.concat([df, categories], axis = 1)

    # drop duplicates
    df = df.drop_duplicates()
        
    return df


def save_data(df, database_filename):
    """
    Saves dataframe as sql file
    """
    engine = create_engine('sqlite:///' + database_filename)
    
    df.to_sql('disaster_response', engine, index=False, if_exists = 'replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()