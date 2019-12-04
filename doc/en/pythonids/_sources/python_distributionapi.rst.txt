
Distribution Versions API
=========================
See also `Shortcuts <shortcuts.html#>`_.

Variables
---------

* `The corresponding *bash* environment names. <pythonids.pythondist.html#maps>`_ 

   .. parsed-literal::

        bash_map

* `The mapping of attributes to values. <pythonids.pythondist.html#maps>`_ 

   .. parsed-literal::

        attribute_map

PythonDist
----------
See also `Shortcuts <shortcuts.html#>`_.

Attributes
^^^^^^^^^^

* The tuple of Python identifiers:

   .. parsed-literal::

      category
      disttype
      dist
      distrel

* Additional shortcuts prepared for direct processing:

   .. parsed-literal::

      hexrelease

* In addition the optional, but strongly supported attributes. 
  Controlled by the parameter *forceall*:

   .. parsed-literal::

      c_libc_version
      c_compiler
      c_compiler_version


Methods
^^^^^^^
   .. raw:: html
   
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +------------------------------+---------------------------------------------------+--------------------------------------------------------------+
   | [doc]                        | [source]                                          |                                                              |
   +==============================+===================================================+==============================================================+
   | `PythonDist.__init__`_       | `pythonids.pythondist.PythonDist.__init__`_       |                                                              |
   +------------------------------+---------------------------------------------------+--------------------------------------------------------------+
   | `PythonDist.__str__`_        | `pythonids.pythondist.PythonDist.__str__`_        |                                                              |
   +------------------------------+---------------------------------------------------+--------------------------------------------------------------+
   | `PythonDist.get_hexrelease`_ | `pythonids.pythondist.PythonDist.get_hexrelease`_ | calculates and caches current resulting hex value            |
   +------------------------------+---------------------------------------------------+--------------------------------------------------------------+
   | `PythonDist.scan`_           | `pythonids.pythondist.PythonDist.scan`_           | scans current local platform and replaces current attributes |
   +------------------------------+---------------------------------------------------+--------------------------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
  

Operators
^^^^^^^^^
The operators commonly operate on the *hexrelease* values.
When these are not yet available, they will be created on the fly.
Thus these operations are quite costly, so use the bublic attributes where possible.
Anyhow, in cases where performance does not count, e.g. for offline tools, the operators
provide a smart toolset. 

   .. raw:: html
   
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +------------+--------------------------+-----------------------------------------------+
   | operator   | [doc]                    | [source]                                      |
   +============+==========================+===============================================+
   | S + x      | `PythonDist.__and__`_    | `pythonids.pythondist.PythonDist.__and__`_    |
   +------------+--------------------------+-----------------------------------------------+
   | S == x     | `PythonDist.__eq__`_     | `pythonids.pythondist.PythonDist.__eq__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S >= X     | `PythonDist.__ge__`_     | `pythonids.pythondist.PythonDist.__ge__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S > X      | `PythonDist.__gt__`_     | `pythonids.pythondist.PythonDist.__gt__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S &= X     | `PythonDist.__iand__`_   | `pythonids.pythondist.PythonDist.__iand__`_   |
   +------------+--------------------------+-----------------------------------------------+
   | int(S)     | `PythonDist.__int__`_    | `pythonids.pythondist.PythonDist.__int__`_    |
   +------------+--------------------------+-----------------------------------------------+
   | S |pi| = x | `PythonDist.__ior__`_    | `pythonids.pythondist.PythonDist.__ior__`_    |
   +------------+--------------------------+-----------------------------------------------+
   | S <= x     | `PythonDist.__le__`_     | `pythonids.pythondist.PythonDist.__le__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S < x      | `PythonDist.__lt__`_     | `pythonids.pythondist.PythonDist.__lt__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S != x     | `PythonDist.__ne__`_     | `pythonids.pythondist.PythonDist.__ne__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | S |pi| x   | `PythonDist.__or__`_     | `pythonids.pythondist.PythonDist.__or__`_     |
   +------------+--------------------------+-----------------------------------------------+
   | x & S      | `PythonDist.__rand__`_   | `pythonids.pythondist.PythonDist.__rand__`_   |
   +------------+--------------------------+-----------------------------------------------+
   | x |pi| S   | `PythonDist.__ror__`_    | `pythonids.pythondist.PythonDist.__ror__`_    |
   +------------+--------------------------+-----------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
   

