import pandas as pd


def remove_outliers_IQR(_df, _colums):
    _df = _df.copy(deep=True)
    for _colum in _colums:
        Q1 = _df[_colum].quantile(0.25)
        Q3 = _df[_colum].quantile(0.75)
        IQR = Q3-Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        _df = _df[(_df[_colum]>= lower_bound) & (_df[_colum] <= upper_bound)]
        
    return _df

def count_outliers_IQR(_df, _colums):
    _df = _df.copy(deep=True)
    new_df = []
    for _colum in _colums:
        Q1 = _df[_colum].quantile(0.25)
        Q3 = _df[_colum].quantile(0.75)
        IQR = Q3-Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        _df_aux = _df[(_df[_colum]< lower_bound) | (_df[_colum] > upper_bound)]
        new_df.append([_colum, _df_aux[_colum].count(), (_df_aux[_colum].count()/_df[_colum].count())*100])
    
    # print(new_df)
    
    return pd.DataFrame(new_df, columns=['Colum', 'num_outliers', 'outlier_%']).sort_values("outlier_%", ascending=False)
