
.. _PYTHONINTERPERSANDCOMPILERS:

Python Implementations
======================
Python is generally defined as an interpreted language with on-the-fly compiled p-code [PCODE]_ for
execution speed up. The p-code is executed in a language specific virtual machine - the p-code machine [PCODE]_ - as 
the runtime system.
The standard reference implementation is *CPython* based on *C*, which supports extension
modules by it's *C-Extension-API*.

.. figure:: _static/abstract-python-integration.png
   :figwidth: 250
   :align: center
   :target: _static/abstract-python-integration.png
   
   Figure: Structure |figureabstractpythonintegration_zoom|

.. |figureabstractpythonintegration_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/abstract-python-integration.png
   :width: 16

Other implementations exist, which utilize the *Java-VM* / *JVM* including just-in-time *JIT* compilation,
more traditional similarity by *IronPython* implemented in *C#* based on the *.NET-Framework*.

The interface for extensions could be applies by various APIs and wrappers.
While the native API requires some more in-depth use of the *C-Types* defined by *Python.h*, the others
provide for more or less additional abstraction of the API. 
The *ctypes* standard package provides a Python interface for calling shared library and DLL interfaces
by supporting elementary bindings for the exchanged parameters and data.  
The packages *CFFI* [CFFI]_ and *Cppyy* [CPPYY]_ provide specific bindings for Python, while
the extention Frameworks like *SWIG* provide a call wrapper for extensions written in different languages including C/C++.
The *Cython* implementation is here somewhat different, as it provides a native *Python* compiler which
preprocesses the *Python* code into *C* code  with optional *Cython* and *C* specific language extensions
of the *Python* syntax.

The relevance for the package *pythonids* is here the difference in the runtime view of the subsystems
from their current execution context.
While the modules of *pythonids* are executed by standard as an imported interpreted native *Python* module, the extensions
are executed within their target language execution context.
This has a defining impact on the implicit and/or explicit inspection support of the runtime code and though
the evaluation of the distribution parameters.

.. _DESCRCPYTHON:

CPython
-------
The *CPython* implementation is as one of the native standard target of the package *platformids*.
Therefore the runtime environment is identical in both code segments - the caller and the callee *platformids*.
Thus the *platformids* evaluates it's own runtime *Python* distribution correctly as the distribution executing
the caller function. 

The *CPYthon* runtime environment based on the Python-Virtual-Machine - PVM, which executes portable intermediate
code, the p-code [PCODE]_.

.. figure:: _static/cpython-integration.png
   :figwidth: 250
   :align: center
   :target: _static/cpython-integration.png
   
   Figure: Structure |figurecpythonintegration_zoom|

.. |figurecpythonintegration_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/cpython-integration.png
   :width: 16

The characterization data is represented by

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------------+----------------------------+-------------------------------------------------------+
   | attribute          | values                     | remarks                                               |
   +====================+============================+=======================================================+
   | category           | python                     |                                                       |
   +--------------------+----------------------------+-------------------------------------------------------+
   | disttype           | python<major0>.<minor0>    | the version of the Python syntax                      |
   +--------------------+----------------------------+-------------------------------------------------------+
   | dist               | cpython                    |                                                       |
   +--------------------+----------------------------+-------------------------------------------------------+
   | distrel            | <major0>.<minor0>.<build0> | in case of CPython the syntax release                 |
   +--------------------+----------------------------+-------------------------------------------------------+
   | hexrelease         | 0xb2......                 | the resulting hex encoding                            |
   +--------------------+----------------------------+-------------------------------------------------------+
   | compiler           | <C-Compiler>               | the used C compiler, e.g. GCC                         |
   +--------------------+----------------------------+-------------------------------------------------------+
   | compiler_version   | <major2>.<minor2>.<build2> | the release version of the C compiler                 |
   +--------------------+----------------------------+-------------------------------------------------------+
   | c_compiler         | <C-Compiler>               | in case of CPython the same as the *compiler*         |
   +--------------------+----------------------------+-------------------------------------------------------+
   | c_compiler_version | <major2>.<minor2>.<build2> | in case of CPython the same as the *compiler_version* |
   +--------------------+----------------------------+-------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

   