Iterators
^^^^^^^^^
The main task using the iterators is the automatic synchronization of the attributes with the *hexrelease*.

   .. raw:: html
   
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | operator   | [doc]                     | [source]                                       | remarks                                              |
   +============+===========================+================================================+======================================================+
   | x = S.k    | `PythonDist.__getattr__`_ | `pythonids.pythondist.PythonDist.__getattr__`_ |                                                      |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | S.k = x    | `PythonDist.__setattr__`_ | `pythonids.pythondist.PythonDist.__setattr__`_ | synchronises all dependencies, else raises excpetion |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | x = S[k]   | `PythonDist.__getitem__`_ | `pythonids.pythondist.PythonDist.__getitem__`_ |                                                      |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | S[k] = x   | `PythonDist.__setitem__`_ | `pythonids.pythondist.PythonDist.__setitem__`_ | synchronises all dependencies, else raises excpetion |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | values(S)  | `PythonDist.items`_       | `pythonids.pythondist.PythonDist.items`_       | yield list of tupels                                 |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | S.keys()   | `PythonDist.keys`_        | `pythonids.pythondist.PythonDist.keys`_        | yield list of attribute names                        |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   | S.values() | `PythonDist.values`_      | `pythonids.pythondist.PythonDist.values`_      | yield list of attribute values                       |
   +------------+---------------------------+------------------------------------------------+------------------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
   
   .. _PythonDist.__and__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__and__
   .. _PythonDist.__eq__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__eq__
   .. _PythonDist.__ge__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__ge__
   .. _PythonDist.__getitem__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__getitem__
   .. _PythonDist.__getattr__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__getattr__
   .. _PythonDist.__gt__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__gt__
   .. _PythonDist.__iand__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__iand__
   .. _PythonDist.__init__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__init__
   .. _PythonDist.__int__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__int__
   .. _PythonDist.__invert__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__invert__
   .. _PythonDist.__ior__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__ior__
   .. _PythonDist.__iter__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__iter__
   .. _PythonDist.__le__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__le__
   .. _PythonDist.__lt__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__lt__
   .. _PythonDist.__ne__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__ne__
   .. _PythonDist.__or__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__or__
   .. _PythonDist.__rand__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__rand__
   .. _PythonDist.__repr__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__repr__
   .. _PythonDist.__ror__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__ror__
   .. _PythonDist.__setattr__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__setattr__
   .. _PythonDist.__setitem__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__setitem__
   .. _PythonDist.__str__: pythonids.pythondist.html#pythonids.pythondist.PythonDist.__str__
   .. _PythonDist.get_hexrelease: pythonids.pythondist.html#pythonids.pythondist.PythonDist.get_hexrelease
   .. _PythonDist.items: pythonids.pythondist.html#pythonids.pythondist.PythonDist.items
   .. _PythonDist.keys: pythonids.pythondist.html#pythonids.pythondist.PythonDist.keys
   .. _PythonDist.scan: pythonids.pythondist.html#pythonids.pythondist.PythonDist.scan
   .. _PythonDist.values: pythonids.pythondist.html#pythonids.pythondist.PythonDist.values
   .. _pythonids.pythondist.PythonDist.__and__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__and__
   .. _pythonids.pythondist.PythonDist.__eq__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__eq__
   .. _pythonids.pythondist.PythonDist.__ge__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__ge__
   .. _pythonids.pythondist.PythonDist.__getitem__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__getitem__
   .. _pythonids.pythondist.PythonDist.__getattr__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__getattr__
   .. _pythonids.pythondist.PythonDist.__gt__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__gt__
   .. _pythonids.pythondist.PythonDist.__iand__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__iand__
   .. _pythonids.pythondist.PythonDist.__init__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__init__
   .. _pythonids.pythondist.PythonDist.__int__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__int__
   .. _pythonids.pythondist.PythonDist.__invert__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__invert__
   .. _pythonids.pythondist.PythonDist.__ior__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__ior__
   .. _pythonids.pythondist.PythonDist.__iter__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__iter__
   .. _pythonids.pythondist.PythonDist.__le__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__le__
   .. _pythonids.pythondist.PythonDist.__lt__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__lt__
   .. _pythonids.pythondist.PythonDist.__ne__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__ne__
   .. _pythonids.pythondist.PythonDist.__or__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__or__
   .. _pythonids.pythondist.PythonDist.__rand__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__rand__
   .. _pythonids.pythondist.PythonDist.__repr__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__repr__
   .. _pythonids.pythondist.PythonDist.__ror__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__ror__
   .. _pythonids.pythondist.PythonDist.__setattr__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__setattr__
   .. _pythonids.pythondist.PythonDist.__setitem__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__setitem__
   .. _pythonids.pythondist.PythonDist.__str__: _modules/pythonids/pythonids.pythondist.html#PythonDist.__str__
   .. _pythonids.pythondist.PythonDist.get_hexrelease: _modules/pythonids/pythonids.pythondist.html#PythonDist.get_hexrelease
   .. _pythonids.pythondist.PythonDist.items: _modules/pythonids/pythonids.pythondist.html#PythonDist.items
   .. _pythonids.pythondist.PythonDist.keys: _modules/pythonids/pythonids.pythondist.html#PythonDist.keys
   .. _pythonids.pythondist.PythonDist.scan: _modules/pythonids/pythonids.pythondist.html#PythonDist.scan
   .. _pythonids.pythondist.PythonDist.values: _modules/pythonids/pythonids.pythondist.html#PythonDist.values
   
   

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
* Performance of Python runtimes on a non-numeric scientific code [PYIMPPERFORM]_
* PyPy [PyPy]_


