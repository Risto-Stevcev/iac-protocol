.. _lowriter:

******************
LibreOffice Writer
******************

.. default-domain:: py

.. index::
   single: libreoffice
   single: writer
   single: application

.. module:: lowriter
   :synopsis: The LibreOffice Writer application implementataion and documentation
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>


This page provides a guide on how to setup and use LibreOffice Writer for the IAC protocol.

.. warning::
    LibreOffice needs to have the UNO bridge running for it to function properly. Please see the instructions 
    for more details.



Instructions
============

#. Install LibreOffice.
   
#. Make sure that UNO works. Run ``import uno`` from the Python interpreter. It requires Python 3+. If it doesn't raise an ``ImportError`` then it works.

#. Run the UNO bridge. The UNO bridge is a server that provides a programming interface to access the internals of a LibreOffice document. 
 
   #. You can run multiple LibreOffice applications by passing them in as switches. If you want to use the ``current_document()`` command, then it will 
      only work on the first switch passed, in this case Calc. Here is the command to run UNO for Calc and Writer:
      ``libreoffice "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --calc --writer``
   
   #. If you want to run the bridge without opening any application, pass in the switch ``--headless``. You cannot use the ``current_document()`` command 
      in this mode because no application is running. Here is the command to write UNO for Calc and Writer:
      ``libreoffice --headless "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --calc --writer`` 

#. Make sure that the LibreOffice applications you want to use are enabled in the ``interfaces.py`` file. You can access LibreOffice writer using the ``lowriter`` 
   scope name.

#. Play with the :mod:`interpreter` to learn how the functionality works. Then use the :mod:`server` to create automation scripts! 

If you wish to contribute to LibreOffice Writer, try playing around with Python's library imports for LibreOffice Writer. But the best way is probably to view the 
UNO API documentation online, available from both LibreOffice and OpenOffice, which are essentially identical APIs. If the functionality is written in Java or another 
language, please try to change the logic to Python. The same namespace and class names are typically used, so this isn't usually difficult to do.

Then, clone the project repository from the project's GitHub_ page, add your modified application, and submit a pull request to be reviewed. If 
your additions to the application follow the protocol convention and it doesn't contain any obvious errors, it will be
accepted! See :ref:`plugin` for more details.



Example
=======

Here is a sample demonstrating LibreOffice Writer's functionality. First, run the UNO bridge::

   libreoffice "--accept=socket,host=localhost,port=18100;urp;StarOffice.ServiceManager" --norestore --nofirststartwizard --nologo --writer

Run the server (``iacs``) and then run the following ``Hello, World!`` shell script::

    #!/usr/bin/env bash
    # Netcat: -u is for UDP, -c closes the connection on EOF

    PORT=14733
    if [[ $# -eq 2 ]]; then
        echo -e "lowriter -> doc = new_document()\n" | nc -uc localhost $PORT 
        echo -e "lowriter -> text = doc.get_document_text()\n" | nc -uc localhost $PORT
        echo -e "lowriter -> text.set_text('$1')\n" | nc -uc localhost $PORT
        echo -e "lowriter -> doc.save_as('$2')\n" | nc -uc localhost $PORT
    else
        echo "Usage: $0 [string] [path]"
    fi

Or try the interpreter by directing the following as stdin::

    lowriter -> doc = new_document()
    lowriter -> text = doc.get_document_text()
    lowriter -> text.set_text('Hello, World!')
    lowriter -> doc.save_as('/home/gyeh/hello.odt')

And then run it as something like ``iaci < hello-lowriter.txt`` (assuming it's saved as that name).



Commands
========

.. function:: current_document()
   Selects the currently active document. Doesn't work if UNO is in headless mode.
   Example usage:
  
   *lowriter -> doc = current_document()*

   :return: A *document* object.

.. function:: load_document(path)
   Example usage:

   *lowriter -> doc = load_document('/home/gyeh/hello.odt')*

   :param str path: The path where the document is (must end with *.odt*)
   :return: A *document* object.

.. function:: new_document()
   Example usage:

   *lowriter -> doc = new_document()*

   :return: A *document* object.

.. function:: document.save_as(path)
   Example usage:

   *lowriter -> doc.save_as('/home/gyeh/hello.odt')*

   :param str path: The path to save the document to (must end with *.odt*)
   :return: *True* on success, *False* otherwise.

.. function:: document.save_as_pdf(path)
   Example usage:

   *lowriter -> doc.save_as_pdf('/home/gyeh/hello.pdf')*

   :param str path: The path to save the document to (must end with *.pdf*)
   :return: *True* on success, *False* otherwise.

.. function:: document.select_text()
   Selects the text that's currently highlighted in the document. Doesn't work if UNO is in headless mode.
   Example usage:

   *lowriter -> document.select_text()*

   :return: A *text_range* object.

.. function:: document.get_document_text()
   Selects the document text. This inherits a *text_range* object's properties.
   Example usage:

   *lowriter -> document.get_document_text()*

   :return: A *text* object (inherits *text_range*).

.. function:: text_range.set_text(string)
   Example usage:

   *lowriter -> text_range.set_text("Hello, World!")*

   :param str string: A string to set the text range contents to.
   :return: *True* on success, *False* otherwise.

.. function:: text_range.get_text()
   Example usage:

   *lowriter -> text_range.get_text()*
  
   :return: The text_range's text.

.. function:: text_range.weight('bold')
   Example usage:

   *lowriter -> text_range.weight('bold')*

   :return: *True* on success, *False* otherwise.


.. _GitHub: https://github.com/Risto-Stevcev/iac-protocol 
