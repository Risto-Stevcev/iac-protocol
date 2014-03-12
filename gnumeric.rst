.. _gnumeric:

********
Gnumeric
********

.. default-domain:: py

.. index::
   single: gnumeric
   single: application

This page provides a guide on how to setup and use Gnumeric for the IAC protocol.

.. warning::
    Gnumeric needs to have the Python plugin loader enabled for it to function properly. Please see the instructions 
    for more details.

Instructions
============

#. Install Gnumeric. Make sure that Gnumeric is installed and works with Python by typing ``import Gnm`` in the Python 
   interpreter. If it doesn't raise an ``ImportError`` then it works.

#. Enable the **Python plugin loader** in Gnumeric by going to **Tools > Plug-ins... -> Plugin List** and selecting it 
   from the checkbox list.

#. Make sure that Gnumeric is enabled in the ``interfaces.py`` file. You can access Gnumeric using the ``gnumeric`` scope
   name.

#. Play with the :mod:`interpreter` to learn how the functionality works. Then use the :mod:`server` to create 
   automation scripts! See the :mod:`server` module for a sample automation shell script.

If you wish to contribute to improving Gnumeric's functionality, view the Gnumeric plugin documentation for Python or 
discover it's properties using Python's object introspection on Gnumeric's module ``Gnm``. Then, clone the project 
repository from the project's GitHub_ page, add your modified application, and submit a pull request to be reviewed. If 
your additions to the application follow the protocol convention and it doesn't contain any obvious errors, it will be
accepted!



The first step is to create your application's python file in the *app/* directory with a descriptive name. If your 
application contains several sub-applications, like an office suite, then create a sub-folder in the *app/* directory. 
Then create an ``__init__.py`` file in the sub-folder so that the IAC protocol can recognize it as a package and add 
all of your sub-applications.

Follow through the example implementation in the next section for implementation details.



Example
=======

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

.. function:: new_document(number_of_sheets)
  Example usage:
  
  *gnumeric -> doc = new_document(1)*

  :param int number_of_sheets: The number of sheets to create in the document.
  :return: A *workbook* object.

.. function:: document.get_sheet(sheet_index)
  Example usage:

  *gnumeric -> sheet = doc.get_sheet(0)*

  :param int sheet_index: The index of the sheet to access.
  :return: A *sheet* object.

.. function:: sheet.fetch_cell(cell_range)
  Example usage:

  *gnumeric -> cell = sheet.fetch_cell('A1')*

  :param str cell_range: The cell to be fetched.
  :return: A *cell* object.

.. function:: cell.set_text(string)
  Example usage:

  *gnumeric -> cell.set_text("Hello, World!")*

  :param str string: A string to set the cell contents to.
  :return: *True* on success, *False* otherwise.

.. function:: cell.get_text()
  Example usage:

  *gnumeric -> cell.get_text()*
  
  If the cell text is set to "*Hello, World*" this would be returned. 

  :return: The cell's text.

.. function:: workbook.save_as(path)
   Example usage:

   *gnumeric -> doc.save_as('/home/gyeh/hello.gnumeric')*

   :param str path: The path to save the workbook to (must end with *.gnumeric*)
   :return: *True* on success, *False* otherwise.


.. _GitHub: https://github.com/Risto-Stevcev/iac-protocol 
