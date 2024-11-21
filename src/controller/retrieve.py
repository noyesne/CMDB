import pandas as pd
import os 
def _gather_info_(e1, e2):
    
    #cwd = os.chdir("../model")
    
    df = pd.read_csv("src\\model\\Test_Data_1.csv")
    print(df)
    specific_data = df.loc[df["Part Number"] == e1, ['RSA KEY (public)', 'RSA KEY (private)', 'AES KEY', 'SHA_256']]
    print("OUTPUT: \n", specific_data)