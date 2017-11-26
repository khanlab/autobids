# autobids
Automated Dicom to BIDS and pipelines using compute canada


## Dependencies:

* dcm4che Singularity image
* neuroglia-helpers


## Install:


Env Variables:

AUTOBIDS_DIR=/home/akhanf/autobids
AUTOBIDS_DATA=/project/6007967/akhanf/cfmm-bids/data

Set-up config files:

## BUGS

Code in the POST-BIDS pipelines (bidsBatch) that is executed BEFORE job submission requires a participants.tsv file..
	-need to refactor this so that a launcher script (dependent on job completion) runs bidsBatch instead..
		-

