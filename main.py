"""
Five Battle summarization tool

From Apple Numbers select Export such sheet to Pythonista3
+--------+-------------+------+---------------+
|  name  | throw_rings | dart | frog_spitting |
+--------+-------------+------+---------------+
| Daniel |           3 |   25 |            75 |
| Nils   |           5 |   15 |            68 |
+--------+-------------+------+---------------+

Outputs a summarization counting scores correctly

==============throw_rings===============
Nils: 2 [Competition score: 5]
Daniel: 1 [Competition score: 3]


==================dart==================
Daniel: 2 [Competition score: 25]
Nils: 1 [Competition score: 15]


=============frog_spitting==============
Daniel: 2 [Competition score: 75]
Nils: 1 [Competition score: 68]


=============Summary score==============
1: Daniel [Score: 5]
2: Nils [Score: 4]

"""
from zipfile import ZipFile
import csv
from io import StringIO
from collections import namedtuple, defaultdict, Counter
import appex
p = appex.get_file_path()

name_point = namedtuple('name_point', ['name', 'point'])


def get_data_io(fn=None):
    """
    :param fn: The filename or path to the data file. This parameter is optional and defaults to None.
    :return: Returns a StringIO object that contains the contents of the data file.

    The `get_data_io` method reads the data from a specified file and returns a StringIO object. If the filename ends with ".zip", it will unzip the file and read the contents from the first
    * file in the zip archive. If the filename ends with ".csv", it will read the contents directly from the file.

    Example usage:

    ```python
    data_io = get_data_io('data.zip')
    ```

    ```python
    data_io = get_data_io('data.csv')
    ```
    """
    print(f'Reading data from {fn}')
    d = None
    if fn.endswith('zip'):
        with ZipFile(fn) as zp:
            fl = zp.filelist
            d = zp.open(fl[0].filename).read().decode()
    elif fn.endswith('csv'):
        d = open(fn, 'r').read()
    return StringIO(d)


def get_results(csv_data):
    """
    :param csv_data: A file object or a string containing the CSV data.
    :return: A defaultdict of lists containing the results for each "grenar" (Swedish for categories).

    The method returns the 'result_grenar' defaultdict containing the results for each category.
    """

    result_grenar = defaultdict(list)
    reader = csv.DictReader(csv_data, delimiter=';')
    ...
    name_field, *grenar = reader.fieldnames
    for row in reader:
        namn = row[name_field]
        for gren in grenar:
            try:
                point = int(row[gren])
            except ValueError:
                point = 0
            result_grenar[gren].append(name_point(namn, point))
    return result_grenar


def get_point_converter(list_points):
    """
    :param list_points: A list of points that need to be converted
    :return: A dictionary containing the conversion table for the points

    Example usage:
        list_points = [0, 1, 3, 2, 2, 1, 4]
        conversion_table = get_point_converter(list_points)
        print(conversion_table)
        # Output: {1: 1, 2: 2, 3: 3, 4: 4}
    """
    convert_table_gren_to_true = {}
    uniq_points = list(set(list_points))
    try:
        uniq_points.remove(0)
    except ValueError:
        ...
    for true_point, p in enumerate(sorted(uniq_points), 1):
        convert_table_gren_to_true[p] = true_point
    convert_table_gren_to_true[0] = 0
    return convert_table_gren_to_true


def print_results(result_grenar):
    """
    :param result_grenar: A dictionary containing the results of each grenade.
    :return: None
    """
    total_point = Counter()
    for gren, name_points in result_grenar.items():
        print('\n')
        print(gren.center(40, '='))
        gren_points = [_.point for _ in name_points]
        point_converter = get_point_converter(gren_points)
        for name, point in sorted(name_points, key=lambda p: p.point, reverse=True):
            rank_point = point_converter[point]
            print(f'{name}: {rank_point} [Competition score: {point}]')
            total_point[name] += rank_point
    print('\n')
    print('Summary score'.center(40, '='))
    for rank, (name, point) in enumerate(sorted(total_point.items(), key=lambda x: x[1], reverse=True), 1):
        print(f'{rank}: {name} [Score: {point}]')


def main():
    data_io = get_data_io(p)
    results = get_results(data_io)
    print_results(results)


if __name__ == '__main__':
    main()


