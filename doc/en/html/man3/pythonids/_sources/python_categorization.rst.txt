
.. _PYTHONCATEGORIZATION:

Implementation Versions
=======================
The type of the core *Python* syntax as defined for a specific release version of the *disttype* itself is
released by various Python distributions under the same *disttype*.
These comprise the reference implementation *CPython* [CPython]_ and various additional distributions, which are
in some cases less compliant to the reference.
The deviation of the core syntax is in any case related to some specific features only, in none of the cases essential.
The packed standard libraries anyhow vary in some cases considerably, thus require either ports of standard libraries,
or adapted code sections.

.. figure:: _static/pythonids-blueprint.png
   :figwidth: 1000
   :align: center
   :target: _static/pythonids-blueprint.png
   
   Figure: Python Infrastructure Services |figurepythonidsblueprint_zoom|

.. |figurepythonidsblueprint_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/pythonids-blueprint.png
   :width: 16

The distributions apply various different versioning schemes, as some follow the syntax scheme, while others introduce
completly independent schemes.
In case of the add-on packages as *IPython* and *Cython* the identification is even almost redundant on the first view.
The syntax versioning is defined by the PEP-440, in particular the numbering scheme for final releases [FINALRELEASE]_.
See also :ref:`Python syntax versions <PYTHONSYNTAXVERSIONS>`.

The complete information in order to decide the actual current Python variant thus comprises not only
the syntax version ':ref:`disttype <PYTHONSYNTAXVERSIONS>`',  

   .. parsed-literal::
   
      Python disttype:  (<major>, <minor>, <micro>)

but also the actual distribution including the release version.

   .. parsed-literal::

      Python:             <syntaxcategory==Python> <disttype>
      PythonDist:         <dist> <distrel>

While the version of the disttype fits into a 16-bit value, this is no longer the case for the complete
information.

The distribution information is in case of *CPython* basically the same as the syntax information related to the distribution,
the *distrel* and *disttype* are in particular literally the same information.
The syntax changes are reflected for the reference actually in the *major* and *minor* version numbers only,
while the *micro* version number reflects in some cases standard library changes.
The *category* of the syntax is constant for all - *category == Python*. 

Therefore the distribution information is designed as an extra bitmask of 32bit, 
containing the *major* and *minor* version numbers of the syntax information, 
the distribution identifier, and the release version of 
the distribution. 

   .. parsed-literal::

      <disttype-major><disttype-minor><dist><distrel>


.. _HIERARCHPYTHONCATEGORIES:

Hierarchy of Python Categories
------------------------------
The Python syntax versioning follows a well defined numbering scheme [PEP440]_, while the distribution
versioning is defined individually, thus resulting in non-conformance to each other,
even not *Cython*.

The resulting layout design covers the dependency of tree structures with branches relying on their
parent nodes.
This for example defines that a version of a Python distribution which is numbered incremental, defines a
syntax version where it is compatible, and eventually from where on it is compatible for coming releases.

.. figure:: _static/pythonids-category-hierarchy.png
   :figwidth: 700
   :align: center
   :target: _static/pythonids-category-hierarchy.png
   
   Figure: Implementations |figurepythonidscategoryhierarchy_zoom|

.. |figurepythonidscategoryhierarchy_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/pythonids-category-hierarchy.png
   :width: 16

The main advance of a versioning hierarchy which includes the versions of multiple layers is the inherent
support for comparison based on the inherently existing order.
Thus this allows for single integer operations for the immediate determination of compatibility issues and ranges.
The common traditional handling of arrays and identifiers requires a larger code-block and thus
requires to spend more CPU power on simple comparisons.

Number Ranges
^^^^^^^^^^^^^
The current maximum value ranges of the version numbers for the Python distributiopns are: 

   .. raw:: html
   
      <div class="centertab">
      <div class="featuretab">
   
   
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | dist          | distrel                  | distrel_major | distrel_minor | distrel_micro | reference        |
   +===============+==========================+===============+===============+===============+==================+
   | CircuitPython | Python-3                 | 3             | 0             | 3             | [CircuitPython]_ |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | CPython       | CPython-2.7, CPython-3.x | 3             | 7             | 15            | [CPython]_       |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | Cython        | Cython-0.x, Cython-3.x   | 3             | 29            | 4             | [Cython]_        |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | iPython       | iPython-2.7, iPython3.x  | 5             | 5             | 0             | [IPython]_       |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | IronPython    | IronPython-2.7           | 2             | 7             | 7             | [IronPython]_    |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | Jython        | Jython-2.7               | 2             | 7             | 1             | [Jython]_        |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | MicroPython   |                          |               |               |               | [MicroPython]_   |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   | PyPy          | PyPy-5.x                 | 5             | 10            | 0             | [PyPy]_          |
   +---------------+--------------------------+---------------+---------------+---------------+------------------+
   
   .. raw:: html
   
      </div>
      </div>

The resulting estimated required bitarraysizes are.

   .. raw:: html
   
      <div class="centertab">
      <div class="featuretab">
   
   +----------------+----------------+---------------+---------------+---------------+
   | disttype-major | disttype-minor | distrel_major | distrel_minor | distrel_micro |
   +================+================+===============+===============+===============+
   | 3-bits         | 5-bits         | 6-bits        | 6-bits        | 6-bits        |
   +----------------+----------------+---------------+---------------+---------------+
   
   .. raw:: html
   
      </div>
      </div>

