.. _intro:

************
Introduction
************

.. index::
   single: introduction

The IAC (inter-application communication) protocol is a protocol/interface the enables 
inter-application communication and scripting. It provides a means to access the internal
functionality of application and a means to create automation scripts.

Have you ever wanted a way to programmatically change the contents of a spreadsheet or
document? have you wanted to automate some process for a document with your favorite 
application? If so, this is the protocol for you. 

The project is currently in it's infancy, but it supports LibreOffice (and essentially 
OpenOffice since they both use UNO), and Gnumeric. If you would like to contribute to
this project, please don't hesitate to sent me an email. 

I currently need to build on the functionality of the LibreOffice suite and Gnumeric, and
I'm looking to add OpenOffice as well. All of these use Python for their plug-in interface.
Python is perfect for this protocol because it's introspective capabilities make it much
easier to find properties and functionality when documentation is scarce. 

If you would like to contribute and the plugin interface for the application is not in 
Python, please send me an email so that I can help you create an interface. The license is
BSD and allows you to create a fork of this project with the proper credits, but in order 
to keep everything standardized and in one place, I recommend sending a pull request and 
contributing to this project directly. I'll strongly consider any differences in design
implementation.

.. warning::
   The IAC protocol is not intended to be secure against erroneous or maliciously constructed
   data. Please make sure that user inputs are properly sanitized and constructed before
   passing them into the interpreter or server.
