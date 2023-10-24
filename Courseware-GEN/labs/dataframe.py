# dataframe.py

import pandas as pd

path = "stack-overflow-developer-survey-2023/survey_results_public.csv"


def filter_test_records(dframe):
    """

    :param dframe:
    :return: DataFrame
    """


    return dframe


def load_df(path, rename_map, extra=None):
    df = pd.read_csv(path)
    df.rename(columns=rename_map, inplace=True, errors='raise')
    df = filter_test_records(df)  # common filters for all dataframes
    if extra:
        df = extra(df)
    return df[list(rename_map.values())]


def load_survey_df(path):
    rename_map = {
        'MainBranch': 'Developer_Type',
        'Age': 'Age_Range',
        'EdLevel': 'Education_Level',
        'LearnCode': 'Learning_Code',
        'YearsCode': 'Years_Coding'
    }

    def extra_filter(df):
        extra_mapping = {'Less than 1 year': 0.5, 'More than 50 years': 50, 'NA': 0, 'NaN': 0}
        df.replace({'Years_Coding': extra_mapping}, inplace=True)
        # df['Years_Coding'] = df['Years_Coding'].astype(pd.Int64Dtype())
        df['Years_Coding'] = df['Years_Coding'].astype(float)
        df_new = df[df['Years_Coding'] >= 2.0]
        return df_new

    return load_df(path, rename_map, extra=extra_filter)


df = load_survey_df(path)
print(df.head())
print(df.describe())