.. _BITMASKLAYOUTDIST:

Bit Mask Layout
^^^^^^^^^^^^^^^
The following bit-mask encoding layout represents the platform IDs as part of the stack of
information systems identifiers.
The sizes of the bit groups are designed to be sufficient for all supported OS and distributions, which represent
various versioning philosophies and different weights on resulting numbering schemes and the number assignment
incrementation cycle periods.

.. figure:: _static/bitarray-principle-stack.png
   :figwidth: 450
   :align: center
   :target: _static/bitarray-principle-stack.png
   
   Figure: bit-mask encoding |bitarrayprinciplestack_zoom|

.. |bitarrayprinciplestack_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-principle-stack.png
   :width: 16


The visualized mapping scheme with the bit allocation within bytes is

.. figure:: _static/bitarray-principle-stack-bytes.png
   :figwidth: 450
   :align: center
   :target: _static/bitarray-principle-stack-bytes.png
   
   Figure: byte maping |bitarrayprinciplestackbytes_zoom|

.. |bitarrayprinciplestackbytes_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-principle-stack-bytes.png
   :width: 16

The bit boundaries are finally a compromise with the main design target to fit 
completely into a 32bit value.


The following table shows the available number ranges for the components of the bit array **pythonids.pythondist.PYDIST**.

   .. raw:: html
   
      <div class="centertab">
      <div class="featuretab">
   
   +----------------+-------+-------------+------------+----------------------+
   | bit-group      | width | number-type | max-values | preferred  operators |
   +================+=======+=============+============+======================+
   | category       | 1bit  | constant    | 1          |                      |
   +----------------+-------+-------------+------------+----------------------+
   | disttype-major | 3bit  | int         | 7          | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   | disttype-minor | 5bit  | int         | 31         | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   | dist           | 5bit  | int         | 31         | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   | distrel-major  | 6bit  | int         | 63         | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   | distrel-minor  | 6bit  | int         | 63         | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   | distrel-micro  | 6bit  | int         | 63         | < > ==               |
   +----------------+-------+-------------+------------+----------------------+
   
   .. raw:: html
   
      </div>
      </div>

.. note::

   Just to remind, the values are hierarchical, thus each range is a subset of its
   prefix-ranges and has to be permutated with all previous ranges.
   So also for the *distrel*, which is a specific sub-set of the *disttype*.


Performance of Comparison Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The provided standard information on the Python syntax and the specific variant by the distribution
releass is originally fragmented across several interfaces.
The data is presented by various parts with different data types. Some libraries provide a more condensed
set of data, but not comprising.
The data is in general not primarily intended for frequent access by high performance routines,
nor for shared modules with several system dependencies. 

The *pythomids* provide therefore the information as numeric values only in order to enable fast comparison and
range checks on all supported Python distributions.
The layout is still a compromise due to the huge amounts of distributions to be represented by a generic application.
But resulting of the design the measured access on the various platforms offers speed 
**improvements beginning by about 60%** with **frequently more than 300%** compared to the usage of the standard data.     
The numeric representation in addition provides simpler code by avoiding the implementation of specific caching
values.


The performance gain is e.g. in particular enhanced in comparison to interfaces like  *string.startswith()*,
which is directly applied to the standard string values.
The gain is here more than 60% compared on all supported platforms. 


.. _DISTNUMBERINGSCHEMES:

Distribution Numbering Scheme
-----------------------------
The complete bit array is describing a release of the specific distribution.
This contains the *distrel* bit field as the version of the distribution referenced by the *dist* field.
The *distrel* is represented as tuple of 3-value version number.
The *disttype* with *major* and *minor* version numbers is represented as a tuple of a 2-value version number.

.. _MAJORMINORVERSIONNUMBER:

Major and Minor
^^^^^^^^^^^^^^^
The *disttype* information contains here the reduced size by *major* and *minor* version numbers only.
This is due to the fact, that the distribution defines the syntax variant including the specific set
teh provided standard libraries.

.. figure:: _static/bitarray-major-minor.png
   :figwidth: 550
   :align: center
   :target: _static/bitarray-major-minor.png
   
   Figure: 2-value versions |bitarraymajorminor2_zoom|

.. |bitarraymajorminor2_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-major-minor.png
   :width: 16

.. _TREEVALUEVERSIONNUMBER:

Three-Value Number
^^^^^^^^^^^^^^^^^^
The distribution version numbers *distrel* are in most cases 3-value tuples. 
The value ranges vary upto 30 for *Cython*, thus the layout is designed for a value range of *0..63*.

.. figure:: _static/bitarray-3num-major-minor.png
   :figwidth: 630
   :align: center
   :target: _static/bitarray-3num-major-minor.png
   
   Figure: 3-value versions |bitarraymajorminor3_zoom|

.. |bitarraymajorminor3_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-3num-major-minor.png
   :width: 16

Combined Bitmask
^^^^^^^^^^^^^^^^

The combined bitmask is 

.. figure:: _static/bitarray-complete-to-bytes.png
   :figwidth: 680
   :align: center
   :target: _static/bitarray-complete-to-bytes.png
   
   Figure: basic scheme |bitarraycompletetobyte_zoom|

.. |bitarraycompletetobyte_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/bitarray-complete-to-bytes.png
   :width: 16

For application examples refer to the sections with the Python distributions, e.g. :ref:`CPython <enumCPYTHON>`


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
   