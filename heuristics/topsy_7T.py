import os

def create_key(template, outtype=('nii.gz'), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return (template, outtype, annotation_classes)

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    t1 = create_key('sub-{subject}/anat/sub-{subject}_acq-MP2RAGE_T1w')
    t1map = create_key('sub-{subject}/anat/sub-{subject}_acq-MP2RAGE_T1map')
    t1inv1 = create_key('sub-{subject}/anat/sub-{subject}_acq-inv1_MP2RAGE')
    t1inv2 = create_key('sub-{subject}/anat/sub-{subject}_acq-inv2_MP2RAGE')
    t1uni = create_key('sub-{subject}/anat/sub-{subject}_acq-uni_MP2RAGE')

    b1map = create_key('sub-{subject}/anat/sub-{subject}_acq-Sa2RAGE_B1map')
    b1inv1 = create_key('sub-{subject}/anat/sub-{subject}_acq-inv1_Sa2RAGE')
    b1inv2 = create_key('sub-{subject}/anat/sub-{subject}_acq-inv2_Sa2RAGE')
    b1div = create_key('sub-{subject}/anat/sub-{subject}_acq-b1Div_Sa2RAGE')

    t2 = create_key('sub-{subject}/anat/sub-{subject}_acq-tse2D_T2w')
    rest = create_key('sub-{subject}/func/sub-{subject}_task-rest_bold')
    rest_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_sbref')
    dwi_PA = create_key('sub-{subject}/dwi/sub-{subject}_acq-PA_dwi')
    dwi_PA_sbref = create_key('sub-{subject}/dwi/sub-{subject}_acq-PA_sbref')
    dwi_AP = create_key('sub-{subject}/dwi/sub-{subject}_acq-AP_dwi')
    dwi_AP_sbref = create_key('sub-{subject}/dwi/sub-{subject}_acq-AP_sbref')
    fmap_PA = create_key('sub-{subject}/fmap/sub-{subject}_acq-PA_epi')
    fmap_diff = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    fmap_magnitude = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')

    info = {t1:[],t1map:[],t1inv1:[],t1inv2:[],t1uni:[],
		b1map:[],b1inv1:[],b1inv2:[],b1div:[],
		t2:[],rest:[],rest_sbref:[],
		dwi_PA:[],dwi_AP:[],dwi_PA_sbref:[],dwi_AP_sbref:[],
		fmap_PA:[],fmap_diff:[],fmap_magnitude:[]}

    for idx, s in enumerate(seqinfo):
        #mp2rage
        if  ('mp2rage' in s.protocol_name):
            if ('UNI-DEN' in (s.series_description).strip()):
                info[t1].append({'item': s.series_id})
	    if ('T1_Images' in (s.series_description).strip()):
                info[t1map].append({'item': s.series_id})
	    if ('INV1' in (s.series_description).strip()):
                info[t1inv1].append({'item': s.series_id})
	    if ('INV2' in (s.series_description).strip()):
                info[t1inv2].append({'item': s.series_id})
	    if ('UNI_Images' in (s.series_description).strip()):
                info[t1uni].append({'item': s.series_id})

	#sa2rage
        if  ('sa2rage' in s.protocol_name):
            if ('invContrast1' in (s.series_description).strip()):
                info[b1inv1].append({'item': s.series_id})
            if ('invContrast2' in (s.series_description).strip()):
                info[b1inv2].append({'item': s.series_id})
            if ('b1DivImg' in (s.series_description).strip()):
                info[b1div].append({'item': s.series_id})
            if ('OTHER' in (s.image_type[2].strip())):
                info[b1map].append({'item': s.series_id})

	#t2 tse
        if  ('t2_tse' in s.protocol_name):
                info[t2].append({'item': s.series_id})

	    
        #rs func (incl opp phase enc)
        if ('bold' in s.protocol_name):
            if (s.dim4 >1 and 'AP_rs' in (s.series_description).strip()):
                info[rest].append({'item': s.series_id})
            if (s.dim4 ==1 and 'AP_rs' in (s.series_description).strip() and 'SBRef' in (s.series_description).strip() ):
		info[rest_sbref].append({'item': s.series_id})
            if (s.dim4 ==1 and 'PA' in (s.series_description).strip() and 'ND' in s.image_type[3].strip()):
		info[fmap_PA].append({'item': s.series_id})

	#gre field map   
        if ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})

        #dwi
        if ('diff' in s.protocol_name):
            if ( s.dim4 > 1 and ('mbep2d_diff_b1000_AP' == (s.series_description).strip()) ) :
                info[dwi_AP].append({'item': s.series_id})
            if ( s.dim4 > 1 and ('mbep2d_diff_b1000_PA' == (s.series_description).strip()) ):
                info[dwi_PA].append({'item': s.series_id})
            if ( s.dim4 == 1 and ('mbep2d_diff_b1000_AP' in (s.series_description).strip()) and 'SBRef' in (s.series_description).strip() ) :
                info[dwi_AP_sbref].append({'item': s.series_id})
            if ( s.dim4 == 1 and ('mbep2d_diff_b1000_PA' in (s.series_description).strip()) and 'SBRef' in (s.series_description).strip() ) :
                info[dwi_PA_sbref].append({'item': s.series_id})

            

   
    return info
