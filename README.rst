.. _readme:

*******************
IAC protocol readme
*******************

.. index::
   single: readme


IAC protocol
============

The IAC (*inter-application communication*) protocol enables inter-application communication and scripting. 

Have you ever wanted to program or script something using the internal functionality of a program, such as a document or spreadsheet program? This interface and protocol specification lets you do just that!

Create the automation scripts of your dreams, and contribute to the growing body of supported programs.

View the package in the PyPI repository_ 


Requirements
============

| Python 2+


Usage
=====

**The easy way:** 

Run ``pip install --user iac-protocol`` (or omit --user for global install) so pip can download it from PyPI 
(may need sudo/root), and go to step 5 on how to use the protocol.

**The long way:**

#. Clone the repository.

#. Run ``python setup.py sdist`` from the project directory to create a
   source distribution.

#. Run ``pip install --user iac*.tar.gz`` (or omit --user for a global install) from the new ``dist/``
   directory to install the package (may need sudo/root).

#. Enable an application for automation from the command-line (may need sudo/root):

   ``iacmodify -s`` to show all available interfaces
   ``iacmodify --enable -a lowriter`` to enable libreoffice writer

#. Run ``iaci`` from the command-line to play with the interactive interpreter.

   *or*

   Run ``iacs`` to quickstart the server.

To update the version:

#. Clone or pull the repository for the latest version.

#. Recreate the source distribution using the steps above.

#. Run ``pip upgrade iac*.tar.gz`` from the ``dist/`` directory to
   upgrade the package.

To uninstall, run ``pip uninstall iac-protocol``.

Please read the official documentation_ for complete instructions.

.. _repository: https://pypi.python.org/pypi/iac-protocol
.. _documentation: http://pythonhosted.org/iac-protocol/
