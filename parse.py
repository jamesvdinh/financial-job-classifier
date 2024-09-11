import pandas as pd

if __name__ == '__main__':
    # Read txt file into pd dataframe
    df = pd.read_csv("(Copy) org_role_100K.txt", sep='\t')
    print(df)
