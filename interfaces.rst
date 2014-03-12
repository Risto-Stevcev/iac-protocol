:mod:`interfaces` --- The IAC protocol application bridge
=========================================================

.. index::
   single: interfaces
   
.. module:: interfaces
   :synopsis: Used as the bridge between the IAC protocol and plug-in implementations.
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>.

The :mod:`interfaces` module is used as a bridge between plug-in implementations
and the IAC protocol's implementation. The parser communicates directly to the plug-in
through this module. It finds the application based on the value passed in as the
scope. If the scope matches the name in the :mod:`interfaces` module, it reads the
corresponding plug-in implementation.



Example
-------

Here is an example of the :mod:`interfaces` module from version 0.1::

   #import iac.app.libreoffice.calc as localc
   import iac.app.libreoffice.writer as lowriter
   import iac.app.gnumeric as gnumeric

All of the application implementations are stored in the *app/* folder. The
folder is treated like a package so that Python can find the applications. 
All registered applications must be stored in teh *app/* folder and they must
use the ``import iac.app.`` prefix in order to be registered properly by the
protocol. 

In order to avoid having to type ``iac.app.libreoffice.writer ->`` *(expression)*
as the namespace for the scope for every command, it is given the shortcut name 
``lowriter`` so that each command can simply be written as: 
``lowriter ->`` *(expression)*.

If the application contains multiple sub-applications, such as an office suite like
LibreOffice, you can create a new package under the *app/* folder with the name
of your application. Then you can pass it in like this example with LibreOffice.
Just be sure to include a blank ``__init__.py`` file in your application directory,
or Python won't recognize it as a package and the IAC protocol won't be able to
register it.

You can specify more than one application so that you can automate between
multiple programs. Unfortunately, as of the time writing this document, there
are no known ways to connect multiple LibreOffice applications to it's corresponding
UNO bridge. In this example, LibreOffice Calc is commented out so that the
IAC protocol can run properly. If you need spreadsheet and document automation at
the same time, you can do your spreadsheet automation with Gnumeric, or you can run
multiple instances of the protocol and UNO using different ports.
