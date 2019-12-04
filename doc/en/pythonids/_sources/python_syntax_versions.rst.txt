
.. _PYTHONSYNTAXVERSIONS:

Python Syntax Versions
======================
The programming language Python is under evolutionary development, thus changes
it's overall syntax frequently.
The syntax is defined hereby within the context of this package as the complete programming interface, which
includes the APIs of the provided standard libraries.
The current major step is the phase of the final switch over from *Python2* to *Python3*.
The syntax is hereby defined by the *major* and *minor* version numbers - an optional additional third number - and provided as
the main and reference implementation by the distribution *CPython* of the *Python Foundation*.
Thus the versions of the *CPython* distribution has the version numbering of the syntax revision,
see [PEP440]_.
The optional *micro* number is not available at the call interface - e.g. *python2*, *python2.7* - and normally
at least in case of the reference implementation *CPython* not relevant for the syntax decision.

The syntax - or better the APIs of the close to system level standard libraries changed from the release
*Python3.0* to *Python3.4* significantly - including based on the *micro* number - while for Python3.5+ the APIs remain widely stable.
Thus code supporting these releases, e.g. for the original Python distribution of RHEL6, may require some
conditional code sections even down to the level of the *micro* version.

The common Python version identifier could be easily represented as a combined bitmask,
see `A bit of Theory - Bit Masks for Numeric Vectors <python_bitmasks.html#>`_.

.. _BITMASKSSYNTAXRELEASES:

A bit of Theory
---------------
The *Python* release defines pure syntax of the *Python* language, but also the standard library API. 
This comprises major cases such as the subprocess calls and multi threading, but frequently 
minor call details such as for the *ConfigParser* and the exchange of deprecated interfaces.
This is in addition superposed by derivates such as *IPython* and *MicroPython* including the 
sub-derivative *CircuitPython*, but also
by alternative implementations such as *PyPy* , *IronPython*, and *Jython*.
The application has to decide whether the syntax alone, or the distribution is relevant for the
adaptation of specific code segments. 
For the enumeration and detection of the distributions refer to the section 
:ref:`Python Syntax and Distribution Categorization <PYTHONCATEGORIZATION>`.

In case of some close-to-system libraries of the lower layer, but also on application level for example
in conjunction with multiprocessing, it could become challenging to implement and deploy common code
for multiple platforms such as generic cloud applications.

The *pythonids* package provides a 16bit value with a set of constants for conditional code segments
in order to provide application focused 3-number release versions.   

The specific bit masks are designed for Python releases are of fixed sizes,
representing the standard values with an appropriate spare range.
The overall size is designed to fit into a 16bit register.
The current supported value ranges are:

   .. code-block:: python
      :linenos:
   
      import sys
   
      sys.version_info[0]  # major version - represented by 3bits:  0-7
      sys.version_info[1]  # minor version - represented by 5bits:  0-31
      sys.version_info[2]  # micro version - represented by 8bits:  0-255

This patttern requires in total 16bits, and provides the ranges:

.. math::
   :label: python_version_ranges

   \begin{split}
   v(x_{major})&: 0<=i<8\\
   v(x_{minor})&: 0<=i<32\\
   v(x_{build})&: 0<=i<256
   \end{split}

which provides a range of:   

.. math::
   :label: python_version_value_range

   Python0.0.0 <= Px <= Python7.31.255

The bitmask layout of the integer value is: 

   |bitmaskpyvers|
   |bitmaskpyvers_zoom|
   
   .. |bitmaskpyvers_zoom| imagewrap:: _static/zoom.png
      :alt: zoom 
      :target: _static/bitarray-python.png
      :width: 16
   
   .. |bitmaskpyvers| imagewrap:: _static/bitarray-python.png
      :width: 300

For example the version *Python-3.6.5* is represented as:

   |bitmaskpyvers365|
   |bitmaskpyvers365_zoom|
   
   .. |bitmaskpyvers365_zoom| imagewrap:: _static/zoom.png
      :alt: zoom 
      :target: _static/bitarray-python365.png
      :width: 16
   
   .. |bitmaskpyvers365| imagewrap:: _static/bitarray-python365.png
      :width: 300

or as numeric representation:

   .. code-block:: python
      :linenos:
   
      0b0110011000000101 = 031405 = 0x3305 = 13061


The features  may in addition vary by the specific platform, which results  
in several system dependent libraries with a few to significant differences.
The ongoing development of the version Python3 evolves with a continous
change of major and minor features including dependency on the micro versions.
The system platform is represented by the standard library *sys* as:

   .. parsed-literal::
   
      sys.platform  # the label of current platform
                    # e.g. 'linux2', 'win32', 'darwin'

