.. _intro:

************
Introduction
************

.. index::
   single: introduction

The IAC (inter-application communication) protocol is a protocol/interface the enables 
inter-application communication and scripting. It provides a means to access the internal
functionality of an application and a means to create automation scripts.

Have you ever wanted a way to programmatically change the contents of a spreadsheet or
document? have you wanted to automate some process for a document with your favorite 
application? If so, this is the protocol for you. 

.. warning::
   The IAC protocol is not intended to be secure against erroneous or maliciously constructed
   data. Please make sure that user inputs are properly sanitized and constructed before
   passing them into the interpreter or server.
