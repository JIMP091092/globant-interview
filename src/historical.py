import pandas as pd
from config.get_schema import GetSchemas
from kafka_utils.producer import producer_msg



def historical_load(source, path):
    func_schema= getattr(GetSchemas, source)
    
    # Read csv to do historical loading
    df= func_schema(GetSchemas, path)
 
    df.apply(lambda x: producer_msg(x, source), axis=1)
    