The  Execution Model
^^^^^^^^^^^^^^^^^^^^
The Python interpreter creates by default p-code [PCODE]_, which is the on-the-fly compiled source code
as abstract assembler code.
The compilation occurs only in case of an actual change, and only when the sources are present.
The p-code is than executed by a virtual processor, the Python-Virtual-Machine - the *PVM*.

The CPython implementation is hereby implemented itself by *C*, and provides an API for the direct inclusion of compiled
*C* and *C++* based code libraries, or others compliant to the call interface. 
The reverse call direction of Python call from a *C/C++* module is supported too.
See :ref:`CPython Extension Modules <CPYTHONEXTENTIONMODS>`.

The important point for *pythonids* is here the lack of dynamic Python binding information within the *C* based extensions 
for introspection.
The module *inspect* for example has no access to the provided symbols within the libraries, in particular when they 
are stripped off.
Therefore the Python implementation of *pyhtonids* can just detect that the caller is an extension module,
and with some heuristics that it is implemented in *C/C++* [ARTICLESTACKOFLOWCEXT]_, but not the type, neither the version.
Even though some solutions are possible, the current version of *pythonids* provides an inline module,
with either access to the extension data, or the hard-coded defition of the identifier and version at compile time. 

.. _CPYTHONEXTENTIONMODS:

CPython Extension Modules
^^^^^^^^^^^^^^^^^^^^^^^^^
For the compiled extension modules some special handling is required,
this is extracted into a specific package coming soon [extensionids]_.

The Data Aquisition
^^^^^^^^^^^^^^^^^^^
The aquisition of the modules implementation identifier data is collected and assembled by the *pythonids*, 
which is a module itself. 
In case the caller is implemented as native Python code, the execution environment is the same.
Things are different, when the caller is implemented within an extentsion module implemented e.g. in *C/C++*,
see :ref:`CPython Extension Modules <CPYTHONEXTENTIONMODS>`.

.. _DESCRIPYTHON:

IPython
-------
The *IPython* implementation basically extends the standard *CPython* implementation with
interactive features, standalone and embeddable, with an additional GUI based console.
*IPython* could be simply installed as an add-on [IPython]_ via *PyPI* [PyPI]_.
Thus *IPython* is basically not an separate implementation, but it changes the interactive behaviour of the
standard implementation including related output features.
This requires in some cases the separate detection, thus it is included as a separate implementation.

.. note::

   See Wikipedia - [IPython]_.

   IPython (Interactive Python) is a command shell for interactive computing in multiple programming languages, 
   originally developed for the Python programming language, that offers introspection, rich media, shell syntax,
   tab completion, and history. IPython provides the following features:

   * Interactive shells (terminal and Qt-based).
   * A browser-based notebook interface with support for code, text, mathematical expressions, inline plots and other media.
   * Support for interactive data visualization and use of GUI toolkits.
   * Flexible, embeddable interpreters to load into one's own projects.
   * Tools for parallel computing.

The characterization data is basically the same as for *CPython* represented by

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------------+----------------------------+-------------------------------------------------------+
   | attribute          | values                     | remarks                                               |
   +====================+============================+=======================================================+
   | category           | python                     |                                                       |
   +--------------------+----------------------------+-------------------------------------------------------+
   | disttype           | python<major0>.<minor0>    | the version of the Python syntax                      |
   +--------------------+----------------------------+-------------------------------------------------------+
   | dist               | cpython                    |                                                       |
   +--------------------+----------------------------+-------------------------------------------------------+
   | distrel            | <major0>.<minor0>.<build0> | in case of CPython the syntax release                 |
   +--------------------+----------------------------+-------------------------------------------------------+
   | hexrelease         | 0xb2......                 | the resulting hex encoding                            |
   +--------------------+----------------------------+-------------------------------------------------------+
   | compiler           | <C-Compiler>               | the used C compiler, e.g. GCC                         |
   +--------------------+----------------------------+-------------------------------------------------------+
   | compiler_version   | <major2>.<minor2>.<build2> | the release version of the C compiler                 |
   +--------------------+----------------------------+-------------------------------------------------------+
   | c_compiler         | <C-Compiler>               | in case of CPython the same as the *compiler*         |
   +--------------------+----------------------------+-------------------------------------------------------+
   | c_compiler_version | <major2>.<minor2>.<build2> | in case of CPython the same as the *compiler_version* |
   +--------------------+----------------------------+-------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>
    
