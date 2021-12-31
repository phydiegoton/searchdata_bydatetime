# searchdata_bydatetime v1.0
This module is  used for datetime analysis of variables (plotting dates). It extracts a variable filtered by date in different ways. You could search by year "2005", year-month "2005-05", complete date like "2005-01-12". The search could be done through two paths, by selection of one date or by selection of an interval (two dates). For this module Datasets needs to be given, with a date varibale in string format, and another target variable to start plotting by date or extract the dataframe by date.

# Usage Instructions
The module is compound of 5 conected functions. Allows the cutting of the data by different range of dates, but currently only using "-" as separator, like "2021-12-30"
The functions set up are:
### - generate_date_columns()
This function generates new date columns with different criteria. This functions allows for the future serach of date by diferent ranges.
### - search_data() 
This funtion returns two lists, the datetime list and the target variable of analysis.
### - create_df_from serach() 
This function creates the df given by the result of the search_data() function. Depending od the range selected de datetime columns is modified.
## High level usage functions.
### - get_df_from_search() 
This function is made of the above and returns the dataframe of the data searched/selected or selected by interval
### - show_graph() 
This fucntions also is made of the above non-high level functions. It make up the plotting of the data selected
# Example:
## Using the next dataset:
![image](https://user-images.githubusercontent.com/61083270/147823068-7ba693bc-7241-41bc-a703-f72c13d491d6.png)
#### show_graph(date0="2008-12-30" , frame=data, target_column_name="AEP_MW", column_date_name="Datetime", date1: "2009-01-01")
![image](https://user-images.githubusercontent.com/61083270/147822950-50f96063-733f-440b-a926-144d9a82bb1f.png)

date1 is only use if the inteval mode selector wants to be used. date1 is set by default fro selecting one date by date0
#### show_graph(date0="2008-08", frame=data, target_column_name="AEP_MW", column_date_name="Datetime")
![image](https://user-images.githubusercontent.com/61083270/147823241-c24a87a9-212d-49a2-a0cc-2c1371193dda.png)
#### show_graph(date0="2005-08", frame=data, target_column_name="AEP_MW", column_date_name="Datetime",date1="2005-12")
![image](https://user-images.githubusercontent.com/61083270/147823279-994c2e34-f034-41f0-bb38-03ba4f63b9d4.png)
#### show_graph(date0="2005-01-01", frame=data, target_column_name="AEP_MW", column_date_name="Datetime")
![image](https://user-images.githubusercontent.com/61083270/147823315-0c9e8e05-765b-481c-91a6-c5acd70ad78e.png)
# Requirements
This module is developed with Python 3.9 (should not be any problems).
# Packages
Packages used in the module are Pandas and Datetime

