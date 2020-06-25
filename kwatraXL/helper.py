import pandas as pd


def clean_df(df):
    df = df.dropna(how='all', axis=1).dropna(how='all', axis=0).fillna('')
    df = df.applymap(str)
    df.columns = df.columns.astype(str)
    return df

def get_data_dict(filepath):
    xl_file = pd.ExcelFile(filepath)
    data_dict = pd.read_excel(xl_file, None)
    for sheet in data_dict:
        data_dict[sheet] = clean_df(data_dict[sheet])
    return data_dict




def get_df_labels(df, sep):
    sep = ' '+sep+' ' 
    col_head_dict = fill_cols(df)[0]
    dd_fields = []
    for key in col_head_dict:
        buff = ''
        for field in col_head_dict[key]:
            if field != '' and 'Unnamed:' not in field:
                if buff == '':
                    buff += field
                else:
                    buff += sep
                    buff += field
        dd_fields.append(buff)
    return dd_fields


def fill_cols(df):
    col_head_dict = {}
    skip_rows = 0
    for j in range(len(df.columns)):
        col_head_dict[j + 1] = [df.columns[j]]
    if col_check(col_head_dict):
        return col_head_dict, skip_rows
    else:
        for i in range(len(df)):
            for j in range(len(df.columns)):
                col_head_dict[j + 1].append(df.loc[df.index[i]][df.columns[j]])
            skip_rows += 1
            if col_check(col_head_dict):
                return col_head_dict, skip_rows


def col_check(col_head_dict):
    for col in col_head_dict:
        if len(set(col_head_dict[col])) < 1:
            return False
        if len(set(col_head_dict[col])) == 1 and (col_head_dict[col][0] == '' or 'Unnamed:' in col_head_dict[col][0]):
            return False
        if len(set(col_head_dict[col])) == 2 and (col_head_dict[col][0] == '' or col_head_dict[col][1] == '') and (
                'Unnamed:' in col_head_dict[col][0] or 'Unnamed:' in col_head_dict[col][1]):
            return False
    return True