.. _DESCRIRONPYTHON:

IronPython
----------
The *IronPython* implementation is different from the standard C based interpreter distributions.
The *IronPython* package uses the *.NET* as the runtime virtual machine and integrates into the 
supported languages, so *C#*.


.. figure:: _static/dotnet-integration.png
   :figwidth: 250
   :align: center
   :target: _static/dotnet-integration.png
   
   Figure: Structure |figureironpythonintegration_zoom|

.. |figureironpythonintegration_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/dotnet-integration.png
   :width: 16

The characterization data is represented by

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------------+-------------------------------------+-------------------------------------------------------+
   | attribute          | values                              | remarks                                               |
   +====================+=====================================+=======================================================+
   | category           | python                              |                                                       |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | disttype           | python<major0>.<minor0>             | the version of the Python syntax                      |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | dist               | ironpython                          |                                                       |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | distrel            | <major0>.<minor0>.<build0>          | in case of CPython the syntax release                 |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | hexrelease         | 0xb2......                          | the resulting hex encoding                            |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | compiler           | .NET                                | the used C compiler                                   |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | compiler_version   | <major2>.<minor2>.<micro2>.<build2> | the release version .NET compiler                     |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | c_compiler         | n.a.                                |                                                       |
   +--------------------+-------------------------------------+-------------------------------------------------------+
   | c_compiler_version | n.a.                                |                                                       |
   +--------------------+-------------------------------------+-------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

The  Execution Model
^^^^^^^^^^^^^^^^^^^^
will be completed soon

The Data Aquisition
^^^^^^^^^^^^^^^^^^^

The access interface to the information about the implementation is the same as for the reference 
implementation *CPython*.  

.. _DESCRJYTHON:

Jython
------
The *Jython* implementation is different from the standard C based interpreter distributions.
The *Jython* package uses the *JVM* as the runtime virtual machine and integrates into *Java*.

.. note::

   See Wikipedia - [Jython]_.

   Jython is an implementation of the Python programming language designed to run on the Java platform. 
   It is the successor of JPython.[3] 


.. figure:: _static/java-integration.png
   :figwidth: 250
   :align: center
   :target: _static/java-integration.png
   
   Figure: Structure |figurejythonintegration_zoom|

.. |figurejythonintegration_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/java-integration.png
   :width: 16

The characterization data is represented by the following table.
The special case is here, that the compiler is Java, but the underlying compiler
is - intentional - not known.

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | attribute          | values                              | remarks                                                                      |
   +====================+=====================================+==============================================================================+
   | category           | python                              |                                                                              |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | disttype           | python<major0>.<minor0>             | the version of the Python syntax                                             |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | dist               | jython                              |                                                                              |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | distrel            | <major1>.<minor1>.<build1>          | the release of the Jython implementation                                     |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | hexrelease         | 0xb2......                          | the resulting hex encoding                                                   |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | compiler           | java                                | also relevant for the frequently applied cross-calls between Jyhton and Java |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | compiler_version   | <major0>.<minor0>.<micro0>.<build0> | the special numbering of Java: *1.8.0_181* == *8u181*                        |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | c_compiler         | n.a.                                | this information is not available                                            |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   | c_compiler_version | n.a.                                |                                                                              |
   +--------------------+-------------------------------------+------------------------------------------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

