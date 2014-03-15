"""
Gnumeric interface for the IAC protocol

Requirements:  
    - Install gnumeric
    - Enable the "Python plugin loader" by going to Tools > Plug-ins... -> Plugin List 
      and selecting it from the checkbox list.
"""
from gi.repository import GOffice
from gi.repository import Gnm
import warnings


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    Gnm.init()


class CellRangeCalculator(object):
    def column_index(self, column):
        if len(column) == 1:
            column_list = list(column[0])
        else:
            column_list = column
        base26 = []
        for i in range(len(column_list)):
            if column_list[i].isdigit():
                return False
            else:
                base26.append(ord(column_list[i].lower()) - ord('a') + 1)
        return base26

    def base26_to_base10(self, digits):
        digit_count = len(digits) - 1
        base10_value = 0
        for digit in digits:
            base10_value += digit * 26**digit_count
            digit_count -= 1
        return base10_value

    def cell_range_to_index(self, cell_range):
        if type(cell_range) is list:
            cell_range = cell_range[0]
        column = []
        row = []
        column_start = True
        for i in cell_range:
            if not i.isdigit() and column_start:
                column.append(i)
            elif i.isdigit():
                column_start = False
                row.append(i)
            if not i.isdigit() and not column_start:
                return False
        row = int("".join(row))
        column = self.base26_to_base10(self.column_index(column)) 
        return (column, row)


class Interface(object):
    variables = {}

    @staticmethod
    def new_document(number_of_sheets):
        """new_document([number of sheets])"""
        return Gnm.Workbook.new_with_sheets(number_of_sheets)

    @staticmethod
    def get_sheet(workbook, sheet_index):
        """[workbook].get_sheet([sheet index])"""
        return workbook.sheet_by_index(sheet_index)

    @staticmethod
    def fetch_cell(sheet, cell_range):
        """[sheet].fetch_cell(['A1'])"""
        cell_range_calculator = CellRangeCalculator()
        column, row = cell_range_calculator.cell_range_to_index(cell_range)
        return sheet.cell_fetch(column - 1, row - 1)

    @staticmethod
    def set_text(cell, string):
        """[cell].set_text(['string'])"""
        if (string.startswith('"') and string.endswith('"')) or \
                (string.startswith("'") and string.endswith("'")):
            string = string[1:-1]
        try:
            cell.set_text(string)
            return True
        except:
            return False

    @staticmethod
    def get_text(cell):
        """[cell].get_text()"""
        return cell.value.get_as_string()

    @staticmethod
    def save_as(workbook, path):
        """[workbook].save_as(['path'])"""
        uri = GOffice.shell_arg_to_uri(path)
        workbook_view = Gnm.WorkbookView.new(workbook)
        file_saver = GOffice.FileSaver.for_file_name(uri)
        command_context = Gnm.CmdContextStderr.new()
        Gnm.wb_view_save_as(workbook_view, file_saver, uri, command_context)
        return True
