import pandas as pd

def load(path: str, icol=None) -> pd.DataFrame:
    '''
    load data from file
    '''
    try:
        data = pd.read_csv(path, index_col=icol)
    except FileNotFoundError:
        print("File not found")
        return None
    print("the shape of data is:", data.shape)
    return data