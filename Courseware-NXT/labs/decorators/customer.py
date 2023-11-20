# customer.py

import pandas as pd

customers = pd.read_csv("customer.csv", header=0, sep="\t")

print(customers)
print("")

customers_group = customers.groupby("Timestamp")

customers_counts = customers_group.value_counts()
print(customers_counts)

customers_duplicates_customerId = customers.duplicated(["customerId"], keep=False)
print(customers_duplicates_customerId)
print("")
# customers_Id = customers[customers_duplicates_customerId]
# print(customers_Id.Timestamp == 'day1' and customers_Id.Timestamp == 'day2')

# customers_Id = customers_Id[customers_Id[["Timestamp"]] == "day1" and customers_Id[["Timestamp"]] == "day2"]
# # print(customers_Id)
# print("")

# customers_Id_count = customers_Id.value_counts()
# print(customers_Id_count)
# print("")
# customer_filter = customers_Id.duplicated("pageId", keep=False)
# customer_unique = customers_Id[~customer_filter]
# print(customer_unique)



