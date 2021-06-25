# -*- coding: utf-8 -*-
"""
usage: levenshtein [-h] -i INPUT_DATA -n NAME -d DISTANCE

Calculate levenshtein distance

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DATA, --input INPUT_DATA
                        Path to file containing data [.csv]
  -n SEARCH_NAME, --name NAME
                        name
  -d DISTANCE, --distance DISTANCE
                        distance
"""
import logging
import argparse
import pandas as pd

import Levenshtein as lev

from typing import List, Any

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main(args: List[str]):
    """
    Main rutine.

    :param args:
    """
    log.info("Getting names to specified levenshtein distance...")

    selected_names = []

    # Read data, name and distance
    hdata_df = pd.read_csv(args.input_data, sep=',')

    for hund_name in hdata_df['HUNDENAME']:

        # Calculate distance and check with required
        if lev.distance(hund_name.lower(), args.name.lower()) == args.distance:
            selected_names.append(hund_name)

    log.info(f"Names to Levenshtein dist. {args.distance} from {args.name}:")
    log.info(selected_names)


def parse_args() -> List[Any]:
    """
    Function that creates a new argument parser and parses arguments.
    """
    # Prepare parser with arguments
    parser = argparse.ArgumentParser(prog='levenshtein',
                                     description='Calculate levenshtein' +
                                                 ' distance')

    parser.add_argument('-i', '--input',
                        dest='input_data',
                        type=str,
                        help='Path to file containing ' +
                             'data [.csv]',
                        required=True)

    parser.add_argument('-n', '--name',
                        dest='name',
                        type=str,
                        help='name',
                        required=True)

    parser.add_argument('-d', '--distance',
                        dest='distance',
                        type=int,
                        help='distance',
                        required=True)

    # Parse arguments and return
    return parser.parse_args()


if __name__ == '__main__':

    # Get input args and run
    main(parse_args())
