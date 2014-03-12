.. _plugin:

**********************************
IAC protocol plugin implementation
**********************************

.. default-domain:: py

.. index::
   single: plugin
   single: implementation

This page provides a guide on how to contribute and develop an application plugin for the IAC protocol.
The plugin implementation is fairly straightforward.

.. warning::
   The plugin interface currently uses static calls to the various functions. This works fine for most
   use cases, but ideally it should support multi-threading and multiple client access without creating
   race conditions. As a result, this implementation will soon be deprecated and will be replaced by
   object instances and regular non-static functions. Don't let this deter you from contributing right now, 
   because the implementation will not change much.


Steps
-----

Suppose you have a favorite application and there isn't an implementation of it for the IAC protocol. If 
the application supports plugin development, it's highly likely that you can turn this into an application 
that the IAC protocol can use. Currently there is no guide for plugin interfaces that aren't written in 
Python, but if you find an application like this, don't hesitate to email me for help on how to integrate it.

Integrating your application is fairly straightforward. Here are the steps:

#. Experiment with your application's plugin development interface directly first to get a feel for it's
   requirements and how it works.

#. Read the :ref:`protocol` section for details on how to structure the semantics of your commands.

#. Follow this page's example for implementation details.

#. Clone the repository from the project's GitHub_ page, add your application, and submit a pull request to be reviewed.

#. If your application has no obvious semantic or implementation errors, then it will be accepted!


The first step is to create your application's python file in the *app/* directory with a descriptive name. If your 
application contains several sub-applications, like an office suite, then create a sub-folder in the *app/* directory. 
Then create an ``__init__.py`` file in the sub-folder so that the IAC protocol can recognize it as a package and add 
all of your sub-applications.

Follow through the example implementation in the next section for implementation details.



Example
-------

The following example gives an implementation overview of the Gnumeric application from the IAC protocol version 0.1 as 
an example of how to structure your application. Notice first that ``gnumeric.py`` is in the *app/* folder. 

Finally, Gnumeric is registered in the ``interfaces.py`` file so that the IAC protocol can recognize it. See the 
:mod:`interfaces` module for more information. It is registered as ``gnumeric``, which is it's scope name.

At the beginning of the Gnumeric's implementation in ``gnumeric.py``, it contains some necessary imports, some comments, 
and other initialization data::

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

Notice that, besides the imports, the application begins by describing some important information on
how to get the application to work. Gnumeric needs to have the *Python plugin loader* enabled from the 
Plug-ins menu or it won't work.

It also contains some initialization functionality. In this case, it suppresses Gtk's warnings, which 
can be pretty visually annoying and not particularly useful for this plugin. It also has the most 
important initialization function, ``Gnm.init()``, which initializaes Gnumeric so that it can be used.

You can create multiple classes and even files, but in order for your plugin to function properly, all 
methods that you want to be called by the interface should be contained within a class called ``Interface``.
The ``Interface`` class contains a ``variables`` dictionary so that it can access declared variables. This
dictionary is required if you want to be able to save and call variables. Here are some of Gnumeric's
definitions and use cases:

.. class:: Interface(object)

   This contains the interface for the application and it's methods. This class is a partial example
   of Gnumeric's implementation of the interface.

   :var variables: *(required)* A dictionary of variables that the protocol uses to access objects and their methods.

   .. staticmethod:: new_document(number_of_sheets)
      Example usage:
      
      *gnumeric -> doc = new_document(1)*

      :param int number_of_sheets: The number of sheets to create in the document.
      :return: A *workbook* object.

   .. staticmethod:: get_sheet(workbook, sheet_index)
      Example usage:

      *gnumeric -> sheet = doc.get_sheet(0)*

      :param workbook workbook: An instance of the *workbook* object.
      :param int sheet_index: The index of the sheet to access.
      :return: A *sheet* object.

   .. staticmethod:: fetch_cell(sheet, cell_range)
      Example usage:

      *gnumeric -> cell = sheet.fetch_cell('A1')*

      :param sheet sheet: An instance of the *sheet* object.
      :param str cell_range: The cell to be fetched.
      :return: A *cell* object.

   .. staticmethod:: set_text(cell, string)
      Example usage:

      *gnumeric -> cell.set_text("Hello, World!")*

      :param cell cell: An instance of the *cell* object.
      :param str string: A string to set the cell contents to.
      :return: *True* on success, *False* otherwise.

   .. staticmethod:: get_text(cell)
      Example usage:

      *gnumeric -> cell.get_text()*
      
      If the cell text is set to "*Hello, World*" this would be returned. 

      :param cell cell: An instance of the *cell* object.
      :return: The cell text.


And here is the example code of the partial implementation of Gnumeric's interface class::

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

            cell.set_text(string)
            return True

        @staticmethod
        def get_text(cell):
            """[cell].get_text()"""
            return cell.value.get_as_string()

.. _GitHub: https://github.com/Risto-Stevcev/iac-protocol 
