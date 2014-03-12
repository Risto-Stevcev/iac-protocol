:mod:`server` --- The IAC protocol server
=========================================

.. index::
   single: server
   
.. module:: server
   :synopsis: The IAC protocol server for creating automation scripts.
.. sectionauthor:: Risto Stevcev <risto1@gmail.com>.


The :mod:`server` module is the server for the IAC protocol. This is the way that the IAC 
protocol provides a means to create automation scripts. This is also the reason why the
protocol is language and platform independent. It supports any language and platform that 
supports socket programming.

Most use cases would be primarily interested in script automation locally, but since this 
is a server, it is capable of handling remote automation calls as well. This makes the
protocol incredibly flexible.


Example
-------

You can run the server directly by either executing ``server.py`` in the IAC protocol's
application directory, or by importing it directly and running its ``main()`` method::

   python -c "import iac.server as iacs; iacs.main()"


Usage
-----

The server can be run in TCP or UDP mode. It is in UDP mode by default. You can view all
of the usage options by running ``server.py -h``. Here is the usage for version 0.1::

    usage: server.py [-h] [-p PORT] [-s BUFFER_SIZE] [-t TIMEOUT] [-b BACKLOG]
                     [-l LOG_FILE] [--tcp | --udp]

    Server for IAC Protocol 0.1 - by Risto Stevcev.

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  server port (default: 14733)
      -s BUFFER_SIZE, --buffer-size BUFFER_SIZE
                            buffer size (default: 1024)
      -t TIMEOUT, --timeout TIMEOUT
                            server timeout (default: None)
      -b BACKLOG, --backlog BACKLOG
                            maximum connections (default: 5)
      -l LOG_FILE, --log-file LOG_FILE
                            log file (default: stdout)
      --tcp                 TCP connection
      --udp                 UDP connection (default)
