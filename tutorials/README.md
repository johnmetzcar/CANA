**CANALIZATION ANALYSIS FOR GENERIC BOOLEAN NETWORK**

=======================================================

This is a development effort to produce a generic pipeline for analysis of logical/Boolean networks using the CANA package, of which this is a fork. See main repository for additional information or README on landing page of this fork.

Currently work is focused on developing the notebook _Generic workflow for canalization of a Boolean network_. It requires additional custom code beyond the standard CANA package available via `pip` or the CANA Github repository [project page](https://github.com/rionbr/CANA). The custom data processing and visualization modules are currently contained in `cana/custom_modules` and as well as the PI3K network data sets from [Sizek et al](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006402), which currently do not ship with CANA. They can be directly accessed by doing a local installation of CANA. To install locally enter the following command entered into an active Python session from within the `CANA` directory:

```
    $ python setup.py develop
```

Note that currently this local install command for this custom code has only been shown to work in MacOS using the PyCharm IDE. Additional environments will be tested in an ongoing and as needed basis. (True as of 05.03.21)