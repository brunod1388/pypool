import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    load data from file
    '''
    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        print("File not found")
        return None
    print("the shape of data is:", data.shape)
    return data
