
.. _PYTHONDISTIDSINIT:

.. raw:: html

   <div class="shortcuttab">


pythonids.__init__
==================
The package 'pythonids' provides the canonical core enumerations 
of bit encoded numeric IDs for the Python syntax.


* **Constants and Attributes**

   .. raw:: html
   
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYVxyz <SPEC_PYVxyz>`            | [Python2]_ [Python3]_ | Current Implementation, integer                                     |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYV27X <SPEC_PYV27X>`            | [Python2]_            | Python2.7, bool                                                     |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYV3X <SPEC_PYV3X>`              | [Python3]_            | Python3, bool                                                       |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYV3X3 <SPEC_PYV3X3>`            | [Python3]_            | Python3.0 <= x <= Python3.3.x, bool                                 |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYV35Plus <SPEC_PYV35Plus>`      | [Python3]_            | Python3.5+, bool                                                    |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`PYV{x}[{y}[{z} <SPEC_PYV_x_y_z>` |                       | Pre-Defined Constants, integer                                      |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`ISSTR <SPEC_ISSTR>`              | [Python2]_ [Python3]_ | tuple of valid string types, includes *unicode* for *Python2*       |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+
   | :ref:`ISSTRBASE <SPEC_ISSTRBASE>`      | [Python2]_ [Python3]_ | tuple of valid *basestring* types, includes *unicode* for *Python2* |
   +----------------------------------------+-----------------------+---------------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>

* **Functions**

   .. raw:: html
   
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   | :ref:`decode_pysyntax_16bit_to_str <SPEC_decode_pysyntax_16bit_to_str>`             | [Python2]_ [Python3]_ | str "<major>.<minor>.<micro>"           |
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   | :ref:`decode_pysyntax_16bit_to_tuple <SPEC_decode_pysyntax_16bit_to_tuple>`         | [Python2]_ [Python3]_ | tuple (<major>, <minor>, <micro>)       |
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   | :ref:`decode_pysyntax_16bit_to_tuple_str <SPEC_decode_pysyntax_16bit_to_tuple_str>` | [Python2]_ [Python3]_ | tuple ("<major>", "<minor>", "<micro>") |
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   | :ref:`decode_pysyntax_str_to_num <SPEC_decode_pysyntax_str_to_num>`                 | [Python2]_ [Python3]_ | int                                     |
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   | :ref:`encode_pysyntax_to_16bit <SPEC_encode_pysyntax_to_16bit>`                     | [Python2]_ [Python3]_ | int                                     |
   +-------------------------------------------------------------------------------------+-----------------------+-----------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>


Module
------

.. automodule:: pythonids.__init__

Sources: `pythonids/__init__.py <_modules/pythonids/__init__.html#>`_

Constants
---------

.. _SPEC_PYV_x_y_z:

Syntax Releases - PYV{x}[{y}[{z}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Definitions of predefined values for the version of the Python syntax.
Some typical feature-milestone values are provided as runtime constants
for comparison operations as the resulting value from 
:ref:`encode_pysyntax_to_16bit() <SPEC_encode_pysyntax_to_16bit>`.
See :ref:`SPEC_PYVxyz`.

   .. index::
      pair: Python; PYV2
      pair: Python; PYV26
      pair: Python; PYV27
      pair: Python; PYV3
      pair: Python; PYV32
      pair: Python; PYV33
      pair: Python; PYV34
      pair: Python; PYV35
      pair: Python; PYV36
      pair: Python; PYV362
      pair: Python; PYV365
      pair: Python; PYV366
      pair: Python; PYV367
      pair: Python; PYV366
      pair: Python; PYV369
      pair: Python; PYV37
      pair: Python; PYV371
      pair: Python; PYV372
      pair: Python; PYV373
      pair: Python; PYV374
      pair: Python; PYV376
      pair: Python; PYV38

   .. parsed-literal::
   
      PYV2   = 16384  # encode_pysyntax_to_16bit(2, 0, 0)
      PYV26  = 17920  # encode_pysyntax_to_16bit(2, 6, 0)  - Python2.6
      PYV27  = 18176  # encode_pysyntax_to_16bit(2, 7, 0)  - Python2.7
      PYV3   = 24576  # encode_pysyntax_to_16bit(3, 0, 0)
      PYV32  = 25088  # encode_pysyntax_to_16bit(3, 2, 0)  - Python3.2
      PYV33  = 25089  # encode_pysyntax_to_16bit(3, 3, 0)  - Python3.3
      PYV34  = 25600  # encode_pysyntax_to_16bit(3, 4, 0)  - Python3.4
      PYV35  = 25856  # encode_pysyntax_to_16bit(3, 5, 0)  - Python3.5
      PYV36  = 26112  # encode_pysyntax_to_16bit(3, 6, 0)  - Python3.6
      PYV362 = 26114  # encode_pysyntax_to_16bit(3, 6, 2)
      PYV365 = 26117  # encode_pysyntax_to_16bit(3, 6, 5)
      PYV366 = 26118  # encode_pysyntax_to_16bit(3, 6, 6)
      PYV37  = 26368  # encode_pysyntax_to_16bit(3, 7, 0)  - Python3.7
      PYV371 = 26369  # encode_pysyntax_to_16bit(3, 7, 1)
      PYV372 = 26370  # encode_pysyntax_to_16bit(3, 7, 2)
      PYV373 = 26371  # encode_pysyntax_to_16bit(3, 7, 3)
      PYV374 = 26372  # encode_pysyntax_to_16bit(3, 7, 4)
      PYV376 = 26374  # encode_pysyntax_to_16bit(3, 7, 6)
      PYV38  = 26624  # encode_pysyntax_to_16bit(3, 8, 0)  - Python3.8

Encoding Support
^^^^^^^^^^^^^^^^

.. index::
   pair: unicode; ISSTR
   pair: Python2; ISSTR
   pair: Python3; ISSTR
   pair: Python; ISSTR

.. _SPEC_ISSTR:

ISSTR
^^^^^
Provides a tuple with valid string types:

   .. parsed-literal::
   
      if PYV35Plus:
          ISSTR = (str, bytes)  #: string and unicode
      
          #: Superpose for generic Python3 compatibility.
          unicode = str  # @ReservedAssignment
      
      elif PYV3X:
          ISSTR = (str, bytes)  #: string and unicode
      
          #: Superpose for generic Python3 compatibility.
          unicode = str  # @ReservedAssignment
      
      elif PYV27X:
          ISSTR = (str, unicode)  #: string and unicode
          unicode = unicode  # @ReservedAssignment

For the application by "*in*":

   .. parsed-literal::
   
      if type(s) in ISSTR:
          ...

.. index::
   pair: unicode; ISSTRBASE
   pair: str; ISSTRBASE
   pair: basestring; ISSTRBASE
   pair: Python2; ISSTRBASE
   pair: Python3; ISSTRBASE
   pair: Python; ISSTRBASE

.. _SPEC_ISSTRBASE:

ISSTRBASE
^^^^^^^^^
Provides a tuple with valid basic string types *basestring* - for *Python3* *(str,)*, and for *Python2* *(str, unicode,)*:

   .. parsed-literal::
   
      if PYV35Plus:
         ISSTRBASE = (str,)  #: str
      
      elif PYV3X:
         ISSTRBASE = (str,)  #: str
      
      elif PYV27X:
          ISSTRBASE = (str, unicode,)  #: basestr

For the application by "*in*":

   .. parsed-literal::
   
      if type(s) in ISSTRBASE:
          ...



.. index::
   pair: Python2; unicode
   pair: Python3; unicode
   pair: Python2; str


.. _SPEC_unicode:

unicode
^^^^^^^
Provides a syntax release dependent type reference *unicode*, which could be used
as a common type:

   .. parsed-literal::
   
      if PYV35Plus:
          unicode = str  # @ReservedAssignment
      
      elif PYV3X:
          unicode = str  # @ReservedAssignment
      
      elif PYV27X:
          unicode = unicode  # @ReservedAssignment


.. _ENUM_PYTHONDIST:

Attributes
----------
The following attributes are part of the official interface and could be used alternively
to the access functions.


.. index::
   pair: Python; PYV35Plus
   pair: Python; PYVxyz

.. _SPEC_PYVxyz:

PYVxyz
^^^^^^
Bit dynamic evaluated encoding of the current Python version.
The value is set automatic for the current performing Python interpreter during the load of the module.

  .. parsed-literal::

     Vxyz := xxxyyyyyzzzzzzzz
     
     xxx      := major version
     yyyyy    := minor version
     zzzzzzzz := build

     For example for the version "3.6.5": ::

     xxx      = 3 = 011
     yyyyy    = 6 = 00110
     zzzzzzzz = 5 = 00000101  
     
     xxxyyyyyzzzzzzzz = 26117 = 0b0110011000000101 

The value is evaluated by the call:

  .. parsed-literal::

     PYVxyz = encode_pysyntax_to_16bit(\*sys.version_info[:3])

This enables the binary checks with pre-defined integer values for fast frequent
evaluation:

  .. parsed-literal::

     if Vxyz & 26117:  # 0b0110011000000101
        # this is version 3.6.5

     if Vxyz & 26112:  # 0b0110011000000000
        # this is version 3.6

     if Vxyz < 26112:
        # this is pre-version 3.6, e.g. 3.5.x

The use of explicit numerical reference values is here perfectly applicable because of the 
static nature of version dependencies. 

For example the syntax release of Python-3.6.5:
   
.. code-block:: python
   :linenos:

   # xxx:      011
   # yyyyy:    00110
   # zzzzzzzz: 00000101

   PYVxyz = 0b0110011000000101 = 0x6605 = 26117


.. index::
   pair: Python; PYV27X

.. _SPEC_PYV27X:

PYV27X
^^^^^^
Adjust to current major syntax version - Python2.7.x.

.. code-block:: python
   :linenos:

   PYV27X = PYVxyz >= PYV27 and PYVxyz < PYV3 #: Python2.7
   if PYV27X:
       ISSTR = (str, unicode)  #: string and unicode

The definition includes also the helper variables *ISSTR* and *unicode*,
which support basic multiplatform encoding checks for Python2 and Python3. 

.. index::
   pair: Python; PYV3X

.. _SPEC_PYV3X:

PYV3X
^^^^^
Adjust to current syntax version - Python3.X.Y

.. code-block:: python
   :linenos:

   PYV3X = PYVxyz >= PYV3  #: Python3
   if PYV3X:
       PYV35Plus = True
       ISSTR = (str, bytes)  #: string and unicode
   
       #: Superpose for generic Python3 compatibility.
       unicode = str  # @ReservedAssignment
   

The definition includes also the helper variables *ISSTR* and *unicode*,
which support basic multiplatform encoding checks for Python2 and Python3. 

.. index::
   pair: Python; PYV3X3

.. _SPEC_PYV3X3:

PYV3X
^^^^^
Adjust to current syntax version - Python3.0 <= X <= Python3.3.X


.. index::
   pair: Python; PYV35Plus

.. _SPEC_PYV35Plus:

PYV35Plus
^^^^^^^^^
The numeric identifier of the supported Python versions.
In most of cases the Python version 3 is considered to contain a sustainable stable
feature set from the version 3.5 onward.
Thus the value of *PYV35Plus* is set as a runtime constant during load.

   .. parsed-literal::
   
     PYV35Plus := (
          True  # Python3.5+
        | False # Python2.7
     )

wirh the implementation:

   .. parsed-literal::
   
      PYV35Plus = PYVxyz >= PYV35  #: Python3.5+
      if PYV35Plus:
          ...


Functions
---------

.. _SPEC_decode_pysyntax_16bit_to_str:

decode_pysyntax_16bit_to_str
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: decode_pysyntax_16bit_to_str


    **Examples**:
    
      .. parsed-literal::

         decode_pysyntax_16bit_to_str(26117)   =>  '3.6.5'
         decode_pysyntax_16bit_to_str(PYV365)  =>  '3.6.5'


.. _SPEC_decode_pysyntax_16bit_to_tuple:

decode_pysyntax_16bit_to_tuple
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: decode_pysyntax_16bit_to_tuple

    **Examples**: 
    
      .. parsed-literal::

         decode_pysyntax_16bit_to_tuple(26117)   =>  (3, 6, 5)
         decode_pysyntax_16bit_to_tuple(PYV365)  =>  (3, 6, 5)


.. _SPEC_decode_pysyntax_16bit_to_tuple_str:

decode_pysyntax_16bit_to_tuple_str
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: decode_pysyntax_16bit_to_tuple_str

    **Examples**:

      .. parsed-literal::
      
         decode_pysyntax_16bit_to_tuple_str(26117)   =>  ('3', '6', '5')
         decode_pysyntax_16bit_to_tuple_str(PYV365)  =>  ('3', '6', '5')


.. _SPEC_decode_pysyntax_str_to_num:

decode_pysyntax_str_to_num
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: decode_pysyntax_str_to_num


.. _SPEC_encode_pysyntax_to_16bit:

encode_pysyntax_to_16bit
^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: encode_pysyntax_to_16bit

    **Examples**:
    
        Calculates the 16bit-mask for the Python release: 
        
           .. code-block:: python
              :linenos:
           
              from pythonids import PYV35, PYVxyz  # pre-defined values 
           
              from pythonids import encode_pysyntax_to_16bit      # function interface for the calculation
                                                     # of bit masks for releases
           
              # calculate non-pre-defined values
              pyv33 = encode_pysyntax_to_16bit(3, 3)
              pyv362 = encode_pysyntax_to_16bit(3, 6, 2)
              
              if PYVxyz & pyv33 == pyv33:
               # do s.th....
                 
              elif PyVxyz & pyv362 == pyv362:
               # do s.th. else...
                 
              elif PyVxyz >= PYV35:
               # do s.th. else...
                 
              else:
               # support the minimal and/or legacy spec....
        
        or
        
           .. code-block:: python
              :linenos:
           
              from pythonids import PYV35, PYVxyz  # pre-defined values 
           
              from pythonids import encode_pysyntax_to_16bit      # function interface for the calculation
                                                     # of bit masks for releases
           
              # calculate non-pre-defined values
              pyv3 = encode_pysyntax_to_16bit(3,)
              pyv33 = encode_pysyntax_to_16bit(3, 3)
              pyv362 = encode_pysyntax_to_16bit(3, 6, 2)
              
              if PYVxyz & pyv3 == pyv3:
                 if PYVxyz & pyv33 == pyv33:
                    # do s.th....
                    
              elif PyVxyz & pyv362 == pyv362:
                 # do s.th. else...
                    
              elif PyVxyz >= PYV35:
                 # do s.th. else...
                    
              else:
                 # support the minimal and/or legacy spec....
        
        For example from *sys.version_info*: 

            .. parsed-literal::
           
               x = sys.version_info[0]  # uses 3bits:  x: 0-7
               y = sys.version_info[1]  # uses 5bits:  y: 0-31
               z = sys.version_info[2]  # uses 8bits:  z: 0-255
        
           resulting in: ::
        
            .. parsed-literal::

               Vxyz = 0bxxxyyyyyzzzzzzzz
        
        For example:
        
            .. parsed-literal::

               x, y, z = (3, 6, 5)
               
               self.bits = (3, 5, 8)
               
               # => result = 0b 011 00110 00000101 
               # => result = 0b0110011000000101 =  26,117
    

Exceptions
----------

.. autoexception:: PythonIDsError
.. autoexception:: PythonIDsImplementationError

.. raw:: html

   </div>

