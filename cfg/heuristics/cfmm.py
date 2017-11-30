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
    
    #MP2RAGE

    t1 = create_key('sub-{subject}/anat/sub-{subject}_acq-MP2RAGE_T1w')
    t1map = create_key('sub-{subject}/anat/sub-{subject}_acq-MP2RAGE_T1map')
    t1inv1 = create_key('sub-{subject}/anat/sub-{subject}_inv-1_MP2RAGE')
    t1inv2 = create_key('sub-{subject}/anat/sub-{subject}_inv-2_MP2RAGE')
    t1uni = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_MP2RAGE')

    b1map = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1map_SA2RAGE')
    b1inv1 = create_key('sub-{subject}/fmap/sub-{subject}_inv-1_SA2RAGE')
    b1inv2 = create_key('sub-{subject}/fmap/sub-{subject}_inv-2_SA2RAGE')
    b1div = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1Div_SA2RAGE')

    t2 = create_key('sub-{subject}/anat/sub-{subject}_acq-tse2D_T2w')

    rest = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:01d}_bold')
    rest_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:01d}_sbref')

    rest_psf = create_key('sub-{subject}/func/sub-{subject}_acq-psf_task-rest_run-{item:01d}_bold')
    rest_psf_dico = create_key('sub-{subject}/func/sub-{subject}_acq-psf_task-rest_run-{item:01d}_rec-dico_bold')

    dwi_PA = create_key('sub-{subject}/dwi/sub-{subject}_acq-PA_dwi')
    dwi_PA_sbref = create_key('sub-{subject}/dwi/sub-{subject}_acq-PA_sbref')
    dwi_AP = create_key('sub-{subject}/dwi/sub-{subject}_acq-AP_dwi')
    dwi_AP_sbref = create_key('sub-{subject}/dwi/sub-{subject}_acq-AP_sbref')

    fmap_PA = create_key('sub-{subject}/fmap/sub-{subject}_acq-PA_epi')
    fmap_PA_sbref = create_key('sub-{subject}/fmap/sub-{subject}_acq-PA_sbref')
    fmap_diff = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    fmap_magnitude = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')

    #T2 SPACE
    spc_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-spc_T2w')

    #Time-of-flight Angio
    TOF_angio = create_key('sub-{subject}/anat/sub-{subject}_acq-TOF_angio')

    #MIPS
    DIS2D_TOF_SAG = create_key('sub-{subject}/anat/sub-{subject}_acq-TOFSAG_rec-DIS2D_mip')
    DIS2D_TOF_COR = create_key('sub-{subject}/anat/sub-{subject}_acq-TOFCOR_rec-DIS2D_mip')
    DIS2D_TOF_TRA = create_key('sub-{subject}/anat/sub-{subject}_acq-TOFTRA_rec-DIS2D_mip')

    #########################
    #### Multi-echo GRE #####
    #########################

    #Multi-echo GRE (Susc3D)
    mag_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-mag_echo_GRE')
    phase_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-phase_echo_GRE')

    DIS2D_mag_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-mag_rec-DIS2D_echo_GRE')
    DIS2D_phase_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-phase_rec-DIS2D_echo_GRE')
    DIS3D_mag_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-mag_rec-DIS3D_echo_GRE')
    DIS3D_phase_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-phase_rec-DIS3D_echo_GRE')

    #Derived T2 star - seem to only be calculated with DIS2D
    T2_star = create_key('sub-{subject}/anat/sub-{subject}_T2star')
    DIS2D_T2_star = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS2D_T2star')
    DIS3D_T2_star = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS3D_T2star')

    # MEMP2RAGE #
    me_t1     = create_key('sub-{subject}/anat/sub-{subject}_acq-MEMP2RAGE_T1w')
    me_t1map  = create_key('sub-{subject}/anat/sub-{subject}_acq-MEMP2RAGE_T1map')
    me_t1inv1 = create_key('sub-{subject}/anat/sub-{subject}_inv-1_MEMP2RAGE')
    me_t1inv2 = create_key('sub-{subject}/anat/sub-{subject}_inv-2_MEMP2RAGE')
    me_t1uni  = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_MEMP2RAGE')

    me_t1inv1_ce = create_key('sub-{subject}/anat/sub-{subject}_inv-1_rec-combEcho_acq-MEMP2RAGE')
    me_t1_ce     = create_key('sub-{subject}/anat/sub-{subject}_rec-combEcho_acq-MEMP2RAGE_T1w')
    me_t1inv2_ce = create_key('sub-{subject}/anat/sub-{subject}_inv-2_rec-combEcho_acq-MEMP2RAGE')
    me_t1uni_ce  = create_key('sub-{subject}/anat/sub-{subject}_rec-combEcho_acq-UNI_MEMP2RAGE')

    # DIR T2 #
    dir_t2       = create_key('sub-{subject}/anat/sub-{subject}_acq-DIR_T2w')
    DIS2D_dir_t2 = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS2D_acq-DIR_T2w')

    info = { t1:[],t1map:[],t1inv1:[],t1inv2:[],t1uni:[],
             b1map:[],b1inv1:[],b1inv2:[],b1div:[],
             t2:[],
             rest:[],rest_sbref:[],
             rest_psf:[],rest_psf_dico:[],
             dwi_PA:[],dwi_AP:[],dwi_PA_sbref:[],dwi_AP_sbref:[],
             fmap_PA:[],fmap_PA_sbref:[],fmap_diff:[],fmap_magnitude:[],
             me_t1:[],me_t1map:[],me_t1inv1:[],me_t1inv1:[],me_t1inv2:[],me_t1uni:[],
             me_t1inv1_ce:[],me_t1_ce:[],me_t1inv2_ce:[],me_t1uni_ce:[],
             dir_t2:[], DIS2D_dir_t2:[]}

    for idx, s in enumerate(seqinfo):

    #memp2rage
        if ('memp2rage' in s.protocol_name):
            if ('UNI-DEN' in (s.series_description).strip()):
                if ('combEcho' in (s.series_description).strip()):
                    info[me_t1_ce].append({'item': s.series_id})
                else:
                    info[me_t1].append({'item': s.series_id})
            if ('INV1' in (s.series_description).strip()):
                if ('combEcho' in (s.series_description).strip()):
                    info[me_t1inv1_ce].append({'item': s.series_id})
                else:
                    info[me_t1inv1].append({'item': s.series_id})
            if ('INV2' in (s.series_description).strip()):
                if ('combEcho' in (s.series_description).strip()):
                    info[me_t1inv2_ce].append({'item': s.series_id})
                else:
                    info[me_t1inv2].append({'item': s.series_id})
            if ('UNI_Images' in (s.series_description).strip()):
                if ('combEcho' in (s.series_description).strip()):
                    info[me_t1uni_ce].append({'item': s.series_id})
                else:
                    info[me_t1uni].append({'item': s.series_id})
            if ('T1_Images' in (s.series_description).strip()):
                info[me_t1map].append({'item': s.series_id})
    #mp2rage
        elif ('mp2rage' in s.protocol_name):
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

    #dir t2
    #note: for all distortion corrected data, no protocol name due to post-scan processing
    #      therfore, s.series_description is used instead
        if ('spc_dir' in (s.series_description).strip()):
            if ('DIS2D' in (s.series_description).strip()):
                info[DIS2D_dir_t2].append({'item': s.series_id})
            else:
                info[dir_t2].append({'item': s.series_id})
 
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
            if ('mbep2d' in (s.series_description).strip() and 'AP' in (s.series_description).strip()):
                if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[rest_sbref].append({'item': s.series_id})
                else:
                    info[rest].append({'item': s.series_id})
 
            if ('mi_ep2d' in (s.series_description).strip()):
                if ('DICO'  in (s.image_type[4].strip())):
                    info[rest_psf_dico].append({'item': s.series_id})
                else:
                    info[rest_psf].append({'item': s.series_id})
                    
            if ('PA' in (s.series_description).strip()):
                if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[fmap_PA_sbref].append({'item': s.series_id})
                else:
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