The significant difference for the user of the *pythonids* is in case of the *Jython* distribution the introduction
of the type *long* for unsigned 32bit integers by the *Jython* compiler.
The *pythonids* uses 32bit values as unsigned integers for bitmaks.
Thus e.g. a type comparison of the of the *category* or *hexrelease* requires the *long* type.

   .. parsed-literal::

      #
      # CPython, etc.
      #
      if type(other) is int:
         proceed_int()
   
      #
      # Jython
      #
      else:
         try:
            # jython - 32bit is a long(unsigned int)
            if isinstance(other, long):  # @UndefinedVariable
               proceed_long()
   
         except NameError:
            pass

Just other differences occurs between the various Java releases, which have an impact at least in some specific developement tasks.
The *Jython* implementation relies closely on the actual JVM, thus provides support for the interfaces it could rely on itself.
E.g. one difference between *OpenJDK* for the version *2.7.0* and the *Java* distribution of *Oracle* for the version *2.7.1* is the
absence of the interface *sys.getNativePlatform()* for the former.
This is the *Jython* specific interface for the enumeration of the underlying *disttype*, e.g. as '*linux2*'. 

The basic native runtime environment data is handled by *Jython* commonly in a special way based on the philosophy 
of platform abstraction of *Java*.
While the implementation data of the runtime information for *Java* itself is still available,
the access to the native data is encapsulated.
This is in particular expressed by the attribte *os.name*, which is set to '*java*', whereas
the attribute '*os._uname*' is introduced in adddition, which covers the native platform as expected.
For further details see [platformids]_. 


The  Execution Model
^^^^^^^^^^^^^^^^^^^^
The *Jython* distribution uses internally the *JVM* of the *Java* runtime environmetns.
Therefore the *Python* code is translated into the *p-code* of *Java* and integrated into the complete
set of the *Java* runtime libraries, including the user interface.

.. note::

   See Wikipedia - [Jython]_.

   Jython programs can import and use any Java class. Except for some standard modules, 
   Jython programs use Java classes instead of Python modules. 
   Jython includes almost all of the modules in the standard Python programming language distribution, 
   lacking only some of the modules implemented originally in C. 
   For example, a user interface in Jython could be written with Swing, AWT or SWT. 
   Jython compiles to Java bytecode (intermediate language) either on demand or statically.

Thus the integration supports simplified access to *Java* based standard and custom packages including applications.
The access to other programming languages and the native platform particularly based on *C/C++* is still
available via the *Java Native Interface* - *JNI*, 
or the derived packages by the community project *Java Native Access* - *JNA*.
For some further details refer to [platformids]_.
 
The Data Aquisition
^^^^^^^^^^^^^^^^^^^
The implementation data of the distribution is available by common portable Python interface,
while the optional compiler data is here the current *Java* engine, 
e.g. based on "*java1.7.0_65*" or "*java1.8.0_181*"

The naming and release version numbering scheme is changed by the manufacturer beginning with the preriod of 
releases of *java8* to *java12*, which in particular includes chnages in licensing. 
The new categrization based on the license changes provided by the manufacturer inludes the naming *jre* / *jdk* and
now *openjdk* by the manufacturer.
This includes in particular the update and clearing of the redundant numbering scheme.
The old version numbering scheme contained the major version *1* and the micro version *0*,  
which are constants for all previous versions:

   .. parsed-literal::
   
      java8: jre1.8.0_202 or jre8u202
       
      java9: jre1.9.0_181 or jre9u181

This is changed now e.g. to:

   .. parsed-literal::
   
      java11: commercial license: jre-11.0.2 + jre-11.0.2
              more open license:  openjdk-11.0.2
      
      java12: commercial license: jre-12.0.0 + jre-12.0.0
              more open license:  openjdk-12.0.0  

.. _DESCRPYPY:

PyPy
----
The *PyPy* distribution is based on a *JIT* compiler written in *Python* itself. 

