import pandas as pd
from config.get_schema import GetSchemas
from kafka_utils.producer import producer_msg



def historical_load(source, path):
    """
    Get schemas depends on source
    Returns: 
        Source function
    """
    func_schema= getattr(GetSchemas, source)
    
    """
    Read csv from local path and assign the correct datatype per column
        Arguments:
            path : local path
        Returns:
            Dataframe
    """
    df= func_schema(GetSchemas, path)
 
    df.apply(lambda x: producer_msg(x, source), axis=1)
    