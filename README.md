###  Note: This version of autobids has been superceded by autobids-v2 -- If you are a Western CFMM user, please enroll your study at: https://autobids-uwo.ca

# autobids

## Description

Autobids is a platform for automated download, standardization and post-processing of neuroimaging data using the BIDS standard.

## Usage

### CFMM autobids

With this option, following an initial configuration and test conversion of your protocol, your dicom data from every scan will be automatically converted to BIDS minutes after acquisition, along with any additional standardized pre-processing you wish you apply, using Compute Canada resources. Data will then be transferred to any computer or server you control, using the Globus file transfer service. You will receive your BIDS data shortly after completing the scan along with an e-mail notification of the transfer.   Please contact Ali Khan (alik -at- robarts -dot- ca) to configure your study for CFMM autobids automated BIDS conversion and post-processing. 

* Note: To use this service, you must grant read access through the CFMM Dicom Server.  Data stored locally on the compute server will be unaccessible by other users, but will remain readable by Khan Lab system administrators. Any data will be deleted from the server upon request or at termination of the study. Statistics on how many subjects processed and compute times will be retained to evaluate the impact of this service, and to enable future requests of resources from Compute Canada. 

### DIY
Download the container(s) and use autobids on your own machine. Note that this does not perform automated conversion, but provides a set of command-line tools to download data from the server, and convert downloaded or existing data to BIDS.

 * Note: requires Singularity or Docker on your machine - [tunel](https://singularityhub.github.io/interface/) is a nice user interface for working with containers)


### For non-CFMM users
The downloading of data from a dicom server (`cfmm2tar`) is set-up specifically for users of the Centre for Functional and Metabolic Mapping (CFMM) 3T and 7T scanners, but could be adapted to other sites too, especially if the site is already using dcm4che as a dicom server.  The tool for BIDS conversion (`tar2bids`) is also mainly for Siemens scanners, with preconfigured heuristics, but these can also be easily customized. 


## Credits

Autobids is developed and maintained by Ali Khan and Yingli Lu, with crowd-sourced support for general CFMM heuristics from a number of users (including Olivia Stanley, Patrick Park, and others). 

We are grateful for the BIDS community and Chris Gorgolewski in particular for driving this initiative.  We are also grateful to the [heudiconv](https://github.com/nipy/heudiconv) developers, as this is the back-end that autobids employs.
