from uno import getComponentContext
from com.sun.star.connection import ConnectionSetupException
from com.sun.star.awt.FontWeight import BOLD
import sys

# For saving the file
from com.sun.star.beans import PropertyValue
from uno import systemPathToFileUrl


class Message(object):
    connection_setup_exception = "Error: Please start the uno bridge first."


# Connect to libreoffice using UNO
UNO_PORT = 18100
try:
    localContext = getComponentContext()
    resolver = localContext.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", localContext)
    context = resolver.resolve(
            "uno:socket,host=localhost,port=%d;urp;StarOffice.ComponentContext" % UNO_PORT)
except ConnectionSetupException:
    print("%s\n" % Message.connection_setup_exception)
    sys.exit(1)

# Get the desktop service
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)


class Interface(object):
    variables = {}

    @staticmethod
    def current_document():
        """current_document()"""
        return desktop.getCurrentComponent()
    
    @staticmethod
    def current_sheet(document):
        """[document].current_sheet()"""
        return document.getCurrentController().getActiveSheet()
    
    @staticmethod
    def save_as(document, path):
        """[document].save_as(['path'])"""
        url = systemPathToFileUrl(path)

        # Set file to overwrite
        property_value = PropertyValue()
        property_value.Name = 'Overwrite'
        property_value.Value = 'overwrite'
        properties = (property_value,)

        # Save to file
        document.storeAsURL(url, properties)
        return True

    @staticmethod
    def fetch_cell(sheet, cell_range):
        """[sheet].fetch_cell(['A1'])"""
        return sheet.getCellRangeByName(cell_range)
    
    @staticmethod
    def set_text(cell, string):
        """[cell].set_text(['string'])"""
        if (string.startswith('"') and string.endswith('"')) or \
                (string.startswith("'") and string.endswith("'")):
            string = string[1:-1]

        cell.setString(string)
        return True

    @staticmethod
    def get_text(cell):
        """[cell].get_text()"""
        return cell.getString()

    @staticmethod
    def weight(cell, bold):
        """[cell].weight(['bold'])"""
        if bold.strip("'").strip('"') == "bold":
            cell.CharWeight = BOLD
            return True
        else:
            return False
