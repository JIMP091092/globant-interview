import argparse
from historical import historical_load

if __name__ == "__main__":

    """"
    Set up the arguments to do the historical loading
    Arguments:
        path : provide the path where csv is located
        source: provide name of source to do the historical loading
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest='path' ,type=str, help='Source path', required=True)
    parser.add_argument('--source', dest='source' ,type=str, help='Choose source to load', choices=['departments','employees','jobs'], required=True)
    args = parser.parse_args()
    
    historical_load(args.source, args.path)