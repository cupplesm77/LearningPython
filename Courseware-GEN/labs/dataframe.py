# dataframe.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "stack-overflow-developer-survey-2023/survey_results_public.csv"


def filter_test_records(df):
    """

    :param df:
    :return: DataFrame
    """
    print(df[['Age_Range',
              'Years_Coding',
              'Compensation_Total',
              'Work_Experience',
              'Compensation_Dollar_PerYear']].head())

    # compensation total drop null value rows
    df.dropna(subset=["Compensation_Dollar_PerYear"], inplace=True)

    # convert NaN to zero
    df.fillna(0, inplace=True)
    print('')

    # clean missing data and convert words to numbers in Years_Coding
    extra_mapping1 = {'Less than 1 year': 0.5, 'More than 50 years': 50}
    df.replace({'Years_Coding': extra_mapping1}, inplace=True)
    df['Years_Coding'] = df['Years_Coding'].astype(float)

    print(df.info())
    print('')

    return df


def load_df(path, rename_map, extra=None):
    df = pd.read_csv(path, na_values='NA')
    df.rename(columns=rename_map, inplace=True, errors='raise')
    df = filter_test_records(df)  # preliminary filters for the dataframe
    if extra:
        df = extra(df)
    return df[list(rename_map.values())]


def load_survey_df(path, analysis_flag):
    rename_map = {
        'MainBranch': 'Developer_Type',
        'Age': 'Age_Range',
        'EdLevel': 'Education_Level',
        'LearnCode': 'Learning_Code',
        'YearsCode': 'Years_Coding',
        'Country': 'Country',
        'Currency': 'Currency',
        'CompTotal': 'Compensation_Total',
        'WorkExp': 'Work_Experience',
        'ConvertedCompYearly': 'Compensation_Dollar_PerYear'
    }

    def extra_filter0(df):
        df_new = df[df['Years_Coding'] >= 4.0]  # stack overflow user is over a range of experience
        df2 = df_new[df_new['Years_Coding'] <= 50.0]
        df2.reset_index(drop=True, inplace=True)
        return df2

    def extra_filter1(df):
        df_new = df[df['Years_Coding'] >= 2.0]  # stack overflow user is relatively inexperienced
        df2 = df_new[df_new['Years_Coding'] <= 4.0]
        df2.reset_index(drop=True, inplace=True)
        return df2

    if analysis_flag == "experienced":
        f_obj = extra_filter0
    elif analysis_flag == "inexperienced":
        f_obj = extra_filter1
    else:
        f_obj = None

    return load_df(path, rename_map, extra=f_obj)


def plotdata(df, saveplot, miny=0.0, maxy=2.0e5):
    sns.set_theme(style='whitegrid')
    g = sns.lmplot(data=df,
                   x="Years_Coding",
                   y="Compensation_Dollar_PerYear",
                   scatter_kws={'s': 20},
                   line_kws={'color': 'orange'})
    g.fig.suptitle("Compensation vs Years of Coding Experience",
                   fontsize=11)
    # plt.title("Compensation vs Year of Coding")
    g.set(xlabel='Coding Experience (years)',
          ylabel="Compensation (US dollars)")
    plt.ylim(miny, maxy)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(3, 3))
    g.savefig(saveplot)
    plt.show()


def savedata(df, new_csv_path):
    df.to_csv(new_csv_path)

# experienced implies utilizing most of the original data range
# analysis_flag = "experienced"  # miny=0, maxy=2.0e5

# inexperience implies using data between years of experience 2 to 4
analysis_flag = "inexperienced" # miny=0, maxy 1.25e5

# None implies the full range of data 0 to >50 years
# analysis_flag = None  # miny=0, maxy=2.0e5

df = load_survey_df(path, analysis_flag)
savedata(df, 'stackoverflow_processed.csv')
plotdata(df, 'compensation.png', miny=0.0, maxy=1.25e5)

print(df.info())
df[['Age_Range',
    'Years_Coding',
    'Compensation_Total',
    'Work_Experience',
    'Compensation_Dollar_PerYear']].head(10)
print(df['Work_Experience'].value_counts())
print('')
print(df['Years_Coding'].value_counts())
