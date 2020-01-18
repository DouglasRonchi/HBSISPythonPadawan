import xlsxwriter as write

from uploads import UPLOADS_PATH


class ExportExcel:
    def __init__(self, data: list):
        self._data = data
        self._header = []
        self._data_list = []
        self._out_workbook = object
        self._out_sheet = object
        self._generate_data_from_category()
        self._create_new_file()
        self._build_header()
        self._write_file_head()
        self._write_file_data()
        self._out_workbook.close()

    def _generate_data_from_category(self) -> None:
        self._data_list = [items.serialize() for items in self._data]

    def _create_new_file(self) -> None:
        self._out_workbook = write.Workbook(UPLOADS_PATH + '/category.xlsx')
        self._out_sheet = self._out_workbook.add_worksheet()

    def _build_header(self) -> None:
        for dict_ in self._data_list:
            for key in dict_.keys():
                if key not in self._header:
                    self._header.append(key)

    def _write_file_head(self) -> None:
        for col in range(len(self._header)):
            self._out_sheet.write(0, col, self._header[col])

    def _write_file_data(self) -> None:
        data_list = []
        for item in self._data_list:
            data_list.append(list(item.values()))

        row = 1
        for data in data_list:
            for position in range(len(data)):
                if data[position] is not None:
                    self._out_sheet.write(row, position, data[position])
            row += 1


