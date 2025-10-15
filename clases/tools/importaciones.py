import pandas as pd

def importa_excel(f):
    df = pd.read_excel(f,skiprows=[0,1,3,4],index_col=0,parse_dates=True)
    return df