.. note::

   See Wikipedia - [PyPy]_.
   
   PyPy is an alternative implementation of the Python programming language[2] to CPython, 
   which is the standard implementation of Python. PyPy often runs faster than CPython, 
   because PyPy is a just-in-time compiler, while CPython is an interpreter. 
   Most Python code runs well on PyPy, except for code that depends on CPython extensions, 
   which either does not work or incurs some overhead when run in PyPy. Functionally, 
   PyPy is designed around the technique known as meta-tracing, which transforms an interpreter
   into a tracing just-in-time compiler. Since interpreters are usually easier to write than compilers, 
   but run slower, this technique can make it easier to produce efficient implementations of programming languages. 
   PyPy's meta-tracing toolchain is called RPython. 


The characterization data is represented by

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------------+----------------------------+-------------------------------------------------------------------+
   | attribute          | values                     | remarks                                                           |
   +====================+============================+===================================================================+
   | category           | python                     |                                                                   |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | disttype           | python<major0>.<minor0>    | the version of the Python syntax                                  |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | dist               | pypy                       |                                                                   |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | distrel            | <major1>.<minor1>.<build1> | the release of the PyPy implementation                            |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | hexrelease         | 0xb2......                 | the resulting hex encoding                                        |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | compiler           | python                     | in case of PyPy the CPython                                       |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | compiler_version   | <major0>.<minor0>.<build0> | in case of PyPy the release version of the used CPython           |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | c_compiler         | <C-Compiler>               | in case of PyP the C compiler used for *CPython* and by *RPython* |
   +--------------------+----------------------------+-------------------------------------------------------------------+
   | c_compiler_version | <major2>.<minor2>.<build2> | release of the C compiler                                         |
   +--------------------+----------------------------+-------------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

The  Execution Model
^^^^^^^^^^^^^^^^^^^^

The *PyPy* is written in *RPython*. 

.. note::

   See Wikipedia - [PyPy]_.
   
   The PyPy interpreter itself is written in a restricted subset of Python, 
   called RPython (Restricted Python).[5] RPython puts some constraints on the 
   Python language such that a variable's type can be inferred at compile time.[6]

   The PyPy project has developed a toolchain that analyzes RPython code and translates
   it into a form of byte code, together with a interpreter written in the C programming language. 
   Much of this code is then compiled into machine code; and the byte code runs on the compiled interpreter.

   It allows for pluggable garbage collectors, as well as optionally enabling Stackless Python features. 
   Finally, it includes a just-in-time (JIT) generator that builds a just-in-time compiler into the interpreter, 
   given a few annotations in the interpreter source code. The generated JIT compiler is a tracing JIT.[7]

   RPython is now also used to write non-Python language implementations such as Pixie.[8]

   PyPy is compatible with CPython 2.7.13.[9] PyPy3, released starting with version 2.3.1,[10] is 
   compatible with CPython 3.5.3.[9] 
   Both versions have JIT compilation support on 32-bit/64-bit x86 and ARM processors.[11] 
   It is tested nightly on Windows, Linux, OpenBSD and Mac OS X. PyPy is able to run pure Python software 
   that does not rely on implementation-specific features.[12]

See also :ref:`HPC with Python <HPCWITHPYTHON>`.


PyPy Extension Modules
^^^^^^^^^^^^^^^^^^^^^^
The interface for extensions depends on the applied interface, for an overview 
refer to :ref:`HPC with Python <HPCWITHPYTHON>`.
For an investigation and overview of alternatives by *Cling* refer to [HPCPYPYCLING]_.


.. note::

   See Wikipedia - [PyPy]_.
   
   There is a compatibility layer for CPython C API extensions called CPyExt, but it is incomplete and experimental. 
   The preferred way of interfacing with C shared libraries is through the built-in CFFI or ctypes libraries.

For the compiled extension modules some special handling is required,
this is extracted into a specific package coming soon [extensionids]_.

The Data Aquisition
^^^^^^^^^^^^^^^^^^^
The data aquisition is compatible to the standard *CPython*, including the optional compiler parameters
with a few deviation of the matched strings. 


.. _HPCWITHPYTHON:

