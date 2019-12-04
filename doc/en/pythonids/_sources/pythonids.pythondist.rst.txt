
.. _PYTHONPARAMS:

.. raw:: html

   <div class="shortcuttab">


pythonids.pythondist
====================
The module 'pythondist' provides the class for the representation of the release parameters 
for the Python distribution. 
The *pythondist* module provides the runtime identifiers of *Python* distributions.
The aquisition of the iderntifiers is implemented by the scan of the current instance and the
one-time  calculation of the hexadecimal labels for the continued fast processing.


* **Constants and Attributes**

   .. raw:: html
   
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`PYDIST <SPEC_PYDIST>`              | [sys.version]_ [Python2]_ [Python3]_ | Current Implementation                                     |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`PYDIST_DATA <SPEC_PYDIST_DATA>`    | [sys.version]_  [Python2]_           | Global Instance of :ref:`PythonDist <SPEC_PythonDist>`     |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`PYE_{distrel}  <SPEC_PYE_distrel>` |                                      | Pre-Defined Implementation Constants                       |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`PYE_{helper}  <SPEC_PYE_helper>`   |                                      | Pre-Defined Bitmask Utility Constants                      |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`ISINT  <SPEC_ISINT>`               |                                      | tuple of valid integer types, includes *long* for *Jython* |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`ISNUM  <SPEC_ISNUM>`               |                                      | tuple of valid numeric types, includes *long* for *Jython* |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+
   | :ref:`isJython  <SPEC_isJython>`         |                                      | boolean for *Jython*                                       |
   +------------------------------------------+--------------------------------------+------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>

* **Functions**

   .. raw:: html

      <style>
         div.tmptab7 table td:nth-child(2) {
            background: lightgrey;
            border: none;
         }
         
      </style>
   
      <div class="tmptab7">
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
   | :ref:`decode_pydist_32bit_to_tuple <SPEC_decode_pydist_32bit_to_tuple>`                   | [CPython]_    | namedtuple: (<category>, <syntaxtype>, <dist>, <distrel>)         |
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
   | :ref:`decode_pydist_32bit_to_tuple_segments <SPEC_decode_pydist_32bit_to_tuple_segments>` | [IPython]_    | namedtuple: (<category>, <syntaxtype>, <dist>, <distrel>)         |
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
   | :ref:`decode_pydist_32bit_to_tuple_str <SPEC_decode_pydist_32bit_to_tuple_str>`           | [PyPy]_       | namedtuple: ("<category>", "<syntaxtype>", "<dist>", "<distrel>") |
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
   | :ref:`encode_pydist_to_32bit <SPEC_encode_pydist_to_32bit>`                               | [IronPython]_ | int/long                                                          |
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
   | :ref:`encode_pydist_segments_to_32bit <SPEC_encode_pydist_segments_to_32bit>`             | [Jython]_     | int/long                                                          |
   +-------------------------------------------------------------------------------------------+---------------+-------------------------------------------------------------------+
      
   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

* **Classes**

   .. raw:: html
   
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +-------------------------------------+-------------------------------+-------------------------------+
   | :ref:`PythonDist <SPEC_PythonDist>` | [CPython]_ [IPython]_ [PyPy]_ | the supported implementations |
   +-------------------------------------+-------------------------------+-------------------------------+
   |                                     | [IronPython]_                 |                               |
   +-------------------------------------+-------------------------------+-------------------------------+
   |                                     | [Jython]_                     |                               |
   +-------------------------------------+-------------------------------+-------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>

* **Python Helper**

   .. raw:: html
   
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +-------------------------------------------+-----------------------+----------------------------------+
   | :ref:`bash_map <SPEC_bash_map>`           | [bash]_ [SHELL]_      | namebinding for shell scripting  |
   +-------------------------------------------+-----------------------+----------------------------------+
   | :ref:`attribute_map <SPEC_attribute_map>` | [Python2]_ [Python3]_ | namebinding for Pyhton scripting |
   +-------------------------------------------+-----------------------+----------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>


Module
------

The values f the distribution identifier are either scanned by *scan()* method of the current instance

   .. code-block:: python
      :linenos:
      
      from pythonids.pythondist import PythonDist 
      
      x = PythonDist()    # creates an empty object
      x.scan()            # scans the Python instance
      print(str(x))       # prints display-format, see also 'repr', 'json', 'bashvars' and 'basharray'

