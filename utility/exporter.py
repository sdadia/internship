# imports
import pandas as pd
import numpy as np
import s3fs
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


def save_to_csv(data, location):
    ''' 
    Saves dataframe to CSV

    Parameters
    ----------
    data : Pandas dataframe
        The Pandas data frame which hsa to be saved
    location : string
            The path where you want to save it.

    Returns
    -------
    None
        '''
    data.to_csv(location, index=0)


def save_to_pickle(data, location):
    ''' 
    Saves dataframe to pickle

    Parameters
    ----------
    data : Pandas dataframe
        The Pandas data frame which hsa to be saved
    location : string
            The path where you want to save it.

    Returns
    -------
    None
    '''
    data.to_pickle(location)
    return None


def save_to_parquet(data, location):
    ''' 
    Saves dataframe to pickle

    Parameters
    ----------
    data : Pandas dataframe
        The Pandas data frame which hsa to be saved
    location : string
            The path where you want to save it.

    Returns
    -------
    None
    '''
    data.to_parquet(location, index=None)
    return None




def save_to_postgres(data, table_name, username, password, host, database, port=5432, mode="append"):
    ''' 
    Saves dataframe to postgres as table

    Parameters
    ----------
    data : Pandas dataframe
        The Pandas data frame which hsa to be saved
    table_name : string
            The name of the table you want it to be called
    username : string
            The username to be used
    password : string
            The password for that username
    database: string
            The password for that specific user
    port : int (default = 5432)
            The port number on which we can access the database
    mode : string (default = 'append')
            Options are : 'append' 'replace' 'fail'
            append : If the table_name already exist, then the data is appended
            replace : If the table_name already exist, then the data is completely overwritten
            fail : Raises a value error

    Returns
    -------
    None
    '''
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, database))
    data.to_sql(table_name, engine)

    return None


def save_to_s3(data, bucket_name, file_name, key, secret):
    ''' 
    Saves dataframe to postgres as table

    Parameters
    ----------
    data : Pandas dataframe
        The Pandas data frame which hsa to be saved
    bucket_name : string
            The name of the bucket you want the csv to be in
    file_name : string
            The name of the CSV file to be called in s3
    key : string
            The AWS_ACCESS_KEY_ID
    secret: string
            The AWS_SECRET_ACCESS_KEY

    Returns
    -------
    None
    '''
    bytes_to_write = data.to_csv(None).encode()
    fs = s3fs.S3FileSystem(key=key, secret=secret)

    # add .csv extenstion for file if i does not exist
    if(".csv" not in file_name):
            file_name = file_name+".csv"

    s3_uri = "s3a://{}/{}".format(bucket_name, file_name)
    with fs.open(s3_uri, 'wb') as f:
        f.write(bytes_to_write)

    return None


def reduce_mem_usage(df2):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.        
    """
    df = df2.copy()
    start_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
    
    for col in df.columns:
        col_type = df[col].dtype
        
        if (is_numeric_dtype(df[col])):
        # if col_type != object and col_type !=category:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
        	pass
        # elif(is_datetime64_dtype(data[col])):
        # 	pass
        # else:
        #     df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    if(start_mem - end_mem) < 0 :
        print("Memory optimization failed, cannot reduce memory! Returning original dataframe")
        return df2
    else:
        print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
        print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
        return df


def dataframe_dtypes(data):
    return pd.DataFrame(data.dtypes, columns=["datatype"]).sort_index()

def save_file(data, NEW_FILE_NAME, NEW_FILE_FORMAT):
	# save file
	if(NEW_FILE_FORMAT  != ""):
	    if(NEW_FILE_FORMAT is "csv"):
	        save_to_csv(data, NEW_FILE_NAME)
	    elif(NEW_FILE_FORMAT is "numpy"):
	        save_to_pickle(data, NEW_FILE_NAME)
	    elif(NEW_FILE_FORMAT is "parquet"):
	        save_to_parquet(data, NEW_FILE_NAME)
	return None

def load_file(FILE_NAME, FILE_FORMAT):
	# load file
	if(FILE_NAME  != ""):
	    if(FILE_FORMAT is "csv"):
	        data = pd.read_csv(FILE_NAME, header=0)
	    elif(FILE_FORMAT is "numpy"):
	        data = pd.read_pickle(FILE_NAME)
	    elif(FILE_FORMAT is "parquet"):
	        data = pd.read_parquet(FILE_NAME)
	return data