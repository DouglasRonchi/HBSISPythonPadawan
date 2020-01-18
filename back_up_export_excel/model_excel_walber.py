import xlsxwriter as write
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from uploads import UPLOADS_PATH


def _generate_data_from_category(data: list) -> list:  # mudar nome do metodo
    return [item.serialize() for item in data]


def _create_workbook() -> Workbook:
    return write.Workbook(UPLOADS_PATH + '/category.xlsx')


def _build_header(data: list) -> list:
    data_list = _generate_data_from_category(data)
    header = []
    for dict_ in data_list:
        for key in dict_.keys():
            if key not in header:
                header.append(key)
    return header


def _build_file_from_data(data: list) -> Worksheet:
    workbook = _create_workbook()
    sheet = _build_sheet(data, workbook)
    workbook.close()
    return sheet


def _build_sheet(data: list, workbook: Workbook) -> Worksheet:
    sheet = workbook.add_worksheet()
    header = _build_header(data)
    [sheet.write(0, col, header[col]) for col in range(len(header))]
    row_increment = 1
    for list_ in _build_data_list(data):
        for position in range(len(list_)):
            if list_[position] is not None:
                sheet.write(row_increment, position, list_[position])
        row_increment += 1
    return sheet


def _build_data_list(data: list) -> list:
    return list(map(lambda it: it.values(), data))


class ExportExcel:
    def __init__(self, data: list):
        self._file = _build_file_from_data(data.copy())

    def get_file(self) -> Worksheet:
        return self._file