.. |bitarraycpython2715_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-cpython2715.png
   :width: 16

.. |bitarraycpython2715| imagewrap:: _static/bitarray-complete-to-bytes-example-cpython2715.png
   :width: 550

.. |bitarraycpython371_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-cpython371.png
   :width: 16

.. |bitarraycpython371| imagewrap:: _static/bitarray-complete-to-bytes-example-cpython371.png
   :width: 550

.. |bitarraycython027_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-cython027.png
   :width: 16

.. |bitarraycython027| imagewrap:: _static/bitarray-complete-to-bytes-example-cython027.png
   :width: 550

.. |bitarraycython30_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-cython300.png
   :width: 16

.. |bitarraycython30| imagewrap:: _static/bitarray-complete-to-bytes-example-cython300.png
   :width: 550

.. |bitarrayipython56_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-ipython56.png
   :width: 16

.. |bitarrayipython56| imagewrap:: _static/bitarray-complete-to-bytes-example-ipython56.png
   :width: 550

.. |bitarrayipython63_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-ipython63.png
   :width: 16

.. |bitarrayipython63| imagewrap:: _static/bitarray-complete-to-bytes-example-ipython63.png
   :width: 550

.. |bitarraypypy58_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-pypy58.png
   :width: 16

.. |bitarraypypy58| imagewrap:: _static/bitarray-complete-to-bytes-example-pypy58.png
   :width: 550

.. |bitarraypypy260_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-pypy260.png
   :width: 16

.. |bitarraypypy260| imagewrap:: _static/bitarray-complete-to-bytes-example-pypy260.png
   :width: 550

.. |bitarraypypy360_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-pypy360.png
   :width: 16

.. |bitarraypypy360| imagewrap:: _static/bitarray-complete-to-bytes-example-pypy360.png
   :width: 550

.. |bitarrayjython27_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-jython27.png
   :width: 16

.. |bitarrayjython27| imagewrap:: _static/bitarray-complete-to-bytes-example-jython27.png
   :width: 550

.. |bitarrayironpython27_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-ironpython27.png
   :width: 16

.. |bitarrayironpython27| imagewrap:: _static/bitarray-complete-to-bytes-example-ironpython27.png
   :width: 550

.. |bitarraycircuitpython30_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes-example-circuitpython30.png
   :width: 16

.. |bitarraycircuitpython30| imagewrap:: _static/bitarray-complete-to-bytes-example-circuitpython30.png
   :width: 550


.. |threevaluedatebasedversionnumbers_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-rte-distrel-3num-with-date.png
   :width: 16


.. |cythonintegration| imagewrap:: _static/cython-integration.png
   :width: 250

.. |cythonintegration_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/cython-integration.png
   :width: 16

.. |pi| raw:: html

   <code>|</code>
   