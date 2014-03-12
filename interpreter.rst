:mod:`interpreter` --- The IAC protocol interpreter
===================================================

.. index::
   single: interpreter
   
.. module:: interpreter
   :synopsis: The IAC protocol interpreter providing an interactive shell.
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>.


The :mod:`interpreter` module is the interpreter for the IAC protocol. It provides a
command-line shell to execute and try out commands for simple use. If you are interested in
writing an automation script, check out the :mod:`server` module instead. But feel free to
use this interpreter to test out commands for a particular plug-in you are interested in using, 
or if you are developing for the protocol. 



Example
-------

You can run the interpreter directly by either executing ``interpreter.py`` in the IAC protocol's
application directory, or by importing it directly and running its ``main()`` method::

   python -c "import iac.interpreter as iaci; iaci.main()"