HPC with Python
---------------
The implementation of high-performance applications based on Python requires in practical cases the integration of
native *C/C++* modules, and/or compiled *Python* code like provided.

   .. raw:: html
   
      <div class="centertab">
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">
   
   
   +---------------+---------+-----------+
   | type          | project | reference |
   +===============+=========+===========+
   | native        | ctypes  | [CTYPES]_ |
   +---------------+---------+-----------+
   | native        | SWIG    | [SWIG]_   |
   +---------------+---------+-----------+
   | native        | CFFI    | [CFFI]_   |
   +---------------+---------+-----------+
   | native        | Cling   | [CPPYY]_  |
   +---------------+---------+-----------+
   | Python + ext. | CPython | [Cython]_ |
   +---------------+---------+-----------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

 
.. note::

   See Wikipedia - [PyPy]_.
   
   There is a compatibility layer for CPython C API extensions called CPyExt, but it is incomplete and experimental. 
   The preferred way of interfacing with C shared libraries is through the built-in CFFI or ctypes libraries.

The compiled extension modules are supported by the package *extensionids* coming soon [extensionids]_.
For an investigation and overview of alternatives by *Cling* refer to [HPCPYPYCLING]_,
for a comparison of "Performance of Python runtimes on a non-numeric scientific code" refer to [PYIMPPERFORM]_.


Native Python as Virtual OS
---------------------------
Some special *Python* distributions are supported for small embedded systems with limited resources.
The distributions *MicroPython* [MicroPython]_ and ithe derived *CircuitPython* [CircuitPython]_ provide a 
literally native *Python* environment,
where the interpreter itself is the only and one execution environemnt which is executed as a virtual OS.
The interactive command line user interface of the *Python* interpreter is hereby similar to a
common *shell* [SHELL]_ replacing the text based dialogue console [SHELLTXT]_.
Thus these *Python* implementations of this type represent the complete process execution frame including
the lower OS platform as described by *platformids*, and  *machineids*. 

.. _FIGURE_NATIVEINTEGRATEDSHELL:

.. figure:: _static/systems-ids-native-shell.png
   :figwidth: 550
   :align: center
   :target: _static/systems-ids-native-shell.png
   
   Figure: Integrated Native Shell |figuresystemabstractprint_zoom|

.. |figuresystemabstractprint_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/systems-ids-native-shell.png
   :width: 16

The native *Python* interpreter includes the required low-level drivers and provides 
basically a Firmware [FIRMWARE]_ stack including the compelete high-level execution frame.
The targeted devices are small SOC such as the original MicroPython [MicroPython]_ board

.. figure:: _static/micropython-device.png
   :figwidth: 200
   :align: center
   :target: https://micropython.org/
   
   Figure: MicroPython Device |micropythondevice_zoom|

.. |micropythondevice_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/micropython-device.png
   :width: 16

or the boards supported by *CircuitPython* [CircuitPython]_

.. figure:: _static/circuitpython-device.png
   :figwidth: 300
   :align: center
   :target: https://circuitpython.org/
   
   Figure: CircuitPython Device |circuitpythondevices_zoom|

.. |circuitpythondevices_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/circuitpython-device.png
   :width: 16

For differences between *CPython* and *MicroPython* see [MicroVsCPython]_.

.. note::

   The current version of *pythonids* does not yet support these implementations.

.. _embeddedMICROPY:

MicroPython
^^^^^^^^^^^
The Python variant *MicroPython* [MicroPython]_ is targeting small devices with limited resources of 
in particular small CPUs and memory and storage limited to some kB. 
*MicroPython* represents on those devices the interactive Python interface as the user interface in
complete replacement of a shell.
This provides the inetractive communication as well as the automated batch execution of Python programs
or small scripts.

The resources on these devices are extremely limited in comparison to the PC based platforms including 
their physically shrinked embedded variants.
Therefore the runtime environment is to be customized by specific custom modules and build options.
The *platformids* provides custom plugins with standard interfaces for the identification of the runtime environment.
 
*available soon*

.. _embeddedCIRCUITPY:

CircuitPython
^^^^^^^^^^^^^
The Python variant *CircuitPython* [CircuitPython]_ is a specialized variant provided by the
company Adafruit Industries Inc. [ADAFRUIT]_ customized for it's small devices.  

*available soon*

