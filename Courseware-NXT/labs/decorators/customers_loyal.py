# customers_loyal.py

import pandas as pd

# input file path
path = "customer.csv"

def load_df(path=path, header=None, sep=None, rename_map=None, extra=None):
    df = pd.read_csv(path, header=header, sep=sep, na_values='NA')
    df.rename(columns=rename_map, inplace=True, errors='raise')

    # print data relevant to data exploration
    output_raw_data(df)

    # df = filter_test_records(df)  # preliminary filters for the dataframe
    # if extra:
    #     df = extra(df)
    return df[list(rename_map.values())]

def output_raw_data(df):
    """
    data to standard output

    Parameters
    ----------
    df  DataFrame

    Returns
    -------
    No Returns
    """
    print(df.info())
    print("")
    print(df.head())
    print("")

    # How many unique customers?
    print(f"Unique Customers: \n{df.groupby('customer_id').value_counts()}")
    print("")

    # How many unique pageId's
    pageId_unique = df['page_id'].nunique()
    print(f"Unique PageId's: \n{pageId_unique}")
    print("")


def both_days(time_parm, time1, time2):
    """
    Routine to find the customers id's that access websites on both days

    Parameters
    ----------
    time_parm: data column of interest
    time1: first day
    time2: second day

    Returns
    -------
    customers_both_days: customers that access a website on both days.
    """

    # customers that access a website page on day 1
    customers_day1 = customers[customers[time_parm] == time1]
    customers_day1_set = set(customers_day1["customer_id"])

    # customers that access a website page on day 2
    customers_day2 = customers[customers[time_parm] == time2]
    customers_day2_set = set(customers_day2["customer_id"])

    # Customer id's for customers that visited the websites on both days
    customers_both_days = customers_day1_set.intersection(customers_day2_set)
    print(f"customers_both_days: \n{customers_both_days}")
    print("")
    return customers_both_days


def customer_query(df, query_construction, list=list):
    customers_loyal = df.query(query_construction)[list]
    print(customers_loyal.info())
    print("")
    return customers_loyal

# ********* Analysis **********************************************************************
# *****************************************************************************************

rename_map = {"Timestamp": "timestamp", "CustomerId": "customer_id", "PageId": "page_id"}
header = 0
sep = "\t"

# read in specific data
customers = load_df(path, header=header, sep=sep, rename_map=rename_map, extra=None)


# ******* First, find the customers that have visits to the websites on both day1 and day2 *******
customers_both_days = both_days("timestamp", "day1", "day2")


# setup an intermediate dataframe and fill with customers_both_days data
# loyal customers visited on both days
query_construction = 'customer_id in @customers_both_days'
tcolumns = ["customer_id", "page_id"]
customers_loyal = customer_query(customers, query_construction, list=tcolumns)
print(f"customers_loyal: \n{customers_loyal}")


# ******* Secondly, select the customers that have duplicate website visits AND also have visits on both days *******
#  we now have the very loyal customers
customers_very_loyal_filter = customers_loyal.duplicated(keep=False)
# print(customers_very_loyal_filter)
print("")
customers_very_loyal = customers_loyal[customers_very_loyal_filter]
print(f"customers_very_loyal: \n{customers_very_loyal}")
print(customers_very_loyal.info())
print("")

# now, find the unique customer id's for the very loyal customers *******
#   note that customer_id = 17 is eliminated: it does not have a duplicate website visit
set_very_loyal_customers = set()
for cust in customers_very_loyal.itertuples():
    set_very_loyal_customers.add(cust[1])
print(f"very loyal customer Id's: \n{set_very_loyal_customers}")
print("")

# ******* Finally, choose the most loyal customers by constructing a dataframe that has only the most loyal customers *******
query_construction = 'customer_id in @set_very_loyal_customers'
customers_most_loyal = customer_query(customers_loyal, query_construction, list=tcolumns)
print(f"customers_most_loyal: \n{customers_most_loyal}")
print("")

# Finally, from the most loyal customer, select THE customers that also have a unique page website visit :
#    the customer has visits to the website on both days
#    the customer has repeat visits to some websites
#    the customer has a unique visit to a website:  find the set of customers that don't have duplicated data
THE_customers_filter = customers_most_loyal.duplicated(keep=False)
THE_customers = customers_most_loyal[~THE_customers_filter]  # see the "not" filter in this line
print(f"THE_customers: \n{THE_customers}")
print("")
#
#  *************************************** Analysis: Finished **********************************************
#  *********************************************************************************************************
