import pandas as pd
import os

data_dic = {"Name": ["Mohan","Ram","Jason"],
            "Age": [27,25,29],
            "City": ["GUJ","MUM","NSk"]
}

df = pd.DataFrame(data_dic)

data_dir = "data"
os.makedirs(data_dir,exist_ok = True)

# define the file path
file_path = os.path.join(data_dir,"sample_data.csv")

# save the dataframe to csv file, including column names
df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")