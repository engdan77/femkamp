from zipfile import ZipFile
import csv
from io import StringIO
from collections import namedtuple, defaultdict, Counter

name_point = namedtuple('name_point', ['name', 'point'])

# import appex
# p = appex.get_file_path()

def get_data_io(fn='./2024_femkamp.zip'):
    d = None
    with ZipFile(fn) as zp:
        fl = zp.filelist
        d = zp.open(fl[0].filename).read().decode()
    return StringIO(d)


def get_results(csv_data):
    """Return {'gren': [name_point, ...]}"""

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
    total_point = Counter()
    for gren, name_points in result_grenar.items():
        print('\n')
        print(gren.center(40, '='))
        gren_points = [_.point for _ in name_points]
        point_converter = get_point_converter(gren_points)
        for name, point in sorted(name_points, key=lambda p: p.point, reverse=True):
            rank_point = point_converter[point]
            print(f'{name}: {rank_point} [Gren poäng: {point}]')
            total_point[name] += rank_point

    print('\n')
    print('Summering poäng'.center(40, '='))
    for rank, (name, point) in enumerate(total_point.items(), 1):
        print(f'{rank}: {name} [Poäng: {point}]')


def main():
    # data_io = get_data_io(p)
    data_io = get_data_io()
    results = get_results(data_io)
    print_results(results)


if __name__ == '__main__':
    main()


