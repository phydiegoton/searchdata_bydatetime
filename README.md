# searchdata_bydatetime v1.0
This module is  used for datetime analysis of variables (plotting dates). It extracts a variable filtered by date in different ways. You could search by year "2005", year-month "2005-05", complete date like "2005-01-12". The search could be done through two paths, by selection of one date or by selection of an interval (two dates). For this module Datasets needs to be given, with a date variable in string format, and another target variable to start plotting by date or extract the dataframe by date.

# Usage Instructions
The module is compound of 5 conected functions. Allows cutting off the data by different range of dates, but currently only using "-" as separator, like "2021-12-30"
The functions set up are:
### - generate_date_columns(...)
This function generates new date columns with different criteria. This functions allows for the future search of date by diferent ranges.
### - search_data(...) 
This funtion returns two lists, the datetime list and the target variable of analysis.
### - create_df_from serach(...) 
This function creates the df given by the result of the search_data() function. Depending od the range selected de datetime columns is modified.
## High level usage functions.
### - get_df_from_search(...) 
This function is made of the above and returns the dataframe of the data searched/selected or selected by interval
### - show_graph(...) 
This fucntions also is made of the above non-high level functions. It make up the plotting of the data selected. For more infomation slide to the example
### - group_by_yearmonth_data(...)
This function is  made of the generate_date_columns(). Makes up group sum information by year, by month of the year, by month of the year sorted by month, and also a selection of the months of eache year to compare the evolution. For more information get into the Example usage of the function, mentioned below.
# Example Usage:
## Using the next Energy Consumption Dataset:
![image](https://user-images.githubusercontent.com/61083270/147823068-7ba693bc-7241-41bc-a703-f72c13d491d6.png)
## Function show_graph(...)
#### - show_graph(date0="2008-12-30" , frame=data, target_column_name="AEP_MW", column_date_name="Datetime", date1: "2009-01-01")
![image](https://user-images.githubusercontent.com/61083270/147822950-50f96063-733f-440b-a926-144d9a82bb1f.png)

date1 is only used if the inteval mode selector wants to be used. date1 is set by default for selecting one date by date0
#### - show_graph(date0="2008-08", frame=data, target_column_name="AEP_MW", column_date_name="Datetime")
![image](https://user-images.githubusercontent.com/61083270/147823241-c24a87a9-212d-49a2-a0cc-2c1371193dda.png)
#### - show_graph(date0="2005-08", frame=data, target_column_name="AEP_MW", column_date_name="Datetime",date1="2005-12")
![image](https://user-images.githubusercontent.com/61083270/147823279-994c2e34-f034-41f0-bb38-03ba4f63b9d4.png)
#### - show_graph(date0="2005-01-01", frame=data, target_column_name="AEP_MW", column_date_name="Datetime")
![image](https://user-images.githubusercontent.com/61083270/147823315-0c9e8e05-765b-481c-91a6-c5acd70ad78e.png)

For all those graphs the dataframes could also be asked with get_df_from_search() adding the same arguments as show_graph function. For more information about the entry arguments explore function.__doc__ at the command window.

## Function - group_by_yearmonth_data(frame,target_column_name,column_date_name,mode,month="all")
- group_by_yearmonth_data(frame=data,target_column_name="AEP_MW",column_date_name="Datetime",mode="year")
![image](https://user-images.githubusercontent.com/61083270/147839046-ff1e512c-97bd-4299-8b21-85f0569cccee.png)
- group_by_yearmonth_data(frame=data,target_column_name="AEP_MW",column_date_name="Datetime",mode="yearmonth")
![image](https://user-images.githubusercontent.com/61083270/147839117-2048a69d-96c8-436a-acd4-f0310947ab5d.png)
group_by_yearmonth_data(frame=data,target_column_name="AEP_MW",column_date_name="Datetime",mode="yearmonth_bymonth")
With those parameters, all the data by month is extracted 
![image](https://user-images.githubusercontent.com/61083270/147839133-900ad8c1-668c-4fa1-9f09-b10475c328cd.png)
With those parameters, all the data by month is extracted but sorted 
group_by_yearmonth_data(frame=data,target_column_name="AEP_MW",column_date_name="Datetime",mode="yearmonth_bymonth",month="11")
![image](https://user-images.githubusercontent.com/61083270/147839159-ebe5099c-d95f-4ef7-9f78-fb4f24cb7fdb.png)

With those parameters its only extacted the info of the month selected

# Requirements
This module is developed with Python 3.9 (should not be any problems).
# Packages
Packages used in the module are Pandas and Datetime
# Next version target improvements
- Enabling selecting by hourly data (if the initial dataset has  hourly dates data). For exmaple select all the "12:00:00" hourly data in the dataset
- Enabling formatting a rapid way to extract Semesters, Quarters
- At some point the code runs with lists, change it to arrays, for a more efficient run.
