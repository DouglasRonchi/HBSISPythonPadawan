import xlsxwriter as write

from uploads import UPLOADS_PATH


def _generate_data_from_category(data: list) -> list: #mudar nome do metodo
    data_list = [items.serialize() for items in data]
    return data_list


def _create_workbook():
    global workbook
    workbook = write.Workbook(UPLOADS_PATH + '/category.xlsx')


def _create_sheet() -> object:
    return workbook.add_worksheet()


def _build_header(data) -> list:
    data_list = _generate_data_from_category(data)
    header = []
    for dict_ in data_list:
        for key in dict_.keys():
            if key not in header:
                header.append(key)
    return header


class ExportExcel:
    def __init__(self, data: list):
        self._export(data)

    def _build_data_from_category(self, data) -> None:
        _create_workbook()
        sheet = _create_sheet()
        header = _build_header(data)
        [sheet.write(0, col, header[col]) for col in range(len(header))]

        data_list = []
        [data_list.append(list(dict_.values())) for dict_ in data]

        row_increment = 1
        for list_ in data_list:
            for position in range(len(list_)):
                if list_[position] is not None:
                    sheet.write(row_increment, position, list_[position])
            row_increment += 1

    def _export(self, data):
        self._build_data_from_category(data)
        workbook.close()