The package *pythonids* provides canonical numerical values on a higher granularity
for the supported system platforms.
This enables in addition for code of system dependent variants controlled by
simple and fast integer comparison operations.
For the implementation details refer to [`encode_pysyntax_to_16bit() <package_init.html#encode_pysyntax_to_16bit>`_].

The following code-example depicts an example for the combined application:

   .. parsed-literal::
   
      import sys
   
      if sys.version_info[0] > 2:
         # Python3
         # prepare loop
      
      for i in range(100000):
         if sys.version_info[0] > 2:
            # Python3
      
            if sys.version_info[1] < 5:
               # Python - 3.0 < 3.5
               
               if sys.platform in ('linux2', 'darwin'):
                  # do s. th.
               else:
                  # do s.th. else.
   
            if sys.version_info[1] < 6 an sys.version_info[2] < 4:
               # Python - 3.5.0 < 3.5.3
               # do s. th.
      
            if sys.version_info[2] < 3:
               # Python - 3.5.4 < 3.6.3
               # do s. th.
   
         elif sys.version_info[1] > 6:
            # Python2.7
   
            if sys.platform == 'linux2':
               # do s. th.
   
            elif sys.platform == 'darwin':
               # do s. th.
   
            elif sys.platform == 'win32':
               # do s. th.
   
            else:
               # do s.th. else.
   
         else:
            # PythonX <= Python2.6  
   
            if sys.platform == 'win32':
               raise Exceptio("Not supported.")
   
            # do s.th....

The same based on static bit masks of version dependency:  

   .. parsed-literal::
   
      from pythonids import RTE, RTE_LINUX, RTE_OSX, RTE_WIN32
      from pythonids import PYV35Plus, Vxyz, encode_pysyntax_to_16bit
   
      if PYV35Plus:
         # Python3
         # prepare loop
   
      v27  = encode_pysyntax_to_16bit(2, 7)
      v35  = encode_pysyntax_to_16bit(3, 5)
      v353 = encode_pysyntax_to_16bit(3, 5, 3)
      v363 = encode_pysyntax_to_16bit(3, 6, 3)
       
      for i in range(100000):
         if PYV35Plus:
            # Python3
      
            if not Vxyz & v35:
               # Python - 3.0 < 3.5
   
               if RTE & RTE_POSIX:
                  # do s. th.
               else:
                  # do s.th. else.
      
            elif  Vxyz & v353:
               # Python - 3.5.0 < 3.5.3
               # do s. th.
      
            elif not Vxyz & v363:
               # Python - 3.5.4 < 3.6.3
               # do s. th.
   
   
         elif Vxyz & v27:
            # Python2.7
   
            if RTE & RTE_LINUX:
               # do s. th.
   
            elif RTE & RTE_OSX:
               # do s. th.
   
            elif RTE & RTE_WIN32:
               # do s. th.
   
            else:
               # do s.th. else.
   
         else:
            # PythonX <= Python2.6  
   
            if not RTE & RTE_WIN32:
               raise Exceptio("Not supported.")
   
            # do s.th....




   .. code-block:: python
      :linenos:
   
      from pythonids import PYV35Plus, encode_pysyntax_to_16bit
   
      # bit-mask values               # 0bxxxxyyyyyzzzzzzz
      vref363  = encode_pysyntax_to_16bit(3, 6, 3)     # 0b0011001100000011 == 13,059
      vref32   = encode_pysyntax_to_16bit(3, 2)        # 0b0011000100000000 == 12,544
      vref27   = encode_pysyntax_to_16bit(2, 7)        # 0b0010011100000000 ==  9,984
      vref2714 = encode_pysyntax_to_16bit(2, 7, 14)    # 0b0010011100001110 ==  9,998
      vref26   = encode_pysyntax_to_16bit(2, 6)        # 0b0010001100000000 ==  8,960
      vref245  = encode_pysyntax_to_16bit(2, 4, 5)     # 0b0010001000000101 ==  8,709
   
      myStaticScalar = encode_pysyntax_to_16bit(  #      0bxxxxyyyyyzzzzzzz
         *sys.version_info[:3]   # e.g. 0b0010010000000011 == 8,709 := (2, 4, 5) 
      )   
      
      def myTempPrePython3Handler():
         if myStaticScalar >= vref2714:
            # for 2.7.14+
            alternative1a()
   
         elif myStaticScalar & vref27:
            # for 2.7.0 - 2.7.13
            alternative1b()
   
         elif myStaticScalar < vref27:
            # for pre-2.7
            alternative2()
   
   
      for i in range(1000000):  # 1.000.000
   
         if not PYV35Plus:
            # for PythonX < Python3
            myTempPrePython3Handler()
   
         elif myStaticScalar > vref363:
            # for the introduced new feature of 3.6.4+
            #
            # the only remaining variant for the revision once
            # the support for the Python2 and Python 3.0.0 - 3.6.3
            # variants are canceld
            #
            target_variant()
   
         else:
            # for 3.0 <= x <= 3.6.2
            temporary_alternative_python3_migration()

