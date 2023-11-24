# customer.py

import pandas as pd

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
    print(customers.info())
    print("")
    print(customers.head())
    print("")

    # How many unique customers?
    print(f"Unique Customers: \n{customers.groupby('CustomerId').value_counts()}")
    print("")

    # How many unique pageId's
    pageId_unique = customers['PageId'].nunique()
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

    customers_day1 = customers[customers[time_parm] == time1]
    customers_day1_set = set()
    for c in customers_day1.itertuples():
        customers_day1_set.add(c[2])

    customers_day2 = customers[customers[time_parm] == time2]
    customers_day2_set = set()
    for c in customers_day2.itertuples():
        customers_day2_set.add(c[2])

    # These are the customer id's for customers that visited the websites on both days
    customers_both_days = customers_day1_set.intersection(customers_day2_set)
    print(f"customers_both_days: \n{customers_both_days}")
    print("")
    return customers_both_days


def customer_query(df, query_construction):
    customers_loyal = df.query(query_construction)[["CustomerId", "PageId"]]
    print(customers_loyal.info())
    print("")
    return customers_loyal

# ********* Analysis ************************************************

# read in specific data
customers = pd.read_csv("customer.csv", header=0, sep="\t")


# print data relevant to data exploration
output_raw_data(customers)


# ******* First, find the customers that have visits to the websites on both day1 and day2 *******
customers_both_days = both_days("Timestamp", "day1", "day2")


# setup an intermediate dataframe and fill with customers_both_days data
# loyal customers visited on both days
query_construction = 'CustomerId in @customers_both_days'
customers_loyal = customer_query(customers, query_construction)
print(f"customers_loyal: \n{customers_loyal}")


# ******* Secondly, select the customers that have duplicate website visits AND also have visits on both days *******
#  we now have the very loyal customers
customers_very_loyal_filter = customers_loyal.duplicated(keep=False)
print(customers_very_loyal_filter)
print("")

customers_very_loyal = customers_loyal[customers_very_loyal_filter]
print(f"customers_very_loyal: \n{customers_very_loyal}")
print(customers_very_loyal.info())
print("")

# now, find the unique customer id's for the very loyal customers *******
#   note that CustomerId = 17 is eliminated: it does not have a duplicate website
s = set()
for cust in customers_very_loyal.itertuples():
    s.add(cust[1])
print(f"very loyal customer Id's: \n{s}")
print("")

# ******* Finally, choose the most loyal customers by constructing a dataframe that has only the most loyal customers *******
query_construction = 'CustomerId in @s'
customers_most_loyal = customer_query(customers_loyal, query_construction)
print(f"customers_most_loyal: \n{customers_most_loyal}")
print("")

# Finally, from the most loyal customer, choose THE customers that also have a unique website page visit :
#    the customer has visits to the website on both days
#    the customer has repeat visits to some websites
#    the customer has a unique visit to a website:  find the set of customers that don't have duplicated data
THE_customers_filter = customers_most_loyal.duplicated(keep=False)
THE_customers = customers_most_loyal[~THE_customers_filter]  # see the "not" filter in this line
print(f"THE_customers: \n{THE_customers}")
print("")
#
#  *************************************** Finished ********************************************************