or provided as call parameters for predictive cross-platform operations by offline evaluation.
For example with the following public attributes.
The values are defined as numeric bit field within 32-bit integer values, thus are
shifted to their defined positions, see also `Python Categorization <python_categorization.html#>`_ :

* Python-2.7.15 - CPython:

   .. parsed-literal::
   
      category         = PYE_PYTHON           # python
      disttype       = PYE_PYTHON27           # python-2.7.15
      dist             = PYE_CPYTHON          # CPython
      distrel          = bitmask(2, 7, 15)    # python2.7 - here same as syntax version
      hexrelease       = bitmask()            # overall bitmask

* Python-2.7.13 - PyPy-5.8.0:

   .. parsed-literal::
   
      category         = PYE_PYTHON           # python
      disttype       = bitmask(2, 7)          # python-2.7.13
      dist             = PYE_PYPY             # PyPy       
      distrel          = bitmask(5, 8, 0)     # pypy5.8
      hexrelease       = bitmask()            # overall bitmask



.. automodule:: pythonids.pythondist


Constants
---------

.. _SPEC_PYE_distrel:

Python Distributions
^^^^^^^^^^^^^^^^^^^^
The representation of the Python distribution parameter is an *int* used 
as bit-array for binary logic operations.
This comprises the *disttype*, the *dist*, and the *distrel* fields
encoded as subsections of the complete bitmask.
For details see :ref:`Python Categorization <PYTHONCATEGORIZATION>`.

.. _PYTHONDISTIDS:

The following predefined constants are available.

* The predefined bitmasks and support masks see also :ref:`current supported Python distributions <PYTHON_SUPPORTED>`.

.. _PYTHONDISTENUMS:

.. index::
   pair: pythonids.pythondist; PYDIST
   pair: pythonids.pythondist; PYE_PYTHON
   pair: pythonids.pythondist; PYE_CPYTHON
   pair: pythonids.pythondist; PYE_CYTHON
   pair: pythonids.pythondist; PYE_JYTHON
   pair: pythonids.pythondist; PYE_IPYTHON
   pair: pythonids.pythondist; PYE_IRONPYTHON
   pair: pythonids.pythondist; PYE_CIRCUITPYTHON
   pair: pythonids.pythondist; PYE_MICROPYTHON
   pair: pythonids.pythondist; PYE_PYPY
 
* Enum Values:

  * Base type blocks:

    *CPython* is basically the reference implementation of the Python Foundation @python.org, thus the
    distribution release is identical to the syntax release. 

    * **PYE_PYTHON** - Python
    * **PYE_PYTHON_PRETTY** - Python as string 'Python' 
    * **PYE_PYTHON_NAME** - Python name as string 'python' 

  * *disttype*:

    The specific syntax variant including the standard libraries. The standard libraries are
    in particular changing in the *Python3.X* releases, even for micro reelases *Python3.X.Z*. 

    * **PYE_PYTHON27** - Python-2.7
    * **PYE_PYTHON35** - Python-3.5
    * **PYE_PYTHON36** - Python-3.6
    * **PYE_PYTHON37** - Python-3.7

  * *dist*:

    The specific implementation for a given base syntax.
    While the base syntax is mostly complied thoroughly, the provided standard libraries frequently vary.

    * **PYE_IPYTHON** - *IPython*: [IPython]_.
    * **PYE_IRONPYTHON** - *IronPython*: [IronPython]_.
    * **PYE_JYTHON** - *Jython*: [Jython]_.
    * **PYE_PYPY** - *PyPy*: [PyPy]_.
    * **RTE_CPYTHON** - *CPython*: [CPython]_.

    A special case is here *Cython*, which provides a compiler - or basically a pre-processor - for 
    the *Python* syntax extended by *C* related syntax elements.

    * **PYE_CYTHON** - *Cython*: [Cython]_.

  * *dist* as special syntax and package variants for small SoCs with small footprints:

    * **PYE_CIRCUITPYTHON** - *CircuitPython*: [CircuitPython]_.
    * **PYE_MICROPYTHON** - *MicroPython*: [MicroPython]_.

