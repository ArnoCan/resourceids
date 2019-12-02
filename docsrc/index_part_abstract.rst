
********
Abstract
********

Modern landscapes of information infrastructures are commonly designed 
and organized as stacks of runtime service environments.
The technical architecture of the service stacks consists of a wide range of
heterogenous landscapes of components frequently requiring adaptation and mediation.


.. figure:: _static/systems-ids.png
   :figwidth: 400
   :align: center
   :target: _static/systems-ids.png
   
   Figure: Infrastructure Service Layers |figuresystemabstractprint_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |figuresystemabstractprint_zoom| imagewrap:: _static/zoom.png
   :alt: zoom 
   :target: _static/systems-ids.png
   :width: 16

This requires commonly the integration by wrappers and add-on coding with diverse languages and their specific releases,
thus in case of *Python*  the distinction of the :ref:`Python syntax versions <PYTHONSYNTAXVERSIONS>` with their specific
sets of standard runtime library variants as well as the `Python implementation <python_categorization.html#>`_ releases.
The *pythonids* provides the automated technical detection and enumeration
of the `runtime process framework layer of Python environments <python_categorization.html#>`_.

The provided information identifies the

* **Python Syntax**: 

   :ref:`16-bit hex-value of the Python syntax version <PYTHONSYNTAXVERSIONS>`

* **Python Interpreter and Compiler Distribution**: 

   :ref:`32-bit hierarchical hex-value of the derived distribution of the Python implementation variant <PYTHONCATEGORIZATION>`
   including the major and minor Python syntax version



The package '*pythonids*' is part of the set of packages of enumerations for efficient and fast operations of
code variants for software and infrastructure stacks. 
For other stack layers refer to [machineids]_, [platformids]_, [resourceids]_, and [extensionids]_.

