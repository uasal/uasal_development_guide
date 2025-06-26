=============================
General Development Guide
=============================

This guide applies generally to all UASAL development but should be followed for any critical software.
  
=============================
=============================
Definition of criticality: 
=============================
=============================

Herein criticality is defined as an essential functionality for the safety or minimum operation of an instrument. 

**This guide is not intended for human safety software and if any life or facility safety functionality is required additional guidance should be sought.**

Either modeling of critical functionality of a simulation or critical function for an instrument.

=================
=================
Code Reviews
=================
=================

For any critical code required for essential functionality, updates should be reviewed following the [Google Code Review Guidelines](https://google.github.io/eng-practices/review/reviewer/). A fork of those guidelines is available in the UASAL organization (https://github.com/uasal/eng-practices).
                                                                                                                                     

=======================
=======================
Release documentation
=======================
=======================
 in the Forge environment and within the code itself, release notes on what was changed, by whom, and the reviewers shall be captured.


=======================
=======================
Test Case Documentation 
=======================
=======================
Test Case Documentation – for embedded software and firmware, test cases shall be defined as part of the verification and validation process. Code under test shall be version controlled as well as input test products. Code reviewer shall review test cases to ensure that the inputs are a) appropriate for the various test cases and b) have defined expected responses/outputs that can be archived. Test documentation shall include: version of code under test, version of inputs to code, test environment – bench top, emulator, etc, date of test performed, and who performed the test, along with the test results.                                                                                                        
                                                                                                                                     
=================
=================
Git Flow
=================
=================