* Control Variables:

  * **PYDIST**: Current Python distribution

For the complete list refer to the sources [`pythonids.__init__.py <_modules/pythonids/__init__.html#>`_]
and [`pythonids/pythondist.py <_modules/pythonids/pythonids.pythondist.html#>`_].

.. _SPEC_PYE_helper:

Bitmask Helper
^^^^^^^^^^^^^^
The following constants provide the extraction of subfields for logic operations by bitmasks.
The bitmasks used for *pythonids* are semantically separative, thus the value of the field itself
is valid, even though e.g. a specific version may not be actually available for the distribution.
Thus the logical layers are in a hierarchical order, but the type of the content is not cumulative,
though formally not bound to it's upper layer.  
The bit values are kept by the bitmask decomposition at their original positions.

* Syntax type bits:

  * **PYE_SYNTAXTYPE**  - extracts a single value for major and minor version
  * **PYE_SYNTAXTYPE_MAJOR** - extracts the major only
  * **PYE_SYNTAXTYPE_MINOR** - extracts the minor only

* Distribution type bits

  * **PYE_DIST** - extracts dist enum only

* Distribution release version bits:

  * **PYE_DISTREL** - extracts the combined value for major, minor, and micro version
  * **PYE_DISTREL_MAJOR** - extracts the major only
  * **PYE_DISTREL_MINOR** - extracts the minor only
  * **PYE_DISTREL_MICRO** - extracts the micro only

.. index::
   pair: pythonids.pythondist; ISINT
   pair: Jython; ISINT

.. _SPEC_ISINT:

ISINT
^^^^^
Provides a tuple of valid integer types. 
This is required in particular for *Jython*, due to it's use of the type *long* for numeric values
with 32 or more bits.
The *long* type is not supported by the syntax releases *Python3* and *Python2* - not specified in the
grammar specification [Python2]_/[Python3]_, but actually understood by *CPython2.7.15*.


   .. parsed-literal::
   
      for Jyhton: ISINT = (int, long,)  # *long* for values of 32bits and more 
      else:       ISINT = (int,) 

For the application by *in*:

   .. parsed-literal::
   
      if type(s) in ISINT:
          ...

.. index::
   pair: pythonids.pythondist; ISNUM
   pair: Jython; ISNUM

.. _SPEC_ISNUM:

ISNUM
^^^^^
Provides a tuple of valid numeric types. 
This is required in particular for *Jython*, due to it's use of the type *long* for numeric values
with 32 or more bits.
The *long* type is not supported by the syntax releases *Python3* and *Python2* - not specified in the
grammar specification [Python2]_/[Python3]_, but actually understood by *CPython2.7.15*.

   .. parsed-literal::
   
      for Jyhton: ISNUM = (int, float, long,)  # *long* for values of 32bits and more 
      else:       ISNUM = (int, float,) 


For the application by *in*:

   .. parsed-literal::
   
      if type(s) in ISNUM:
          ...

Variables
---------

.. index::
   pair: pythonids.pythondist; PYDIST

.. _SPEC_PYDIST:

PYDIST
^^^^^^

.. autodata:: pythonids.pythondist.PYDIST
   :annotation:

   The bit encoded Python distribution identifier of current executable for bit mask operations.
   
      .. code-block:: python
         :linenos:
      
         PYDIST = encode_pysyntax_to_16bit(*sys.version_info[:3])
      
         e.g. for Python-3.6.5
         
         xxx:      011
         yyyyy:    00110
         zzzzzzzz: 00000101
      
         PYVxyz = 0b0110011000000101 = 0x6605 = 26117
   
   Du to the static nature of the version number code dependencies the reference values could be 
   provided as integer constants when frequent evaluation is required.

.. index::
   pair: pythonids.pythondist; PYDIST_DATA

.. _SPEC_PYDIST_DATA:

PYDIST_DATA
^^^^^^^^^^^
.. autodata:: pythonids.pythondist.PYDIST_DATA
   :annotation:

   A global object of *pythonids.pythondist.PythonDist* initialized with the data of the current runtime environment.
   The default is with core attributes only - which almost for sure must not raise exceptions at all.

.. index::
   pair: pythonids.pythondist; isJython

.. _SPEC_isJython:

