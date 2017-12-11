# autobids
Automated Dicom to BIDS and pipelines using compute canada


## Dependencies:

* dcm4che Singularity image
* neuroglia-helpers


## Install:

Clone the autobids repository to your home directory:
```
git clone http://github.com/khanlab/autobids ~/autobids
```

Create a folder in your project space for your bids data:
```
mkdir -p ~/projects/rrg-akhanf/$USER/bids
```

Run the following to set-up your environment (re-login afterwards):
```
echo "export AUTOBIDS_DIR=~/autobids   #this repository" >> ~/.bashrc
echo "export AUTOBIDS_DATA=~/projects/rrg-akhanf/$USER/bids" >> ~/.bashrc
echo "export PATH=$AUTOBIDS_DIR/bin:$PATH" >> ~/.bashrc
```

## Config files:

If deploying to your own BIDS project directory, set-up config files:
```
cfg
├── dicom-retrieve.cfg	# dicom server info
├── heuristics	# heudiconv heuristic files, referred to from study_cfg
│   ├── snsx_7T.py
│   ├── topsy_7T.py
└── study		#study config files (example below)
    ├── Gati_TestProtocol.SC_Test
    ├── Khan_NeuroAnalytics.SNSX
    ├── MacDonald_VDSC.3T
    ├── MacDonald_VDSC.7T
    └── Palaniyappan_TOPSY
```


## Study Config Files:

A study config file defines a subject ID mapping, the heuristic file to use, and the pipelines to run for dicom conversion, bids tune-up, and post-processing. ** NEW: If it does not exist, a config file will automatically be generated when you run autobidsProcess, using the default study config file **


The name of the study config file is used to match up a incoming study tarball to a study.
The filename must thus be structured as:
```
<PI>_<STUDY>.<OPTIONAL_WILDCARD>
```
The contents of the study config file specifies the BIDS folder (BIDS_DIR), how to determine 
subject ID automatically from the PatientName tag (SUBJ_EXPR), how to convert to BIDS (HEURISTIC) 
and optionally what pipelines to automatically run (PRE_BIDS_PIPELINE, POST_BIDS_PIPELINE)
	
	
The OPTIONAL_WILDCARD is matched against the name of the incoming tarball to determine 

Example: 
```
#!/bin/bash

#BIDS_DIR is optional, if it is not included will default to:  $AUTOBIDS_DATA/{PI}/{STUDY_NAME}

BIDS_DIR=$AUTOBIDS_DATA/Palaniyappan/TOPSY_7T		

SUBJ_EXPR=*TOPSY_{subject}  	#search string for subject id within PatientName dicom tag
				# Note:  must include {subject}
	


HEURISTIC=$AUTOBIDS_DIR/cfg/heuristics/topsy_7T.py
PRE_BIDS_PIPELINE=$AUTOBIDS_DIR/pipelines/tuneup_bids
POST_BIDS_PIPELINE=$AUTOBIDS_DIR/pipelines/mriqc

EMAIL_NOTIFICATION=alik@robarts.ca
```

## Usage:


* Example 1: Retrieving a set of subjects from the dicom server, and batch convert to BIDS and pre-process

1. Create study config file (if not created)
2. Run getDicomTarballs to get tarballs from the dicom server
3. Run autobidsProcess on the tarballs to submit jobs that convert to BIDS and pre-process

Note: by default, tar files are moved to the `sourcedata` folder in the BIDS directory

e.g.:
```
getDicomTarballs 'Khan^NeuroAnalytics' '-' ~/projectdir/tarball_dir
autobidsProcess ~/projectdir/tarball_dir/*.tar
```

* Example 2: Re-process dicoms from an already imported scan, by using sourcedata tar files
```
autobidsProcess <YOUR_BIDS_DIR>/sourcedata/*.tar
```

* Example 3: Trigger processing for newly acquired scans (performs processing one by one)

e.g.: Running the following will retrieve all scans acquired today for all studies, then submit jobs to convert/process

`procNewScans `date +%Y%m%d`

e.g.: Or can run with a date string to retrieve a subset of scans, then submit jobs to convert/process

`procNewScans '20170815-`

Note: `procNewScans` uses a locking mechanism to ensure the script cannot be initiated when it is already running. This is to ensure no conflicts arise when using cron jobs to retrieve scans.

### getDicomTarballs:

Retrieves studies based on StudyDescription & Date.  If date not provided, all studies are downloaded
Uses credentials in ~/.uwo_credentials or prompts for username/password (username line 1, password line 2)
```
Usage: getDicomTarballs '<studydesc-search>' '<date-search>' '<output folder>'   <optional flags>
	Example (all scans on specific date): getDicomTarballs 'Khan*' '20170530' myfolder
	Example (all scans since date): getDicomTarballs 'Khan*' '20170530-' myfolder
	Example (all scans in date range): getDicomTarballs 'Khan^NeuroAnalytics' '20170530-20170827' myfolder
	Example (all scans in all dates): getDicomTarballs 'Khan*' '-' myfolder
```
Output tarballs are named as:
```
<PI>_<STUDY>_<DATE>_<PATIENT_NAME>_<INSTANCE_NUMBER>.<RANDOM_HASH>.tar
```
e.g.:
```
Khan_NeuroAnalytics_20171108_2017_11_08_SNSX_C023_1.AC168B21.tar
PI: Khan
STUDY: NeuroAnalytics
DATE: 20171108
PATIENT_NAME: 2017_11_08_SNSX_C023
INSTANCE_NUMBER: 1
RANDOM_HASH: AC168B21
```

