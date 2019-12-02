
.. _STANDARDOSDIST:

Supported Python Distributions
==============================


.. _PYTHON_SUPPORTED:

The current actively supported and tested Python distributions are:

   .. raw:: html
   
      <div class="indextab">
      <div class="centertab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   
   +------------+--------------+----------------+----------------+--------+------------------------------------+--------------------------------------+----------------------------------------+
   | category   | disttype     | dist           | tested distrel | status | doc                                | API                                                                           |
   +            +              +                +                +        +                                    +--------------------------------------+----------------------------------------+
   |            | syntaxtype   |                |                |        |                                    | syntax                               | distribution                           |
   +============+==============+================+================+========+====================================+======================================+========================================+
   | PYE_PYTHON | PYE_PYTHON27 | PYE_CPYTHON    | 2.7.*          | OK     | :ref:`CPython <enumCPYTHON>`       | :ref:`pythonids <PYTHONDISTIDSINIT>` | :ref:`pythonids.pydist <PYTHONPARAMS>` |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_IPYTHON    | 5.6.0          | OK     | :ref:`IPython <enumIPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_IRONPYTHON | 2.7.[79]       | OK     | :ref:`IronPython <enumIRONPYTHON>` |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_JYTHON     | 2.7.[01]       | OK     | :ref:`Jython <enumJYTHON>`         |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_PYPY       | 5.8.0          | OK     | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +              +                +----------------+--------+------------------------------------+                                      +                                        +
   |            |              |                | 6.0.0          | OK     | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +--------------+----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            | PYE_PYTHON35 | PYE_CPYTHON    | 3.5.[345]      | OK     | :ref:`CPython <enumCPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_IPYTHON    | 5.5.0          | OK     | :ref:`IPython <enumIPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_PYPY       | 5.10.1         | OK     | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_PYPY       | 6.0.0          |        | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_PYPY       | 7.0.0          |        | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +--------------+----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            | PYE_PYTHON36 | PYE_CPYTHON    | 3.6.[45]       | OK     | :ref:`CPython <enumCPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_IPYTHON    | 6.3.1          | OK     | :ref:`IPython <enumIPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_PYPY       | 7.0.0          |        | :ref:`PyPy <enumPYPY>`             |                                      |                                        |
   +            +--------------+----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            | PYE_PYTHON37 | PYE_CPYTHON    | 3.7.[012]      | OK     | :ref:`CPython <enumCPYTHON>`       |                                      |                                        |
   +            +              +----------------+----------------+--------+------------------------------------+                                      +                                        +
   |            |              | PYE_IPYTHON    | 6.5.0          | OK     | :ref:`IPython <enumIPYTHON>`       |                                      |                                        |
   +------------+--------------+----------------+----------------+--------+------------------------------------+--------------------------------------+----------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

.. _pythonids: package_init.html
.. _pythondist: pythonids.pythondist.html

.. _enumCPYTHON:

CPython
-------

   +----------+--------------------+----------+
   | type     | enum               | string   |
   +==========+====================+==========+
   | category | PYE_PYTHON         | posix    |
   +----------+--------------------+----------+
   | disttype | PYE_PYTHON27       | python27 |
   +----------+--------------------+----------+
   |          | PYE_PYTHON35       | python35 |
   +----------+--------------------+----------+
   |          | PYE_PYTHON36       | python36 |
   +----------+--------------------+----------+
   |          | PYE_PYTHON37       | python37 |
   +----------+--------------------+----------+
   | dist     | PYE_CPYTHON        | cpython  |
   +----------+--------------------+----------+
   | distrel  | see disttype       |          |
   +----------+--------------------+----------+
   | pretty   | PYE_CPYTHON_PRETTY | CPython  |
   +----------+--------------------+----------+


**Examples**:

The definition for **CPython-2.7.15**:

   .. parsed-literal::

      CPython-2.7.15
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON27  =  0x23800000
      PYE_CPYTHON   =  0x00040000
      (2, 7, 15)    =  0x000021cf
   
      PYDIST        =  0x238421cf
   
      PYDIST        =  0xa38421cf  # optional PYE_PYTHON, actually ignored


   |bitarraycpython2715|
   |bitarraycpython2715_zoom|


Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

The definition for **CPython-3.7.1**:

   .. parsed-literal::
 
      CPython-3.7.1
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON37  =  0x33800000
      PYE_CPYTHON   =  0x00040000
      (3, 7, 1)     =  0x000031c1
   
      PYDIST        =  0x338431c1
   
      PYDIST        =  0xb38431c1  # optional PYE_PYTHON, actually ignored


   |bitarraycpython371|
   |bitarraycpython371_zoom|
   
Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.
   
.. _enumIPYTHON:


IPython
-------

   +----------+----------------------+----------+
   | type     | enum                 | string   |
   +==========+======================+==========+
   | category | PYE_PYTHON           | posix    |
   +----------+----------------------+----------+
   | disttype | PYE_PYTHON27         | python27 |
   +----------+----------------------+----------+
   |          | PYE_PYTHON37         | python37 |
   +----------+----------------------+----------+
   | dist     | PYE_IPYTHON          | ipython  |
   +----------+----------------------+----------+
   | distrel  | distribution version |          |
   +----------+----------------------+----------+
   | pretty   | PYE_IPYTHON_PRETTY   | IPython  |
   +----------+----------------------+----------+

**Examples**:

The definition for **IPthon-5.6.0**:

   .. parsed-literal::
 
      IPython-5.6.0
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON27  =  0x23800000
      PYE_IPYTHON   =  0x00100000
      (5, 6, 0)     =  0x00005180
   
      PYDIST        =  0x23905180
   
      PYDIST        =  0xa3905180  # optional PYE_PYTHON, actually ignored
   
   
   |bitarrayipython56|
   |bitarrayipython56_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

The definition for **IPython-6.3.0**:

   .. parsed-literal::
 
      The definition for **IPython-6.3.0**:
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON37  =  0x33800000
      PYE_IPYTHON   =  0x00100000
      (6, 3, 0)     =  0x000060c0
   
      PYDIST        =  0x339060c0
   
      PYDIST        =  0xb39060c0  # optional PYE_PYTHON, actually ignored
   
   
   |bitarrayipython63|
   |bitarrayipython63_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

.. _enumPYPY:

PyPy
----

   +----------+----------------------+----------+
   | type     | enum                 | string   |
   +==========+======================+==========+
   | category | PYE_PYTHON           | posix    |
   +----------+----------------------+----------+
   | disttype | PYE_PYTHON27         | python27 |
   +----------+----------------------+----------+
   |          | PYE_PYTHON35         | python35 |
   +----------+----------------------+----------+
   | dist     | PYE_PYPY             | pypy     |
   +----------+----------------------+----------+
   | distrel  | distribution version |          |
   +----------+----------------------+----------+
   | pretty   | PYE_PYPY_PRETTY      | PyPy     |
   +----------+----------------------+----------+

**Examples**:

The definition for **PyPy-5.8.0**:

   .. parsed-literal::
    
      PyPy-5.8.0
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON27  =  0x23800000  # Python-2.7.13
      PYE_PYPY      =  0x00200000
      (5, 8, 0)     =  0x00005200
   
      PYDIST        =  0x23a05200
   
      PYDIST        =  0xa3905200  # optional PYE_PYTHON, actually ignored
   
   |bitarraypypy58|
   |bitarraypypy58_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

The definition for **PyPy2-6.0.0**:

   .. parsed-literal::
 
      PyPy2-6.0.0
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON27  =  0x23800000  # Python-2.7.13
      PYE_PYPY      =  0x00200000
      (6, 0, 0)     =  0x00006000
   
      PYDIST        =  0x23a06000
   
      PYDIST        =  0xa3a06000  # optional PYE_PYTHON, actually ignored
   
   |bitarraypypy260|
   |bitarraypypy260_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

The definition for **PyPy3-6.0.0**:

   .. parsed-literal::
 
      PyPy3-6.0.0
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON35  =  0x32800000  # Python-3.5.3
      PYE_PYPY      =  0x00200000
      (6, 0, 0)     =  0x00006000
   
      PYDIST        =  0x32a06000
   
      PYDIST        =  0xb2a06000  # optional PYE_PYTHON, actually ignored
   
   |bitarraypypy360|
   |bitarraypypy360_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

.. _enumJYTHON:

Jython
------

   +----------+----------------------+----------+
   | type     | enum                 | string   |
   +==========+======================+==========+
   | category | PYE_PYTHON           | posix    |
   +----------+----------------------+----------+
   | disttype | PYE_PYTHON27         | python27 |
   +----------+----------------------+----------+
   | dist     | PYE_JYTHON           | jython   |
   +----------+----------------------+----------+
   | distrel  | distribution version |          |
   +----------+----------------------+----------+
   | pretty   | PYE_JYTHON_PRETTY    | Jython   |
   +----------+----------------------+----------+

**Examples**:

The definition for **Jython-2.7.1**:

   .. parsed-literal::
 
      Jython-2.7.1
      
      PYE_PYTHON    =  0x80000000
      PYE_PYTHON27  =  0x23800000
      PYE_JYTHON    =  0x00180000
      (2, 7, 1)     =  0x000021c1
   
      PYDIST        =  0x239821c1
   
      PYDIST        =  0xa39821c1  # optional PYE_PYTHON, actually ignored
   
   
   |bitarrayjython27|
   |bitarrayjython27_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

.. _enumIRONPYTHON:

IronPython
----------

   +----------+-----------------------+------------+
   | type     | enum                  | string     |
   +==========+=======================+============+
   | category | PYE_PYTHON            | posix      |
   +----------+-----------------------+------------+
   | disttype | PYE_PYTHON27          | python27   |
   +----------+-----------------------+------------+
   | dist     | PYE_IRONPYTHON        | ironpython |
   +----------+-----------------------+------------+
   | distrel  | distribution version  |            |
   +----------+-----------------------+------------+
   | pretty   | PYE_IRONPYTHON_PRETTY | IronPython |
   +----------+-----------------------+------------+

**Examples**:

The definition for **IronPython-2.7.7**:

   .. parsed-literal::
 
      IronPython-2.7.7
      
      PYE_PYTHON      =  0x80000000
      PYE_PYTHON27    =  0x23800000
      PYE_IRONPYTHON  =  0x00140000
      (2, 7, 7)       =  0x000021c7
     
      PYDIST          =  0x239421c7
   
      PYDIST          =  0xa39421c7  # optional PYE_PYTHON, actually ignored
   
   
   |bitarrayironpython27|
   |bitarrayironpython27_zoom|

Color codes see :ref:`Numbering Schemes <DISTNUMBERINGSCHEMES>`.

MicroPython
-----------

.. note::

   coming soon


CircuitPython
-------------

.. note::

   coming soon



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


   
