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
==============

Here is the source code for the :mod:`modify_interfaces` module::

    import os
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    _INTERFACES = 'interfaces.py'

    def modify(application_name, uncomment=True):
        new_interfaces = []
        with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
            for line in f:
                if application_name in line and uncomment:
                    new_interfaces.append(line.replace('#', ''))
                elif application_name in line and not uncomment:
                    new_interfaces.append("#" + line)
                else:
                    new_interfaces.append(line)
        with open(os.path.join(_ROOT, _INTERFACES), 'w') as f:
            for line in new_interfaces:
                f.write(line)

    def read():
        with open(os.path.join(_ROOT, _INTERFACES), 'r') as f:
            print(f.read())



Example
-------

Here's an example to *uncomment* LibreOffice Calc::
   
   python -c "import iac.modify_interfaces; iac.modify_interfaces.modify('lowriter', uncomment=True)"

The resulting ``interfaces.py`` file modified from a clean install of version 0.2 would look like::

    #import iac.app.libreoffice.calc as localc
    import iac.app.libreoffice.writer as lowriter
    #import iac.app.gnumeric as gnumeric

To *comment* it back in order to disable it, you can do the following::

    python -c "import iac.modify_interfaces; iac.modify_interfaces.modify('lowriter', uncomment=False)"

Which would result in the following ``interfaces.py`` file::

    #import iac.app.libreoffice.calc as localc
    #import iac.app.libreoffice.writer as lowriter
    #import iac.app.gnumeric as gnumeric

To *read* the current ``interfaces.py`` file contents::

    python -c "import iac.modify_interfaces; iac.modify_interfaces.read()"