isJython
^^^^^^^^
Provides a boolean value of the detection status of *Jython*.

   .. parsed-literal::
   
      isJython =: (True | False)

Maps
^^^^
The followin maps provide the data for shell scripting.

.. _SPEC_bash_map:

**bash_map**

The corresponding *bash* environment names. 
   ::

      bash_map = {
          'category': "PYDIST_CATEGORY",
          'disttype': "PYDIST_DISTTYPE",
          'dist': "PYDIST_DIST",
          'distrel': "PYDIST_DISTREL",
          'hexrelease': "PYDIST_DISTREL_HEXVERSION",
          'compiler': "PYDIST_COMPILER",
          'compiler_version': "PYDIST_COMPILER_VERSION",
          'c_libc_version': "PYDIST_C_LIBC_VERSION",
          'c_compiler': "PYDIST_C_COMPILER",
          'c_compiler_version': "PYDIST_C_COMPILER_VERSION",
      }

.. _SPEC_attribute_map:

**attribute_map**

The mapping of attributes to values. 
   ::

      attribute_map = {
          'category': "category",
          'disttype': "disttype",
          'dist': "dist",
          'distrel': "distrel",
          'hexrelease': "hexrelease",
          'compiler': "compiler",
          'compiler_version': "compiler_version",
          'c_libc_version': "c_libc_version",
          'c_compiler': "c_compiler",
          'c_compiler_version': "c_compiler_version",
      }

.. _SPEC_decode_pydist_32bit_to_tuple_segments:

decode_pydist_32bit_to_tuple_segments
-------------------------------------
.. autofunction:: decode_pydist_32bit_to_tuple_segments

   Example::
   
     example_ = pythonids.pythondist.decode_pydist_32bit_to_tuple_segments(
        0xa38421cf
        )
     
     example == {
        'category': 1,             # Python
        'disttype': (2, 7),        # Python release: 2.7
        'dist': 1,                 # CPython
        'distrel': (2, 7, 15)      # CPython release: 2.7.15
     }


.. _SPEC_decode_pydist_32bit_to_tuple_str:

decode_pydist_32bit_to_tuple_str
--------------------------------
.. autofunction:: decode_pydist_32bit_to_tuple_str

   Example::
   
      example_ = pythonids.pythondist.decode_pydist_32bit_to_tuple_str(
         0xa38421cf
         )
      
      example = {
         'category': 'python',      # Python
         'disttype': 'python2.7',   # Python release: 2.7
         'dist': 'cpython',         # CPython
         'distrel': '2.7.15'        # CPython release: 2.7.15
      }


.. _SPEC_decode_pydist_32bit_to_tuple:

decode_pydist_32bit_to_tuple
----------------------------
.. autofunction:: decode_pydist_32bit_to_tuple

   Example::
   
      example_ = pythonids.pythondist.decode_pydist_32bit_to_tuple_str(
         0xa38421cf
         )
      
      example = (
         2147483648,               # PYE_PYTHON   
         595591168,                # PYE_PYTHON27
         262144,                   # PYE_CPYTHON
         8655                      # 2.7.15
      )


.. _SPEC_encode_pydist_to_32bit:

encode_pydist_to_32bit
----------------------
.. autofunction:: encode_pydist_to_32bit

   Example:

      For details refer to the component *distrel* of :ref:`Bit Mask Layout <BITMASKLAYOUTDIST>`.

         .. parsed-literal::
   
            example_ = pythonids.pythondist.encode_pydist_to_32bit(
               pythonids.pythondist.PYE_CPYTHON,
               2, 7, 15,
               2,7,
               )
           
            example = 0xa38421cf = PYE_PYDIST_CPYTHON2715


.. _SPEC_encode_pydist_segments_to_32bit:

encode_pydist_segments_to_32bit
-------------------------------
.. autofunction:: encode_pydist_segments_to_32bit

   Example:

      For details refer to the component *distrel* of :ref:`Bit Mask Layout <BITMASKLAYOUTDIST>`.

         .. parsed-literal::
   
            example_ = pythonids.pythondist.encode_pydist_to_32bit(
               category='python',
               dist='cpython',
               distrel=(2, 7, 15),
               disttype=(2, 7),
               )
           
            example = 0xa38421cf = PYE_PYDIST_CPYTHON2715


