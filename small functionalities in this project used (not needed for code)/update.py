#code used to update values into a csv file
import pandas as pd

data = [{'name':'vij','email':'ranuj@gmail.com','password':678}
        
       ]
df = pd.DataFrame.from_dict(data)



output_file = '/Users/srikumark/Desktop/experimental/rvised/Book2.csv'


df.to_csv(output_file, index=False) 

print(f"Data has been written to {output_file}")




