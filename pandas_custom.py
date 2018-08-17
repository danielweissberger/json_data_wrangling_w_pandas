


#Group a dataframe by an attribute, aggregate by count and sort
def group_and_sort_df_by_count(attr, df):
    df_count = df.groupby(attr).count()
    df_count.columns = ['count']
    return df_count.sort_values(by='count', ascending=False)


#create a dictionary mappping from two columns in a dataframe
def create_dict_from_columns(column1_name, column2_name, df):
    return {row[column1_name]:row[column2_name] for index, row in df.iterrows()}