This code could be later easily modified to *Python3* support only:

   .. code-block:: python
      :linenos:
   
      # bit-mask values               # 0bxxxxyyyyyzzzzzzz
      vref363  = encode_pysyntax_to_16bit(3, 6, 3)     # 0b0011001100000011 == 13,059
      vref32   = encode_pysyntax_to_16bit(3, 2)        # 0b0011000100000000 == 12,544
   
      myStaticScalar = encode_pysyntax_to_16bit(  #      0bxxxxyyyyyzzzzzzz
         *sys.version_info[:3]   # e.g. 0b0011010000000011 == 8,709 := (3, 4, 5) 
      )   
      
      for i in range(1000000):  # 1.000.000
   
         if myStaticScalar > vref363:
            # for 3.6.4+
            target_variant()
   
         else:
            # for 3.0 <= x <= 3.6.2
            temporary_alternative_python3_migration()

and later as easy migrated to the final target of stable *Python3* features only.

   .. code-block:: python
      :linenos:
   
      for i in range(1000000):  # 1.000.000
         target_variant()


The following example demonstrates the application in order to handle 
the changes of the Python interpreter.
 
   .. code-block:: python
      :linenos:
   
      import sys
      from pythonids import PYVxyz, PYV35, PYV33, PYV2, \\
         encode_pysyntax_to_16bit
   
      #: The Python release of current process
      PYVxyz = encode_pysyntax_to_16bit(*sys.version_info[:3])
   
      modfpath = os.path.dirname(__file__)+os.sep+'dist'+os.sep+_impmodname + '.py'
      try:
          if PYV35Plus: # PYVxyz >= PYV35: # Python 3.5+
              import importlib.util  # @UnresolvedImport
              spec = importlib.util.spec_from_file_location(_impmodname, modfpath)  # @UndefinedVariable
              if spec:
                  _modx = importlib.util.module_from_spec(spec)  # @UndefinedVariable
                  spec.loader.exec_module(_modx)
      
          elif PYVxyz >= PYV33: # Python 3.3 and 3.4
              from importlib.machinery import SourceFileLoader  # @UnresolvedImport
              _modx = SourceFileLoader(_impmodname, modfpath).load_module()
      
          elif PYVxyz & PYV2: # Python 2 - verified and released for 2.7 only, but don't block
              import imp
              _modx = imp.load_source(_impmodname, modfpath)
      
          sys.modules[_impmodname] = _modx
          globals()[_impmodname] = _modx
      
      except KeyError:
          # continue with generic
          pass

Supported Python Releases
-------------------------

The following Python interpreters and releases are used to veriy and test the code:

   +---------------+-------+-------+--------------------+
   | Python        | major | minor | distrel            |
   +===============+=======+=======+====================+
   | CPython       | 2     | 7     | CPython-2.7        |
   +---------------+-------+-------+--------------------+
   | CPython       | 3     | 5+    | CPython-3.5+       |
   +---------------+-------+-------+--------------------+
   | CircuitPython | 3     | 4     | CircuitPython-3.0+ |
   +---------------+-------+-------+--------------------+
   | Cython        | 2     | 7     | Cython-0.27+       |
   +---------------+-------+-------+--------------------+
   | Cython        | 3     | 0+    | Cython-3.0a3       |
   +---------------+-------+-------+--------------------+
   | IronPython    | 2     | 7     | IronPython-2.7+    |
   +---------------+-------+-------+--------------------+
   | Jython        | 2     | 7     | Jython-2.7         |
   +---------------+-------+-------+--------------------+
   | MicroPython   | 3     |       |                    |
   +---------------+-------+-------+--------------------+
   | PyPy          | 2     | 7     | PyPy-5.8+          |
   +---------------+-------+-------+--------------------+
   | PyPy          | 3     | 5+    |                    |
   +---------------+-------+-------+--------------------+
   | iPython       | 2     | 7     | IPython-5.5+       |
   +---------------+-------+-------+--------------------+
   | iPython       | 3     | 5+    | IPython-6.3+       |
   +---------------+-------+-------+--------------------+