.. _SPEC_PythonDist:

PythonDist
----------
The class *PythonDist* provides the representation of Python distributions. 
The data contains either the current runtime environment, or a user provided platform
by parameters.
The automatic scan of the current runtime environment has to be triggered explicitly 
by the method `pythonids.PythonDist.scan() <#scan>`_.
The call replaces all attribute values of the current instance by the detected values.

.. autoclass:: PythonDist

   The provided public attributes are:
   
   * **category**:
   
     The 32-bit enum of category of the syntax. Here the only value is *PYE_PYTHON*.
   
   * **disttype**:
   
     The 32-bit encoded major and minor version of the Python syntax 
     definition - PEP440 - finalrelease (2-value).
   
   * **dist**:
   
     The 32-bit encoded enum of the Python distribution.
   
   * **distrel**:
   
     The 32-bit encoded major, minor, and micro version of the Python
     interpreter/compiler distribution.
   
   * **hexrelease**:
   
     The numeric 32-bit bitmask for the complete set of information.
      ::

         hexrelease = (category | disttype | dist | distrel)
     
     See `bitmasks <python_categorization.html#>`_.
   
   
   The following extra attributes are optional and not yet reliable on 
   all OS platforms at production degree. These are scanned only when
   the attribute *forceall* is set to *True*. This is not the case for
   the global default object. 
   
   Anyhow, in some cases such as *PyPy* it is implemented in combination 
   with the *distrel* information and ... |smilecool|.
   
   * **c_compiler**:
   
     The lower case name of the compiler for the dist.
   
   * **c_compiler_version**:
   
     The 3-value integer version tuple of the compiler. 
   
   * **c_libc_version**:
   
     The tuple of the name and 3-value integer version tuple of the C-library
     from *platform.libc_ver*. 
   
   
Attributes
^^^^^^^^^^

The following public attributes are provided for the 
:ref:`hierachical platform categorization <HIERARCHPYTHONCATEGORIES>`

.. _SPEC_category:

**category**

The 32bit encoded type of operating system. 

   .. parsed-literal::
   
      category := PYE_PYTHON

.. _SPEC_disttype:

**disttype**

The 32bit encoded value of the Python syntax release. 
See :ref:`bitmasks <BITMASKLAYOUTDIST>`:

   .. parsed-literal::
   
      disttype := (<disttype-major>, < disttype-minor>)

Predefined values are:

   .. parsed-literal::
   
      PYE_PYTHON27, PYE_PYTHON35, PYE_PYTHON36, PYE_PYTHON37 

.. _SPEC_dist:

**dist**

The 32bit encoded enum of the distribution. 
See :ref:`bitmasks <BITMASKLAYOUTDIST>`:

   .. parsed-literal::
   
      dist := (
           PYE_CPYTHON
         | PYE_IPYTHON
         | PYE_IRONPYTHON
         | PYE_JYTHON
         | PYE_PYPY
         #
         # experimental
         #
         | PYE_CIRCUITPYTHON  # experimental
         | PYE_MICROPYTHON    # experimental
      )

.. _SPEC_distrel:

**distrel**

The 32bit encoded value of the implementation release. 
See :ref:`bitmasks <BITMASKLAYOUTDIST>`:

   .. parsed-literal::
   
      distrel := (<distrel-major>, <distrel-minor>, <distrel-micro>)

The values are for the reference implementation *CPython* the same as the syntax release, 
but differ for other implementations.

.. _SPEC_hexrelease:

**hexrelease**

The 32bit numeric bitmask of the release version representing all previous
attributes within one value. See
:ref:`bitmasks <BITMASKLAYOUTDIST>`.

