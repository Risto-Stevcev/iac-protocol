.. _localc:

******************
LibreOffice Calc
******************

.. default-domain:: py

.. index::
   single: libreoffice
   single: calc
   single: application

.. module:: localc
   :synopsis: The LibreOffice Calc application implementataion and documentation
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>


This page provides a guide on how to setup and use LibreOffice Calc for the IAC protocol.

.. warning::
    LibreOffice needs to have the UNO bridge running for it to function properly. Please see the instructions 
    for more details.



Instructions
============

#. Install LibreOffice.
   
#. Make sure that UNO works. Run ``import uno`` from the Python interpreter. It requires Python 3+. If it doesn't raise an ``ImportError`` then it works.

#. Run the UNO bridge. The UNO bridge is a server that provides a programming interface to access the internals of a LibreOffice document. 
 
   #. You can run multiple LibreOffice applications by passing them in as switches. If you want to use the ``current_document()`` command, then it will 
      only work on the first switch passed, in this case Calc. Here is the command to run UNO for Calc and Calc:
      ``libreoffice "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --calc --calc``
   
   #. If you want to run the bridge without opening any application, pass in the switch ``--headless``. You cannot use the ``current_document()`` command 
      in this mode because no application is running. Here is the command to write UNO for Calc and Calc:
      ``libreoffice --headless "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --calc --calc`` 

#. Make sure that the LibreOffice applications you want to use are enabled in the ``interfaces.py`` file. You can access LibreOffice calc using the ``localc`` 
   scope name.

#. Play with the :mod:`interpreter` to learn how the functionality works. Then use the :mod:`server` to create automation scripts! 

If you wish to contribute to LibreOffice Calc, try playing around with Python's library imports for LibreOffice Calc. But the best way is probably to view the 
UNO API documentation online, available from both LibreOffice and OpenOffice, which are essentially identical APIs. If the functionality is written in Java or another 
language, please try to change the logic to Python. The same namespace and class names are typically used, so this isn't usually difficult to do.

Then, clone the project repository from the project's GitHub_ page, add your modified application, and submit a pull request to be reviewed. If 
your additions to the application follow the protocol convention and it doesn't contain any obvious errors, it will be
accepted! See :ref:`plugin` for more details.



Example
=======

Here is a sample demonstrating LibreOffice Calc's functionality. First, run the UNO bridge::

   libreoffice "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --calc

Then run the following ``Hello, World!`` shell script::

    #!/usr/bin/env bash
    # Netcat: -u is for UDP, -c closes the connection on EOF

    PORT=14733
    if [[ $# -eq 3 ]]; then
        echo -e "localc -> doc = new_document()\n" | nc -uc localhost $PORT 
        echo -e "localc -> sheet = doc.current_sheet()\n" | nc -uc localhost $PORT
        echo -e "localc -> cell = sheet.fetch_cell($1)\n" | nc -uc localhost $PORT
        echo -e "localc -> cell.set_text('$2')\n" | nc -uc localhost $PORT
        echo -e "localc -> doc.save_as('$3')\n" | nc -uc localhost $PORT
    else
        echo "Usage: $0 [cell] [string] [path]"
    fi



Commands
========

.. function:: current_document()
   Selects the currently active document. Doesn't work if UNO is in headless mode.
   Example usage:
  
   *localc -> doc = current_document()*

   :return: A *document* object.
   :noindex:

.. function:: document.current_sheet()
   Selects the currently active sheet in the document.
   Example usage:
  
   *localc -> sheet = document.current_sheet()*

   :return: A *spreadsheet* object.
   :noindex:

.. function:: load_document(path)
   Example usage:

   *localc -> doc = load_document('/home/gyeh/hello.ods')*

   :param str path: The path where the document is (must end with *.ods*)
   :return: A *document* object.
   :noindex:

.. function:: new_document()
   Example usage:

   *localc -> doc = new_document()*

   :return: A *document* object.
   :noindex:

.. function:: document.save_as(path)
   Example usage:

   *localc -> doc.save_as('/home/gyeh/hello.ods')*

   :param str path: The path to save the document to (must end with *.ods*)
   :return: *True* on success, *False* otherwise.
   :noindex:

.. function:: sheet.fetch_cell(cell_range)
   Selects a cell range.
   Example usage:

   *localc -> sheet.fetch_cell('A1')*

   :return: A *cell* object.
   :noindex:

.. function:: cell.set_text(string)
   Example usage:

   *localc -> cell.set_text("Hello, World!")*

   :param str string: A string to set the cell contents to.
   :return: *True* on success, *False* otherwise.
   :noindex:

.. function:: cell.get_text()
   Example usage:

   *localc -> cell.get_text()*
  
   :return: The cell's text.
   :noindex:

.. function:: cell.weight('bold')
   Example usage:

   *localc -> cell.weight('bold')*

   :return: *True* on success, *False* otherwise.
   :noindex:


.. _GitHub: https://github.com/Risto-Stevcev/iac-protocol 
