#checks if a certain dict is in a csv file
import pandas as pd
csv_file_path='Book2.csv'

def check_email_in_csv(csv_file_path,thing_to_check):
    df=pd.read_csv(csv_file_path)
    emial_column='email'
    is_present=thing_to_check in df[emial_column].values
    return is_present
