
*********
Blueprint
*********


.. _REFERENCE_ARCHITECTURE:

The package '*pythonids*' provides the normalized identity and release version information for the basic Python runtime system.
The information is provided in two flavours of integer values as compressed hierarchical bit-arrays
for efficient comparison operations by single-call numeric operations.
The difference to provided values by the standard distributions - beneath others - is the integrated support
of multiple Python distributions in order to select specialized code blocks, e.g. by relocatable cloud applications.
 
The '*pythonids*' provides the information acquisition of the process framework within the service stack.
The identifiers are designed for :ref:`resource efficient large scale operations <BITMASKSFORNUMERICVECTORS>`.

.. figure:: _static/systems-ids-sublayers.png
   :figwidth: 500
   :align: center
   :target: _static/systems-ids-sublayers.png
   
   Figure: Runtime Process Sublayers |figuresystemabstractsublayers_zoom|  :ref:`more... <REFERENCE_ARCHITECTURE3>`

.. |figuresystemabstractsublayers_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/systems-ids-sublayers.png
   :width: 16

The identifiers are thus packed into `hierarchical bit mask vectors <python_bitmasks.html#>`_.
These provide for combined operations of bitwise-comparison as well as simple
numeric order relations, while providing high perfomeance and memory efficiency
through fast binary and numeric standard operators.  

.. _REFERENCE_ARCHITECTURE3:

The *Python Syntax* version is packed into a bit-array, reducing the required code 
e.g. in case of the adaptation of current syntax and runtime library changes of *Python3.x.y* on the level of changes
for minor versions [PEP440]_.
For the specific distinction including the release version of the actual *Python Distribution* the global
variable *PYDIST* is provided by the module *pythonids.pythondist*, which provides the integrated information 
required for the identification of specific syntax variants and standard library sets.


.. _FIGURE_PYTHONIDSBLUEPRINT:

.. figure:: _static/pythonids-blueprint.png
   :figwidth: 1000
   :align: center
   :target: _static/pythonids-blueprint.png
   
   Figure: Python Infrastructure Services |figurepythonidsblueprint_zoom|

.. |figurepythonidsblueprint_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/pythonids-blueprint.png
   :width: 16

The numeric values of bitmasks replace the common standard values of arrays and strings,
which are originally in addition distributed in dependence of the platform over a variety
of libraries.
The bitmasks replace for example the partial comparison by *string-slices* and *startswith* with a bit-operation 
on a single integer value, reducing the pure comparison processing time for single operations, and in particular
in case of the repetitive comparison with array members.

Python Syntax Version
---------------------
The *pythonids* provides a :ref:`16bit bitmask for Python releases <BITMASKSSYNTAXRELEASES>`, for alternatives refer to *sys.hexversion* of the
various Python implementation and syntax variants.

* **pythonids.PYV35Plus** 

  The flag for the supported *Python Syntax* versions [`pythonids <package_init.html#v3k>`_]:

  .. code-block:: python
     :linenos:

     pythonids.PYV35Plus = (
         True,   # Python3.5+
         False   # Python2.7
     )

  For example:

  .. code-block:: python
     :linenos:

     from pythonids import PYV35Plus  # raises exception when not in 2.7 or 3.5+

     if PYV35Plus == True:
         # do sth. special for Python3...
   
      else:
         # do sth. else for Python2.7...

* **pythonids.PYVxyz**

  The combined bit-mask-flag of the *Python Syntax* version *PythonX.Y*
  and release  *PythonX.Y(Z)* is provided by the variable *Vxyz*
  [`PYVxyz <package_init.html#pyvxyz>`_]:

  .. code-block:: python
     :linenos:
  
     PYVxyz := 0bxxxyyyyyzzzzzzzz
   
     xxx:     3 bits / 0-7   for major version, e.g. 3       for 3.6.5  or e.g. future 4.0.2    
     yyyyy:   5 bits / 0-31  for minor version, e.g. 6       for 3.6.5  or e.g. future 3.14.3
     zzzzzz:  8 bits / 0-255 for the release build, e.g. 14  for 2.7.14 or e.g. future 2.7.23

  See also [`encode_pysyntax_to_16bit <package_init.html#encode-pysyntax-to-16bit>`_].

* **pythonids.encode_pysyntax_to_16bit()**

  Dynamic version evaluation by compressed bitmasks as single integer values
  by the slim and fast function interface
  [`encode_pysyntax_to_16bit <package_init.html#encode-pysyntax-to-16bit>`_].

  .. code-block:: python
    :linenos:
   
    PYV32 = encode_pysyntax_to_16bit(3, 2)        # integer
    myPYVxyz = encode_pysyntax_to_16bit(3, 6, 5)  # integer
   
    for x in range(1000000000):

       if PYVxyz & myPYVxyz:   # pure integer comparison - is the version 3.6.5
          callFunction0(x)
   
       elif PYV32 > myPYVxyz:  # pure integer comparison - is higher than version 3.2.0
          callFunction1(x)

       else:                   # is lower or equal version 3.2.0
          callFunction2(x)

See also `Python Syntax Versions <python_syntax_versions.html#>`_.

Python Distribution
-------------------
The *pythonids* provides a 
:ref:`32bit bitmask for 'Python Distribution' releases <PYTHONCATEGORIZATION>`
, which identify the actual current implementation of the 
execution framework including the major and minor version of the *Pyhton Syntax*.

