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


Requirements
============

| Python 3+


Usage
=====

**The easy way:** run ``pip install --user iac-protocol`` so pip can download it from PyPI, and go to step 5 on how to use the protocol.

#. Clone the repository.

#. Run ``python setup.py sdist`` from the project directory to create a
   source distribution.

#. Run ``pip install --user iac*.tar.gz`` from the new ``dist/``
   directory to install the package.

#. Enable an application for automation under the ``interfaces.py`` file, and read the official documentation for any additional setup instructions.

#. Run ``python -c "import iac.interpreter as iaci; iaci.main()"`` to
   play with the interactive interpreter.

   *or*

   Run ``python -c "import iac.server as iacs; iacs.main()"`` to quickstart the server.

To update the version:

#. Clone or pull the repository for the latest version.

#. Recreate the source distribution using the steps above.

#. Run ``pip upgrade iac*.tar.gz`` from the ``dist/`` directory to
   upgrade the package.

To uninstall, run ``pip uninstall iac-protocol``.

Please read the **official documentation** for complete instructions.
