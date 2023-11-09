"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neo_objects = []
    with open(neo_csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for line in reader:
            try:
                data = [line[3], line[7], line[4], float(line[15])]
            except ValueError:
                data = [line[3], line[7], line[4], float('nan')]
            data[1] = True if data[1] == 'Y' else False
            neo_objects.append(data)
    return [NearEarthObject(*data) for data in neo_objects]

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path, 'r') as json_file:
        cad_data = json.load(json_file)

    cad_data = cad_data['data']
    cad_data = [[entry[0], entry[3], float(entry[4]), float(entry[7])] for entry in cad_data]
    return [CloseApproach(*entry) for entry in cad_data]