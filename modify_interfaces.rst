:mod:`modify_interfaces` --- An interface for enabling/disabling applications
=============================================================================

.. index::
   single: modify
   single: interfaces
   
.. module:: modify_interfaces
   :synopsis: A simple module to modify the interfaces module in order to enable/disable applications.
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>.

The :mod:`modify_interfaces` module is used as a simple interface for modifying the :mod:`interfaces` 
module so that you don't have the edit the ``interfaces.py`` file manually.



Implementation
--------------

Here is the source code for the :mod:`modify_interfaces` module::

   import os

   _ROOT = os.path.abspath(os.path.dirname(__file__))
   _INTERFACES = 'interfaces.py'


   def modify(application_name, enable=True):
       new_interfaces = []
       with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
           for line in f:
               if application_name in line and enable:
                   new_interfaces.append(line.replace('#', ''))
               elif application_name in line and not enable:
                   new_interfaces.append("#" + line)
               else:
                   new_interfaces.append(line)
       with open(os.path.join(_ROOT, _INTERFACES), 'w') as f:
           for line in new_interfaces:
               f.write(line)

   def read():
       with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
           print(f.read())

   def enable(application_name):
       modify(application_name, enable=True)

   def disable(application_name):
       modify(application_name, enable=False)




Example
-------

Here's an example to enable LibreOffice Calc::
   
    python -c "import iac.modify_interfaces; iac.modify_interfaces.enable('lowriter')"

    --or--

    iacmodify --enable --app lowriter

The resulting ``interfaces.py`` file modified from a clean install of version 0.2 would look like::

    #import iac.app.libreoffice.calc as localc
    import iac.app.libreoffice.writer as lowriter
    #import iac.app.gnumeric as gnumeric

To disable it, you can do the following::

    python -c "import iac.modify_interfaces; iac.modify_interfaces.disable('lowriter')"

    --or--

    iacmodify --disable --app lowriter

Which would result in the following ``interfaces.py`` file::

    #import iac.app.libreoffice.calc as localc
    #import iac.app.libreoffice.writer as lowriter
    #import iac.app.gnumeric as gnumeric

To *read* the current ``interfaces.py`` file contents::

    python -c "import iac.modify_interfaces; iac.modify_interfaces.read()"

    --or--

    iacmodify --show

To view the help::

    iacmodify --help