The presented values are optional and may change unnoticed.
These are primarily intended for the test of the *pythonids* itself.
Due to the amout of possible versions these have to be calculated dynamically.


   .. parsed-literal::
   
      distrel := (
           PYE_PYDIST_CPYTHON2715    # 0xa38421cf - CPython-2.7.15   - Python2.7
         | PYE_PYDIST_CPYTHON372     # 0xb38431c2 - CPython-3.7.2    - Python3.7
         | PYE_PYDIST_IPYTHON550     # 0xA3905140 - IPython-5.5.0    - Python2.7
         | PYE_PYDIST_IPYTHON560     # 0xA3905180 - IPython-5.6.0    - Python2.7
         | PYE_PYDIST_IRONPYTHON277  # 0xA39421C7 - IRonPython-2.7.7 - Python2.7
         | PYE_PYDIST_IRONPYTHON279  # 0xA39421C9 - IRonPython-2.7.9 - Python2.7
         | PYE_PYDIST_JYTHON270      # 0xA39821C0 - Jython-2.7.0     - Python2.7
         | PYE_PYDIST_JYTHON271      # 0xA39821C1 - Jython-2.7.1     - Python2.7
         | PYE_PYDIST_PYPY580        # 0xA3A05200 - PyPy-5.8.0       - Python2.7
         | PYE_PYDIST_PYPY60027      # 0xA3A06000 - PyPy-6.0.0       - Python2.7
         | PYE_PYDIST_PYPY60035      # 0xB2A06000 - PyPy-6.0.0       - Python3.5
         | PYE_PYDIST_PYPY70036      # 0xB3207000 - PyPy-7.0.0       - Python3.6
      )

.. _SPEC_forceall:

**forceall**

Controls the scan of the compiler and libc information when set to *True*.
Is by default *False*, thus in global instance too.


.. _SPEC_c_libc_version:

**c_libc_version**

The version of the used libc.

.. _SPEC_c_compiler:

**c_compiler**

The name of the used compiler.

.. _SPEC_c_compiler_version:

**c_compiler_version**

The version of the used compiler.

__init__
^^^^^^^^
.. automethod:: PythonDist.__init__

__and__
^^^^^^^
.. automethod:: PythonDist.__and__
   
__eq__
^^^^^^
.. automethod:: PythonDist.__eq__
   
__ge__
^^^^^^
.. automethod:: PythonDist.__ge__

__getattr__
^^^^^^^^^^^
.. automethod:: PythonDist.__getattr__

__getitem__
^^^^^^^^^^^
.. automethod:: PythonDist.__getitem__

__gt__
^^^^^^
.. automethod:: PythonDist.__gt__
   
__iand__
^^^^^^^^
.. automethod:: PythonDist.__iand__

__int__
^^^^^^^
.. automethod:: PythonDist.__int__

__ior__
^^^^^^^
.. automethod:: PythonDist.__ior__

__iter__
^^^^^^^^
.. automethod:: PythonDist.__iter__

__le__
^^^^^^
.. automethod:: PythonDist.__le__

__lt__
^^^^^^
.. automethod:: PythonDist.__lt__

__ne__
^^^^^^
.. automethod:: PythonDist.__ne__

   See *__eq__*.

__or__
^^^^^^
.. automethod:: PythonDist.__or__

__rand__
^^^^^^^^
.. automethod:: PythonDist.__rand__

__repr__
^^^^^^^^
.. automethod:: PythonDist.__repr__

__ror__
^^^^^^^
.. automethod:: PythonDist.__ror__

__setattr__
^^^^^^^^^^^
.. automethod:: PythonDist.__setattr__

__setitem__
^^^^^^^^^^^
.. automethod:: PythonDist.__setitem__

__str__
^^^^^^^
.. automethod:: PythonDist.__str__

get_distribution
^^^^^^^^^^^^^^^^
.. automethod:: PythonDist.get_distribution
   
get_hexrelease
^^^^^^^^^^^^^^
.. automethod:: PythonDist.get_hexrelease

items
^^^^^
.. automethod:: PythonDist.items

keys
^^^^
.. automethod:: PythonDist.keys

scan
^^^^
.. automethod:: PythonDist.scan

values
^^^^^^
.. automethod:: PythonDist.values


.. _SPEC_PyDist_Class:

PyDist
------
.. autoclass:: PyDist 

   
.. _SPEC_PyDistSegments:

PyDistSegments
--------------
.. autoclass:: PyDistSegments 

   
.. _SPEC_PyDistStr:
   
PyDistStr
---------
.. autoclass:: PyDistStr 
   
Exceptions
----------

.. autoexception:: PythonDistError

.. raw:: html

   </div>


.. |smilecool| imagewrap:: _static/smiling-face-with-sunglasses-32x32.png
   :width: 16
   :alt: :-)
