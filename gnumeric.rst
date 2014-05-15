.. _gnumeric:

********
Gnumeric
********

.. default-domain:: py

.. index::
   single: gnumeric
   single: application

.. module:: gnumeric
   :synopsis: The Gnumeric application implementataion and documentation
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>


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
discover it's properties using Python's object introspection on Gnumeric's module ``gi.repository``. 

Then, clone the project repository from the project's GitHub_ page, add your modified application, and submit a pull request to be reviewed. If 
your additions to the application follow the protocol convention and it doesn't contain any obvious errors, it will be
accepted! See :ref:`plugin` for more details.



Example
=======

Here is an example ``Hello, World!`` shell script.  
Run the server (``iacs``) and try this script::

    #!/usr/bin/env bash
    # Netcat: -u is for UDP, -c closes the connection on EOF

    PORT=14733
    if [[ $# -eq 3 ]]; then
        echo -e "gnumeric -> doc = new_document(1)\n" | nc -uc localhost $PORT 
        echo -e "gnumeric -> sheet = doc.get_sheet(0)\n" | nc -uc localhost $PORT
        echo -e "gnumeric -> cell = sheet.fetch_cell('$1')\n" | nc -uc localhost $PORT
        echo -e "gnumeric -> cell.set_text('$2')\n" | nc -uc localhost $PORT
        echo -e "gnumeric -> doc.save_as('$3')\n" | nc -uc localhost $PORT
    else
        echo "Usage: $0 [cell] [string] [path]"
    fi


Or try the interpreter by directing the following as stdin::

    gnumeric -> doc = new_document(1)
    gnumeric -> sheet = doc.get_sheet(0)
    gnumeric -> cell = sheet.fetch_cell('A1')
    gnumeric -> cell.set_text('Hello, World!')
    gnumeric -> doc.save_as('./hello.gnumeric')

And then run it as something like ``iaci < hello-gnumeric.txt`` (assuming it's saved as that name).

Commands
========

.. function:: new_document(number_of_sheets)
   Example usage:
  
   *gnumeric -> doc = new_document(1)*

   :param int number_of_sheets: The number of sheets to create in the document.
   :return: A *workbook* object.
   :noindex:

.. function:: document.get_sheet(sheet_index)
   Example usage:

   *gnumeric -> sheet = doc.get_sheet(0)*

   :param int sheet_index: The index of the sheet to access.
   :return: A *sheet* object.
   :noindex:

.. function:: sheet.fetch_cell(cell_range)
   Example usage:

   *gnumeric -> cell = sheet.fetch_cell('A1')*

   :param str cell_range: The cell to be fetched.
   :return: A *cell* object.
   :noindex:

.. function:: cell.set_text(string)
   Example usage:

   *gnumeric -> cell.set_text("Hello, World!")*

   :param str string: A string to set the cell contents to.
   :return: *True* on success, *False* otherwise.
   :noindex:

.. function:: cell.get_text()
   Example usage:

   *gnumeric -> cell.get_text()*
  
   :return: The cell's text.
   :noindex:

.. function:: workbook.save_as(path)
   Example usage:

   *gnumeric -> doc.save_as('/home/gyeh/hello.gnumeric')*

   :param str path: The path to save the workbook to (must end with *.gnumeric*)
   :return: *True* on success, *False* otherwise.
   :noindex:


.. _GitHub: https://github.com/Risto-Stevcev/iac-protocol 
