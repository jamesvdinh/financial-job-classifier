import pandas as pd

if __name__ == '__main__':
    # Read txt file into pd dataframe
    df = pd.read_csv("(Copy) org_role_100K.txt", sep='\t')
    print(df)

    srt_by_org = df.sort_values(by=["org"])
    bofa = df[df["org"] == "Bank of America"].sort_values(
        by=["cnt"], ascending=True)
    print('Bank of America Roles:\n', bofa.head(50))
    print("# of roles:", len(bofa))