Syntax Versions API
-------------------
See also `Shortcuts <shortcuts.html#>`_.

Constants
^^^^^^^^^
The following constants provide pre-defined release values.

   `PYV2 PYV27 PYV3 PYV32 PYV33 PYV34 PYV35 PYV36 PYV362 PYV365 PYV366 PYV367 PYV368 PYV369 PYV37 PYV371 PYV372 PYV373 PYV374 PYV375 PYV376 PYV38 <package_init.html#constants>`_


Variables
^^^^^^^^^
The provided variables are forseen to be uused by applications in fast and efficient numerical and boolean operations.

* `The 3-value Python final release of the current process in accordance to PEP440. <package_init.html#attributes>`_ [PEP440]_

   .. parsed-literal::

      PYVxyz

* `Attributes to adjust to current major Python version to Python3 vs. Python2. <package_init.html#attributes>`_

   .. parsed-literal::

      PYV35Plus       # Python3.5+ - to be changed to 3.0+
      PYV35Plus     # Python3.5+ - the safe constant
      ISSTR     # string and unicode
      unicode   # Superpose for generic Python3 compatibility.

Functions
^^^^^^^^^
   .. raw:: html
   
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +---------------------------------------+-------------------------------------------------+
   | [docs]                                | [source]                                        |
   +=======================================+=================================================+
   | `decode_pysyntax_str_to_num`_         | `pythonids.decode_pysyntax_str_to_num`_         |
   +---------------------------------------+-------------------------------------------------+
   | `decode_pysyntax_16bit_to_str`_       | `pythonids.decode_pysyntax_16bit_to_str`_       |
   +---------------------------------------+-------------------------------------------------+
   | `decode_pysyntax_16bit_to_tuple`_     | `pythonids.decode_pysyntax_16bit_to_tuple`_     |
   +---------------------------------------+-------------------------------------------------+
   | `decode_pysyntax_16bit_to_tuple_str`_ | `pythonids.decode_pysyntax_16bit_to_tuple_str`_ |
   +---------------------------------------+-------------------------------------------------+
   | `encode_pysyntax_to_16bit`_           | `pythonids.encode_pysyntax_to_16bit`_           |
   +---------------------------------------+-------------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
   
   .. _decode_pysyntax_16bit_to_str: package_init.html#pythonids.__init__.decode_pysyntax_16bit_to_str
   .. _decode_pysyntax_16bit_to_tuple: package_init.html#pythonids.__init__.decode_pysyntax_16bit_to_tuple
   .. _decode_pysyntax_16bit_to_tuple_str: package_init.html#pythonids.__init__.decode_pysyntax_16bit_to_tuple_str
   .. _decode_pysyntax_str_to_num: package_init.html#pythonids.__init__.decode_pysyntax_str_to_num
   .. _encode_pysyntax_to_16bit: package_init.html#pythonids.__init__.encode_pysyntax_to_16bit
   .. _pythonids.decode_pysyntax_16bit_to_str: _modules/pythonids/__init__.html#decode_pysyntax_16bit_to_str
   .. _pythonids.decode_pysyntax_16bit_to_tuple: _modules/pythonids/__init__.html#decode_pysyntax_16bit_to_tuple
   .. _pythonids.decode_pysyntax_16bit_to_tuple_str: _modules/pythonids/__init__.html#decode_pysyntax_16bit_to_tuple_str
   .. _pythonids.decode_pysyntax_str_to_num: _modules/pythonids/__init__.html#decode_pysyntax_str_to_num
   .. _pythonids.encode_pysyntax_to_16bit: _modules/pythonids/__init__.html#encode_pysyntax_to_16bit

Corresponding values in case of the current process are provided e.g. by *sys.version* and *sys.version_info*.


Comparison with sys.hexversion
------------------------------
The standard library provides for the Python syntax version information also the numeric value
*sys.hexversion*, which is similar to *pythonids.PYVxyz*.

   .. code-block:: python
      :linenos:
      
      sys.hexversion

The original standard library covers the core *Python* syntax including the standard libraries of
the reference implementation *CPython*.
It has to be considered that the API including the provided libraries may deviate for the same syntax release version 
on alternative implementations. 
This frequently requires additional checks in order to determine the actual implementation of the current *Python*
distribution, see  :ref:`Python Distribution Categorization <PYTHONCATEGORIZATION>`.

