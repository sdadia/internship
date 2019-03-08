# imports
import pandas as pd
import numpy as np


def convert_to_date(data, column_list, date_format=None):
    """
	Converts column(s) from string to datetime64[ns] in pandas

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert from string to datetime

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed for those columns
	"""
    # convert columns_names to a list, if its already not a list
    # if not isinstance(column_list, list):
    #     column_list = list(column_list)
    for column in column_list:
        data[column] = pd.to_datetime(data[column], infer_datetime_format=True)

    # return data


def convert_to(data, column_list, new_type):
    '''
	Generic function to converts column(s) to generic type of "str", "int", "float", "category"

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert from string to datetime
	new_type : String
	        The new types that you want to convert to.

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed for those columns
    '''
    if not isinstance(column_list, list):
        column_list = [column_list]

    for col in column_list:
        data[col] = data[col].astype(dtype=new_type)

    # return data


def convert_to_float32(data, column_list):
    '''
	Converts column(s) to float32

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert to 

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed to float32
    '''
    # convert columns_names to a list, if its already not a list
    if not isinstance(column_list, list):
        column_list = [column_list]

    for col in column_list:
        data[col] = data[col].astype(dtype=np.float32)

    # return data


def convert_to_int32(data, column_list):
    '''
	Converts column(s) to int32

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert to 

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed to int32
    '''
    # convert columns_names to a list, if its already not a list
    if not isinstance(column_list, list):
        column_list = [column_list]

    for col in column_list:
        data[col] = data[col].astype(dtype=np.int32)

    # return data


def convert_to_string(data, column_list):
    ''' 
	Converts column(s) to string type

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert.

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed to string
    '''
    # convert columns_names to a list, if its already not a list
    if not isinstance(column_list, list):
        column_list = [column_list]

    for col in column_list:
        data[col] = data[col].astype(str)

    # return data


def convert_to_category(data, column_list):
    ''' 
	Converts column(s) to string type

	Parameters
	----------
	data : Pandas dataframe
	    The data frame of panas
	column_list : List
	        The names of columns which you want to convert.

	Returns
	-------
	data : Pandas dataframe
	    Same pandas dataframe with the type changed to string
    '''
    # convert columns_names to a list, if its already not a list
    if not isinstance(column_list, list):
        column_list = [column_list]

    for col in column_list:
        data[col] = data[col].astype('category')

    # return data

