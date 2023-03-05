import argparse
from historical_load.historical import historical_load
import api.rest_api as api

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--type', dest='type' ,type=str, help='Choose type of program', choices=['api','historical'], required=True)
    parser.add_argument('--path', dest='path' ,type=str, help='Source path')
    parser.add_argument('--source', dest='source' ,type=str, help='Choose source to load', choices=['departments','employees','jobs'])
    args = parser.parse_args()

    if args.type == 'historical':
        """"
        Set up the arguments to do the historical loading
        Arguments:
            path : provide the path where csv is located
            source: provide name of source to do the historical loading
        """
        historical_load(args.source, args.path)
    else:
        api.app.run(debug=True, port=8080)