The numeric representation is described in the manual [CPython]_.
The value consumes 32bits, the encoded fields comprise some additional release 
information of interest for the Python interpreter developers only.

   .. code-block:: python
      :linenos:
   
      import sys
   
      sys.version_info[0]  # major version
      sys.version_info[1]  # minor version
      sys.version_info[2]  # micro version  or build-tag
      sys.version_info[3]  # textual label of release level, current:
                           # ('alpha' | 'beta' | 'candidate' | 'final') 
      sys.version_info[4]  # serial number, frequently '0'


Both variants do not contain the identification of integrated language variants
which is covered by the *Python* distribution,
see  :ref:`Python Distribution Categorization <PYTHONCATEGORIZATION>`.

The syntax of *Python* for final production releases is specified by the *major(PY_MAJOR_VERSION)* 
and *minor(PY_MINOR_VERSION)* version number, while the optional *build(PY_MICRO_VERSION)* number
could already be ignored in most cases [FINALRELEASE]_.
So the *PY_RELEASE_LEVEL* and the *PY_RELEASE_SERIAL* are not meaningful relevant for production grade code,
but are eventually used for internal test purposes.

The content of the *sys.hexversion* comprises the 3-value version identifier of the 
current Python release with additional production information of the Python interpreter itself.

   +-------------------------+---------------------------------------------------------------------------------------------+
   | Bits (big endian order) | Meaning                                                                                     |
   +=========================+=============================================================================================+
   | 1-8                     | PY_MAJOR_VERSION (the 2 in 2.1.0a3)                                                         |
   +-------------------------+---------------------------------------------------------------------------------------------+
   | 9-16                    | PY_MINOR_VERSION (the 1 in 2.1.0a3)                                                         |
   +-------------------------+---------------------------------------------------------------------------------------------+
   | 17-24                   | PY_MICRO_VERSION (the 0 in 2.1.0a3)                                                         |
   +-------------------------+---------------------------------------------------------------------------------------------+
   | 25-28                   | PY_RELEASE_LEVEL (0xA for alpha, 0xB for beta, 0xC for release candidate and 0xF for final) |
   +-------------------------+---------------------------------------------------------------------------------------------+
   | 29-32                   | PY_RELEASE_SERIAL (the 3 in 2.1.0a3, zero for final releases)                               |
   +-------------------------+---------------------------------------------------------------------------------------------+

While the 3-value version identifier actually identifies relevant information on the syntax 
and library API releases, the additional values provide basically information non/transparent to the
system and application developer.
In addition the comparison operations require additional steps in order to eliminate the additional bits.

The  *pythonids.PYVxyz* focusses solely on the semantics related to the Python syntax
and API definition as required for systems and application development[FINALRELEASE]_.
Therefore utilizes the first 3-values only.
This reduces the number of operations required on comparison opreations under some circumstances significantly.

   +-------+-------------------------------------------------+
   | Bits  | Meaning                                         |
   +=======+=================================================+
   | 15-13 | PY_MAJOR_VERSION: 0<= v <= 7  (the 3 in 3.6.4)  |
   +-------+-------------------------------------------------+
   | 12-8  | PY_MINOR_VERSION: 0<= v <= 31 (the 6 in 3.6.4)  |
   +-------+-------------------------------------------------+
   | 7-0   | PY_MICRO_VERSION: 0<= v <= 255 (the 4 in 3.6.4) |
   +-------+-------------------------------------------------+

The endiannes is "visually similar" to the order of decimal integer numbers, thus virtually little-endian.

The size of  *sys.hexversion* is 32bit while the size of *pythonids.PYVxyz* is 16bit. 
The 16bit based layout seems to be sufficient for atleast more than the next three to four decades,
if the syntax evolution continues with curretn rate of change, else even longer.
Thus virtually 'endless' in terms of IT application life cycles.

Resources
---------

* CPython [CPython]_
* CircuitPython [CircuitPython]_
* Cython [Cython]_
* Detect if python script is run from an ipython shell, or run from the command line [ARTICLESTACKOFLOWIPYTHON]_
* In Python how can one tell if a module comes from a C extension? [ARTICLESTACKOFLOWCEXT]_ 
* IPython [IPython]_
* IronPython [IronPython]_
* Jython [Jython]_
* MicroPython [MicroPython]_
* PEP407 - New release cycle and introducing long-term support versions [PEP407]_
* PEP421 - Adding sys.implementation - [PEP421]_
* PEP440 - Version Identification and Dependency Specification [PEP440]_
* PEP440 [PEP440]_  - section final releases [FINALRELEASE]_
* PyPy [PyPy]_
* Software Versioning [SWVERS]_

