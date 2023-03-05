import pandas as pd

class GetSchemas:
    def employees(self, path:str) -> pd.DataFrame:

        df = pd.read_csv(path, header=None, names=['id', 'name', 'datetime', 'department_id', 'job_id'])
        df = df.fillna(0)

        schema = {
            'id': int, 
            'name': str, 
            'datetime': str, 
            'department_id': int, 
            'job_id': int
        }

        df = df.astype(schema)

        return df
    
    def departments(self, path:str) -> pd.DataFrame:
        df = pd.read_csv(path, header=None, names=['id', 'department'])
        df = df.fillna(0)

        schema = {
            'id': int, 
            'department': str
        }

        df = df.astype(schema)

        return df
    
    def jobs(self, path:str) -> pd.DataFrame:
        df = pd.read_csv(path, header=None, names=['id', 'job'])
        df = df.fillna(0)

        schema = {
            'id': int, 
            'job': str
        }

        df = df.astype(schema)
        
        return df
    
    def json_employees(self, row) -> dict:

        data= {
        'id': row['id'], 
        'name': row['name'], 
        'datetime': row['datetime'], 
        'department_id': row['department_id'], 
        'job_id': row['job_id']
        }

        return data
    
    def json_departments(self, row) -> dict:

        data= {
            'id': row['id'], 
            'department': row['department']
        }

        return data
    
    def json_jobs(self, row) -> dict:

        data= {
            'id': row['id'], 
            'job': row['job']
        }

        return data
    
    def json_errors(self, row) -> dict:

        data= {
            'transaction': str(row)
        }

        return data