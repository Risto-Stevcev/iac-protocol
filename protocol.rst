.. _protocol:

**************************
IAC protocol specification
**************************

.. index::
   single: protocol
   single: specification

The protocol implementation is in the :mod:`parser` module. The protocol specification could potentially
be implemented in a different language. Python, however, is the perfect language for this protocol because
of its introspective capabilities, its use as a glue language, and its general awesomeness!

The power of the parser and lexer are intentionally stripped down because calculations should be 
performed on the client-side. The protocol specification is simple and concerned only with object 
creation and functional calls to the provided interface.


.. _lexer:

Lexical definitions
===================

.. index::
   single: lexer
   single: lexical
   single: definitions

The lexer is kept intentionally simple. It tokenizes the operators, string literals, and
identifiers (also referred to as *names*). String literals currently do not support any 
escape sequences. The lexical definitions are as follows:

.. productionlist::
   stringliteral: "'" `stringchar`* "'" | '"' `stringchar`* '"' 
   stringchar: <any source character except newline or the quote>
   identifier: (`letter`|"_") (`letter` | `digit` | "_")*
   letter: `lowercase` | `uppercase`
   lowercase: "a"..."z"
   uppercase: "A"..."Z"
   digit: "0"..."9"
 

.. _operators:

Operators
=========

.. index:: 
   single: operators

The following tokens are operators::

   =       (       )
   .       ,       ->


The assignment operator ``=`` is used for variable assignment::

   identifier = expression

The parenthesis ``(`` and ``)`` operators are used to enclose function calls. The
``.`` operator is used to call an object-specific function. Objects and functions
are both identifiers::

   function()  
   | function(parameters)  
   | object.function()  
   | object.function(parameters)

The ``->`` operator is used for application scope. It is required for each command
so that the protocol knows which application to call::

   scope -> statement

The ``,`` operator is used as a delimiter for parameter arguments::

   function(argument1, argument2, ...)



.. _scope:

Scoped statements
=================

.. index::
   single: scope
   single: statements

Scoped statements are comprised of an application scope and a statement. The scoped statement 
is mandatory for every command in the protocol. The scope is an identifier. The application
looks for the passed in scope name in the :mod:`interfaces` module.

The scoped statement is the entry point for the parser. It is defined as:

.. productionlist::
   scoped_statement: `scope` "->" `statement`



.. _statements:

Statements
==========

.. index::
   single: statements

Statements are used to assign or call a value. The syntax is as follows:

.. productionlist::
   statement: `expression`
            : | `identifier` "=" `expression`



.. _expressions:

Expressions
===========

.. index::
   single: expressions

Expressions are used to call a value or procedure. The syntax is as follows:

.. productionlist::
   expression: `identifier`"()"
            : | `identifier` 
            : | `identifier`"("`parameters`")"
            : | `identifier`"."`identifier`"()"
            : | `identifier`"."`identifier`"("`parameters`")"
   parameters: `parameters`"," `optional_argument`
            : | `optional_argument`
   optional_argument: `stringliteral` | `digit` 



.. _implementation:

Implementation
==============

.. index::
   single: implementation

See the :mod:`interfaces` module and existing plug-ins for more details on plug-in implementation.


