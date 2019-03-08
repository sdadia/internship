# imports
import pandas as pd


def missing_stats(data):
    ''' 
    Finds number of missing values for each column of pandas data frame,
    in terms of raw counts and as percentage.

    Parameters
    ----------
    data : Pandas dataframe
        The data frame

    Returns
    -------
    missing_value_df : Pandas dataframe
        Data frame with missing values sorted in
        descending order.
    '''
    missing = data.isnull().sum()
    percent_missing = missing * 100 / len(data)
    missing_value_df = pd.DataFrame({'missing': missing,
                                     'percent_missing': percent_missing})
    missing_value_df.sort_values('percent_missing', 
                                 inplace=True, 
                                 ascending=False)
    return missing_value_df


def drop_missing_rows(data):
    ''' 
    Function which removes the rows with one or more missing values.
    It returns a new data frame. Does not perform inplace operation

    Parameters
    ----------
    data : Pandas dataframe
        The data frame of pandas

    Returns
    -------
    data_no_missing : Pandas dataframe
        Pandas dataframe with rows having no missing values at all
    '''
    # drop rows with missing values
    data_no_missing = data.dropna(inplace=False)
    return data_no_missing


def get_missing_rows(data):
    '''
    Function which gets the rows with one or more missing values.
    It returns a new data frame

    Parameters
    ----------
    data : Pandas dataframe
        The data frame of pandas

    Returns
    -------
    null_data : Pandas dataframe
        Pandas dataframe with rows having one or more missing values

    '''
    null_data = data[data.isnull().any(axis=1)]
    return null_data


def imupute_missing(data, imputation_mode, fill_value=0):
        ''' 
        Impute the missing values in the rows with their column mean value.

        Parameters
        ----------
        data : Pandas dataframe
            The data frame of pandas where imputation is performed
        imputation_mode : String
            The type of imputation 'mean', 'fill', 'ffill', 'bfill
        fill_value : Float
            The numerica vlaue to be replaced when using fill

        Returns
        -------
        imputed_data : Pandas dataframe
            Pandas dataframe with mean
        '''
        if(imputation_mode == 'fill'):
            return data.fillna(fill_value)
        elif(imputation_mode == 'ffill'):
            return data.fillna(method='ffill')
        elif(imputation_mode == 'bfill'):
            return data.fillna(method='bfill')