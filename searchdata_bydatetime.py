# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:32:17 2021
(Feliz cumpleañosss!!)
@author: Diego

Este código srive para navegar a lo largo de un dataset de fecha y otro tipo d
de valor. Se hace bsuqedas por selección de fecha como 2004-12-01 o 2005 o 
2005-12. O bien se hace la busqueda a estableciendo un intervalo,
date0: 2020-01-12 , date1: 2020-02-12. Solo permite graficas de 2 variables

Puntos a mejorar:
    - Que la selección permita seleccionar por fecha y hora
    - Mas personalización para la graficación
    - Hay momentos que se trabaja con lista, mejor trabajar con arrays
"""
import pandas as pd
from datetime import datetime

import numpy as np   
    
def generate_date_columns(frame,column_date_name):
    """Doctrising: Esta función añade columnas de  interes a un dataframe existente, las columnas que se operan son de fecha. 
        Esta pensada para recibir datos en formato string.
        frame: datos de entrada con alguna columna con datos en formato fecha str
        column_date_name: Nombre de la columna con datos de fecha str iniciales con la que se va a trabajar"""            
    #NOTA: El nombre las columnas nuevas es escrito con _ para que de ninguna manera coincida con columnas de data original
    frame=frame.copy()
    frame["Date_String_"]=frame[column_date_name].apply(lambda x: x.split()[0]) # Nueva columna con solo los datos de fecha (sin horas) str
    frame["Datetime_/Y/M/D_"]=frame["Date_String_"].apply(lambda x : datetime.strptime(x,'%Y-%m-%d'))# Nueva columna con solo datos en fecha (sin horas) datetime
    frame["Year_"]=frame["Date_String_"].apply(lambda x: x[:4]) #Nueva columna, solo con datos de año, str
    frame["Year_Month_"]=frame["Date_String_"].apply(lambda x: x[:7]) #nueva columna, solo con datos año y mes, str 
    frame["Month_"]=frame["Date_String_"].apply(lambda x: x[5:7])       
    if len(frame[column_date_name][0])>10: #Se hace la comporbación del dato incial con un dato (Podría ser interesante hacerlo con todos)  
        frame["Datetime_original"]=frame[column_date_name].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))# nueva columna si los datos recibidos (str) vienen con horas, todo se pasa a datetime
        #Se pasa a datetime para poder ordenar los valores con el siguiente comando
    else:
        frame["Datetime_original"]=frame[column_date_name].apply(lambda x: datetime.strptime(x,'%Y-%m-%d'))
    result=frame.sort_values(by="Datetime_original")
    return result
    
                                                               



def search_data(date0,frame,target_column_name,column_date_name,date1):
    """Doctrising: Esta función es el corazon del programa, sirve para segmentar los datos. Existen dos modus operandi: 
        1) Seleccionando una fecha concreta en date0, e ignorado date1 (Aquí no hay Default en date1 pues es una función intermedia
        (en la función final si qeu se establece date1 como default)). 2) Estableciendo un intervalo con date0 y date1"""
    frame=generate_date_columns(frame, column_date_name)
    assert type(date0)==str # Se aegura que date0 tiene fromato str
    assert type(date1)== bool or str #Se asegura de que date1 es un booleano o un str
    assert type(target_column_name)==str #Se asegura que el nombre de la columna target es str
    #1) Por selección unica de fecha
    if date1 == False: #Este es el switch para dieferenciar selección unica de fecha o por intervalo 
        if len(date0) == 10:# Para busqueda por día %Y-%m-%d
            data_base = frame.groupby("Date_String_")[target_column_name].apply(list).to_dict()# Esta función genera el diccionario a traves del cual se hace la busqueda
            data_base_date = frame.groupby("Date_String_")[column_date_name].apply(list).to_dict()
            return data_base[date0] ,[x[11:] for x in data_base_date[date0]]        
        elif len(date0) == 4: # Para busqueda por año %Y
            data_base=frame.groupby("Year_")[target_column_name].apply(list).to_dict()          
            data_base_date=frame.groupby("Year_")[column_date_name].apply(list).to_dict()
            return data_base[date0], data_base_date[date0]
        elif len(date0)== 7: # Para busqueda por mes del año
            data_base=frame.groupby("Year_Month_")[target_column_name].apply(list).to_dict()
            data_base_date=frame.groupby("Year_Month_")[column_date_name].apply(list).to_dict()
        
            return data_base[date0],data_base_date[date0]
    #2) Por intervalo de fecha
    if type(date1)==str: # Se ejecuta su date1 es formato str
        if len(date0)==4: # Se reescribe date0 y date1 (cuadno se introduce año) para poder operar con ello. Ejemplo: Se escribe 2020, se tranforma a una fecha entera 2020-01-01 por ejemplo
            date0=date0+"-01-01"
            date1=date1+"-12-31"
        elif len(date0)==7: # Se reescribe date0 y date1 (cuadno se introduce año y mes) para poder operar con ello. Ejemplo: Se escribe 2020-01, se tranforma a una fecha entera 2020-01-01 por ejemplo
            date0=date0+"-01"
            date1=date1+"-31"
        #Se indeza una columna con formato datetime, pues es mas comodo seleccionar así un intervalo
        frame.index=frame["Datetime_/Y/M/D_"]
        frame_data=frame.loc[date0:date1] #Aquí se selecciona el intervalo dado por date0 y date1 
        frame_data.index=frame_data["Date_String_"] # Se sustituye ahora por el indice en formato str
        frame_data.index.name="Dates_string_index" # Se establece un nombre al indice
        data_base=frame_data.groupby("Date_String_")[target_column_name].apply(list) #Se genera un array con las listas de los valores target de los dias/horas
        data_base_date=frame_data.groupby("Date_String_")[column_date_name].apply(list)#Se genera un array con las listas de los valores fecha de los dias/horas
        #En el siguiente trozo de codigo se procesan los datos de las dos lineas anteriores
        # Se porcesan para obtener una lista con todos los datos ordenados, pues antes se tenia un array de listas
        result_data=[]
        result_date=[]
        for i in range(0,len(data_base.values)):
            result_data.extend(data_base.values[i]) 
        for i in range(0,len(data_base_date.values)):
            result_date.extend(data_base_date.values[i]) 
        
        result_frame=pd.DataFrame(result_data,columns=[target_column_name])
        result_frame.index=result_date
        
        
        return result_data,result_date
        
         
def create_df_from_search(search_data_result,target_column_name):
        """Doctrising: Esta función forma parte del proceso como paso intermedio para graficar la selección de datos. 
            Su función es la de genera un dateframe con la infromación de la función anterior "serach_data" que daba resultado a info en
            ormato lista.
            search_data_result: Se tiene que introducri el resultado de la función search_data"""       
        frame_created=pd.DataFrame(search_data_result[0],columns=[target_column_name]) # Se crea un dataframe con los datos target
        frame_created.index=search_data_result[1] # El indice se asigna a los datos fecha de la función anterior "search_data"
        #El siguiente trozo de código Esta relacionado con la graficación. con la visulaización del eje x
        if len(search_data_result[0])>24: # Afecta solo a los que tiene datos superiores a 1 dia. Es decir para los dato de 1 dia se jace de otra manera
            frame_created['Date_string_']=search_data_result[1]
            frame_created.index=frame_created['Date_string_'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
            del(frame_created['Date_string_'])
        return frame_created
            
            
    
def show_graph(date0,frame,target_column_name,column_date_name,date1=False):
    """Doctrising: date0: fecha inicial (formato obligado con guiones -, Se aceptan 2005-12,2005-12-01 y 2000)
    date1= Es la fecha final. Se utiliza para hcer busqueda por intervalo y no por selección
    frame: Tiene que ser un dataframe que contenta una columna en string con formato (/%Y-%m-%d (se pueden incluir la horas))
    target_column_name: Es el nombre de la columna que se quiere graficar
    column_date_name: Es el nombre de la columna de datos fecha"""
    final_data=search_data(date0, frame, target_column_name, column_date_name,date1)
    created_dataframe=create_df_from_search(final_data,column_date_name)
    return created_dataframe.plot(xlabel=column_date_name,ylabel=target_column_name,legend=False) #Aqui modifico las opciones de la visualizacion
        
def get_df_from_search(date0,frame,target_column_name,column_date_name,date1=False):
    """Doctrising: date0: fecha inicial (formato obligado con guiones -, Se aceptan 2005-12,2005-12-01 y 2000)
    date1= Es la fecha final. Se utiliza para hcer busqueda por intervalo y no por selección
    frame: Tiene que ser un dataframe que contenta una columna en string con formato (/%Y-%m-%d (se pueden incluir la horas))
    target_column_name: Es el nombre de la columna que se quiere graficar"""
    final_data=search_data(date0, frame, target_column_name, column_date_name,date1)
    created_dataframe=create_df_from_search(final_data,column_date_name)
    return created_dataframe
           
def group_by_yearmonth_data(frame,target_column_name,column_date_name,mode:str,month="all"):
    """Doctrising: Esta función genera dataframes distintos tipos.
    1) Un data frame agrupado por año con la suma y la media y pct cambio previo -> mode="year"
    2) Un dataframe agrupado por meses del año con la suma, media y pct cambio -> mode= "yearmonth"
    3) Un dataframe de los meses de todos los años, es decir agrupa todos los eneros o febreros de los años
    mode="yearmonth_bymonth"
    month-> "all" (Para obtener todo los yearmonth ordenados) (Es Default)
    month-> "xx" Se selecciona el buscado para todos los años"""
                    
    assert mode== "year" or "yearmonth"or "yearmonth_bymonth"
    frame=generate_date_columns(frame, column_date_name)#Se hace uso de las columnas generadas date
    if mode=="year":  #Para obtener datos totales por año
        #Obtener la columna sum
        data_grouped_by_year_sum=frame.groupby("Year_")[target_column_name].apply(sum) 
        data_grouped_by_year_sum=pd.DataFrame(data_grouped_by_year_sum)
        data_grouped_by_year_sum.columns=[f"SUM {target_column_name}"]
        #Obtener el pct change de sum
        data_grouped_by_year_sum["PCT Change SUM"]=data_grouped_by_year_sum.pct_change()
        #Obtener la columna mean
        data_grouped_by_year_mean=frame.groupby("Year_")[target_column_name].apply(np.mean)
        data_grouped_by_year_mean=pd.DataFrame(data_grouped_by_year_mean)
        data_grouped_by_year_mean.columns=[f"Mean per hour {target_column_name}"]
        #Obtener el pct_change de mean
        data_grouped_by_year_sum["PCT Change Mean"]=data_grouped_by_year_mean.pct_change()
        #Unir las columnas mean y sum
        data_grouped_by_year=pd.concat([data_grouped_by_year_sum,data_grouped_by_year_mean],axis=1) 
        #Modificar el orden de las columnas
        data_grouped_by_year=data_grouped_by_year[[f"SUM {target_column_name}","PCT Change SUM",f"Mean per hour {target_column_name}","PCT Change Mean"]]
        return data_grouped_by_year
    elif mode=="yearmonth" or "yearmonth_bymonth": #Para obtener datos totales por mes del año
        #Obtener la columna sum
        data_grouped_by_year_sum=frame.groupby("Year_Month_")[target_column_name].apply(sum) 
        data_grouped_by_year_sum=pd.DataFrame(data_grouped_by_year_sum)
        data_grouped_by_year_sum.columns=[f"SUM {target_column_name}"] 
        #Obtener el pct change de sum
        data_grouped_by_year_sum["PCT Change SUM"]=data_grouped_by_year_sum.pct_change()
        #Obtener la columna mean
        data_grouped_by_year_mean=frame.groupby("Year_Month_")[target_column_name].apply(np.mean)
        data_grouped_by_year_mean=pd.DataFrame(data_grouped_by_year_mean)
        data_grouped_by_year_mean.columns=[f"Mean per hour {target_column_name}"]
        data_grouped_by_year_mean["PCT Change Mean"]=data_grouped_by_year_mean.pct_change()
        # Se unen las dos columnas
        data_grouped_by_year=pd.concat([data_grouped_by_year_sum,data_grouped_by_year_mean],axis=1)  
        #Se edita el nombre de las columnas
        data_grouped_by_year=data_grouped_by_year[[f"SUM {target_column_name}","PCT Change SUM",f"Mean per hour {target_column_name}","PCT Change Mean"]]
        if mode=="yearmonth_bymonth": #Para obtener datos totales por mes del año ordenados por mes
            # Se restablece el indice para operar con los datos de la columna indice
            data_grouped_by_year=data_grouped_by_year.reset_index()
            #Se genera la columna Month que servira para ordenar los valores por ella
            data_grouped_by_year["Month_"]=data_grouped_by_year["Year_Month_"].apply(lambda x: int(x[5:7]))
            #Se genera la columna Year que servira tambien para ordenar los valores
            data_grouped_by_year["Year_"]=data_grouped_by_year["Year_Month_"].apply(lambda x: int(x[:4]))
            #Se ejecuta la ordenación por mes y por año 
            data_grouped_by_year=data_grouped_by_year.sort_values(by=["Month_","Year_"])
            data_grouped_by_year.index=data_grouped_by_year["Year_Month_"]
            #Se borran la variables intermedias del proceso para depurar el dato final
            del(data_grouped_by_year["Year_Month_"])
            del(data_grouped_by_year["Month_"])
            del(data_grouped_by_year["Year_"])
            #data_grouped_by_year.index=data_grouped_by_year["Year_Month_"].apply(lambda x: datetime.strptime(x,"%Y-%M"))
            if month=="all": #Para obtener datos totales por mes del año ordenados por mes
                return data_grouped_by_year
            else: #Para obtener datos totales por mes del año pero solo de la seleccion del mes
                assert len(month)==2
                #Se restablece el indice para operar con sus datos
                data_grouped_by_year=data_grouped_by_year.reset_index()
                #Se genera la columna Month a traves de la columna que previamente era indice
                data_grouped_by_year["Month_"]=data_grouped_by_year["Year_Month_"].apply(lambda x: x[5:7])
                #Se aplica al dataframe una filtro de mes dado por month
                data_grouped_by_year=data_grouped_by_year[data_grouped_by_year["Month_"]==month]
                data_grouped_by_year.index=data_grouped_by_year["Year_Month_"]
                #Se eliminan las varibles intermedias creadas para depurar el dato final
                del(data_grouped_by_year["Month_"])
                del(data_grouped_by_year["Year_Month_"])
                return data_grouped_by_year
        else: # Devuelve la ejecución para yearmonth
            return data_grouped_by_year
 
    