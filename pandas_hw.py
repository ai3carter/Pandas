# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:17:52 2019

@author: ai3ca
"""

import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

tp=len(purchase_data["SN"].unique())
player=pd.DataFrame({"Total Players":[tp]})
player

unique_items=len(purchase_data["Item ID"].unique())
avg_price=purchase_data["Price"].mean()
purchases=purchase_data["Item ID"].count()
revenue=purchase_data["Price"].sum()

analysis_df=pd.DataFrame({"Number of Unique Items":[unique_items],
                          "Average Price":[avg_price],
                          "Number of Purchases":[purchases],
                          "Total Revenue":[revenue]})
analysis_df

gender_group=purchase_data.groupby(["Gender"])

total_count=gender_group["SN"].nunique()
percentage_of_player=(total_count/tp)*100


gender=pd.DataFrame({"Total Count":total_count,"Percentage of Players":percentage_of_player},
                    index=["Male","Female","Other/Non-Disclosed"])
gender

purchase_count=gender_group["Purchase ID"].count()
avg_purchase_price=gender_group["Price"].mean()

#print(purchase_count)
#print(avg_purchase_price)
total_purchase_value=gender_group["Price"].sum()
avg_total_purchase_per_person=total_purchase_value/total_count

gender_df=pd.DataFrame({"Purchase Count":purchase_count,
      "Average Purchase Price":avg_purchase_price,
      "Total Purchase Value":total_purchase_value,
      "Avg Total Purchase per Person":avg_total_purchase_per_person})


gender_df

purchase_data["Age"].max()  ##45
purchase_data["Age"].min()  ##7


bins=[0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,100]
group_names=["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
purchase_data["Age_Summary"]=pd.cut(purchase_data["Age"],bins,labels=group_names)

age=purchase_data.groupby("Age_Summary")
total_count_agegroup=age["SN"].nunique()
percentage_of_agegroup=(total_count_agegroup/tp)*100

age_demo=pd.DataFrame({"Total Count":total_count_agegroup,"Percentage of Players":percentage_of_agegroup})
age_demo

purchase_count_age=age["Purchase ID"].count()
avg_purchase_price_age=age["Price"].mean()

#print(purchase_count_age)
#print(avg_purchase_price_age)
total_purchase_value_age=age["Price"].sum()
avg_total_purchase_per_person_age=total_purchase_value_age/total_count_agegroup

age_df=pd.DataFrame({"Purchase Count":purchase_count_age,
      "Average Purchase Price":avg_purchase_price_age,
      "Total Purchase Value":total_purchase_value_age,
      "Avg Total Purchase per Person":avg_total_purchase_per_person_age})


age_df



top_spender=purchase_data.groupby(["SN"])
purchase_count_tp=top_spender["Purchase ID"].count()
avg_purchase_price_tp=top_spender["Price"].mean()

total_purchase_value_tp=top_spender["Price"].sum()

top_spender_demo=pd.DataFrame({"Purchase Count":purchase_count_tp,
      "Average Purchase Price":avg_purchase_price_tp,
      "Total Purchase Value":total_purchase_value_tp})

clean_ts=top_spender_demo.sort_values(["Total Purchase Value"],ascending=False).head()
clean_ts


purchase_data[["Item ID","Item Name","Price"]].head()

item=purchase_data[["Item ID","Item Name","Price"]]
item_group=item.groupby(["Item ID","Item Name"])

purchase_count_p=item_group["Price"].count()
total_purchase_value_p=item_group["Price"].sum()

item_price_p=total_purchase_value_p/purchase_count_p


popular=pd.DataFrame({"Purchase Count":purchase_count_p,
      "Item Price":item_price_p,
      "Total Purchase Value":total_purchase_value_p})
#popular.head()
clean_p=popular.sort_values(["Purchase Count"],ascending=False).head()
clean_p

clean_p=popular.sort_values(["Total Purchase Value"],ascending=False).head()