* **pythonids.pythondist.PYDIST** 

  The combined bit-mask-flag of the *Python Distribution* version *Python-Variant-X.Y* with
  the major and minor syntax compatibility to *PythonX.Y*
  [`PYDIST <package_init.html#pydist>`_]:

  .. code-block:: python
     :linenos:
  
     PYDIST := 0bnxxxxxxxxyyyyyyzzzzzzzzzzzzzzzzzz

     n:                   1 bits    ignored, optional set as category Python    
     xxxxxxxx:            8 bits    for major and minor version of the Python Syntax    
     yyyyyy:              6 bits    enum value for the Python Distribution
     zzzzzzzzzzzzzzzzzz:  18 bits   release version of the Python Distribution

  See also [`encode_pydist_to_32bit <package_init.html#encode-pydistribution-to-32bit>`_].

* **pythonids.encode_pydist_to_32bit()**

  Dynamic version evaluation by compressed bitmasks as single integer values
  by the slim and fast function interface
  [`encode_pydist_to_32bit <package_init.html#encode-pydistribution-to-32bit>`_].

  The following example demonstrates the detection of *Cython* [Cython]_ and the specific
  release of *Cython* itself. This enables the appropriate selection of the special optimization
  for the best performance of the current application.
  The required overhead is basically negligible, in particular when multiple code segments require the
  same or similar environment dependent processing decisions.
  
  .. code-block:: python
    :linenos:
   
      from pythonids.pythondist import PYDIST, PYE_DIST, PYE_CPYTHON, PYE_PYPY, PYE_JYTHON, \
         encode_pydist_to_32bit
      
      CPYPY580PYV27 = encode_pydist_to_32bit(PYE_PYPY, 5, 8, 0, 2, 7)     # Syntax Python-2.7.13
      CPYPY5100PYV27 = encode_pydist_to_32bit(PYE_PYPY, 5, 10, 0, 2, 7)   # Syntax Python-2.7.13
      CPYPY5101PYV35 = encode_pydist_to_32bit(PYE_PYPY, 5, 10, 1, 3, 5)   # Syntax Python-3.5.3
      
      if PYDIST & PYE_DIST == PYE_PYPY:  # check by single integer value 
         #
         # for PyPy 
         #
      
         if PYDIST == CPYPY580PYV27:
            for x in range(1000000000):
               callFunctionOptimized0(x)
      
         elif PYDIST > CPYPY5100PYV27 and PYDIST < CPYPY5101PYV35:
            for x in range(1000000000):
               callFunctionOptimized1(x)
      
         elif PYDIST > CPYPY5101PYV35:
            for x in range(1000000000):
               callFunctionOptimized(x)
      
         else:                   
            for x in range(1000000000):
               callFunctionStillWorks(x)
      
      elif PYDIST & PYE_DIST == PYE_JYTHON:  # check by single integer value Jython
         #
         # for Jython
         #
         callFunctionJython(x)

      else:                   
         #
         # generic
         #
         callFunctionGeneric(x)


See also `Python Distribution Categorization <python_categorization.html#>`_.

Integer Type Comparison
-----------------------
The *Python* type *int* is common for values and in particular for enumerations and pseudo-const variables in *Python*.
Therefore commonly used in conditional clauses including checks on the *type*.
This causes some difficulties on *Jython*, because *Jython* uses the type *long*.
Thus the following *if* clause delivers different results on *Jython* and else.

.. parsed-literal::

   ix = 123123123123
   
   if type(ix) == int:
      res = True
   else:
      res = False
      
The results are different on implementations:

* on *CPython*, *IPython*, *IronPython*, and *PyPy*:

   .. parsed-literal::

      res = True

* on *Jython*:

   .. parsed-literal::

      res = False

The module *pythonids.pythondist* supports the constant *ISINT*:

   
   .. parsed-literal::

      if (PYDIST & PYE_DIST) == PYE_JYTHON:
          # Jython knows the type long - and casts to it from 32bit on
          isJython = True
          ISINT = (int, long,) 
      
      else:
          isJython = False
          ISINT = (int,)

thus the conditional clause:

   .. parsed-literal::

      from pythonids.pythondist import ISINT
      
      ix = 123123123123
      
      if type(ix) in ISINT:
         res = True
      else:
         res = False

delivers now the same result on all implementations:

   .. parsed-literal::

      res = True

See also :ref:`BITMASKSFORNUMERICVECTORS`.


Basic Unicode
-------------
The implementation of Python code for the versions Python2 and Python3
has to handle numerous changes.
The probably most frequent compatibility issue arises for the change of the string
representation.
Here the most common comparison and basic transformation could be handled
by the following patch.
See also [ISSUE32078]_. 

* **pythonids.ISSTR** and **pythonids.unicode**

  The simplified portability of encodings for Python2 and Python3
  is supported by the adapted type set *ISSTR* and the
  conditional *unicode* alias
  [`pythonids <package_init.html#>`_]:
   
  .. code-block:: python
     :linenos:
   
     if PYV35Plus:
        unicode = str           # applicable for basic compatibility only
        ISSTR = (str, bytes,)
   
     else:
        ISSTR = (str, unicode,)

See also `Python2 and Python3 Encoding and Decoding <python_encode_decode.html#>`_.
