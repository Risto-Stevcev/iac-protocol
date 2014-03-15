.. iac-protocol documentation master file, created by
   sphinx-quickstart on Wed Mar 12 04:13:43 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The IAC protocol
================

The IAC (*inter-application communication*) protocol is a protocol that enables inter-application communication and scripting. 

Have you ever wanted to program or script something using the internal functionality of a program, such as a document or spreadsheet program? This interface and protocol specification lets you do just that!

Create the automation scripts of your dreams, and contribute to the growing body of supported programs.

| **Is this a protocol or an interface?**
| It's both. The :ref:`protocol` section defines the protocol specification in case it's difficult to integrate an application to this interface implementation.
  The specification provides a simple parser that's intentionally stripped down, because all calculations should occur on the back-end of the plugin or within the
  automation script itself. The protocol supports UDP by default, since most uses would be localhost, and packets dropping aren't an issue. If it's accessed over a
  network, TCP is provided. If speed is an issue and congestion isn't, consider implementing TCP without congestion control. See the RFC-793_ specification for TCP 
  for more details. The interface implementation is the rest of this application, and there are several applications that can be used for script automation.

View the package in the PyPI repository_ 



Contents:

.. toctree::
   :numbered:

   intro.rst
   protocol.rst
   interfaces.rst
   modify_interfaces.rst
   interpreter.rst
   server.rst
   plugin.rst
   gnumeric.rst
   lowriter.rst
   localc.rst
   README.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _repository: https://pypi.python.org/pypi/iac-protocol
.. _RFC-793: http://www.ietf.org/rfc/rfc793.txt
