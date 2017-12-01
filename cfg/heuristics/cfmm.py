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

    #Compatible with:
    # (D): DIS2D/DIS3D reconstruction incl
    # (#): multiples runs as run-#

    # MP2RAGE (D)
    # Sa2RAGE (D)
    # MEMP2RAGE 
    # T2 TSE (D,#)
    # multiband BOLD (#)
    # psf-dico BOLD (#)
    # diffusion (#)
    # EPI-PA field mapping
    # GRE field mapping
    # T2 SPACE (D)
    # TOF Angio (D)
    # ME GRE/susc  (D)
    # DIR T2 (D)

    #to do: 
        # add (D) for MEMP2RAGE


    #MP2RAGE

    inv1_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-1_MP2RAGE')
    inv2_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-2_MP2RAGE')
    t1map = create_key('sub-{subject}/anat/sub-{subject}_T1map')
    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    uni_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_MP2RAGE')

        #Dist. corrected versions:
    DIS3D_inv1_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-1_rec-DIS3D_MP2RAGE')
    DIS3D_inv2_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-2_rec-DIS3D_MP2RAGE')
    DIS3D_t1map = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS3D_T1map')
    DIS3D_t1w = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS3D_T1w')
    DIS3D_uni_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_rec-DIS3D_MP2RAGE')

    DIS2D_inv1_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-1_rec-DIS2D_MP2RAGE')
    DIS2D_inv2_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-2_rec-DIS2D_MP2RAGE')
    DIS2D_t1map = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS2D_T1map')
    DIS2D_t1w = create_key('sub-{subject}/anat/sub-{subject}_rec-DIS2D_T1w')
    DIS2D_uni_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_rec-DIS2D_MP2RAGE')


    inv_1_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-1_SA2RAGE')
    inv_2_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-2_SA2RAGE')
    b1map_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1map_SA2RAGE')
    b1Div_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1Div_SA2RAGE')

           #only calculated for DIS2D 
    DIS2D_inv_1_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-1_rec-DIS2D_SA2RAGE')
    DIS2D_inv_2_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-2_rec-DIS2D_SA2RAGE')
    DIS2D_b1Div_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1Div_rec-DIS2D_SA2RAGE')
    DIS2D_b1map_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1map_rec-DIS2D_SA2RAGE')
    DIS3D_b1map_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1map_rec-DIS3D_SA2RAGE')



    #2D TSE
    t2_tse = create_key('sub-{subject}/anat/sub-{subject}_acq-tse_run-${item:02d}_T2w')
    DIS2D_t2_tse = create_key('sub-{subject}/anat/sub-{subject}_acq-tse_run-{item:02d}_rec-DIS2D_T2w')
    DIS3D_t2_tse = create_key('sub-{subject}/anat/sub-{subject}_acq-tse_run-{item:02d}_rec-DIS3D_T2w')




    # BOLD
    rest = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:02d}_bold')
    rest_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:02d}_sbref')

    rest_psf = create_key('sub-{subject}/func/sub-{subject}_acq-psf_task-rest_run-{item:02d}_bold')
    rest_psf_dico = create_key('sub-{subject}/func/sub-{subject}_acq-psf_task-rest_run-{item:02d}_rec-dico_bold')


    #Diffusion
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_run-{item:02d}_dwi')
    dwi_sbref = create_key('sub-{subject}/dwi/sub-{subject}_run-{item:02d}_sbref')

    #Field Maps:

    #Multiple phase enc  pepolar
    fmap_PA = create_key('sub-{subject}/fmap/sub-{subject}_dir-PA_epi')
    fmap_PA_sbref = create_key('sub-{subject}/fmap/sub-{subject}_dir-PA_sbref')
    
    #GRE phase diff 
    fmap_diff = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    fmap_magnitude = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')

    #T2 SPACE
    spc_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-spc_T2w')

    #Dist. corr. versions:
    DIS2D_spc_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-spc_rec-DIS2D_T2w')
    DIS3D_spc_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-spc_rec-DIS3D_T2w')

    #Time-of-flight Angio
    TOF_angio = create_key('sub-{subject}/anat/sub-{subject}_acq-TOF_angio')

    DIS2D_TOF_angio = create_key('sub-{subject}/anat/sub-{subject}_acq-TOF_rec-DIS2D_angio')
    DIS3D_TOF_angio = create_key('sub-{subject}/anat/sub-{subject}_acq-TOF_rec-DIS3D_angio')

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
    me_t1     = create_key('sub-{subject}/anat/sub-{subject}_echo_acq-MP2RAGE_run-{item:02d}_T1w')
    me_t1map  = create_key('sub-{subject}/anat/sub-{subject}_echo_acq-MP2RAGE_run-{item:02d}_T1map')
    me_t1inv1 = create_key('sub-{subject}/anat/sub-{subject}_echo_inv-1_run-{item:02d}_MP2RAGE')
    me_t1inv2 = create_key('sub-{subject}/anat/sub-{subject}_echo_inv-2_run-{item:02d}_MP2RAGE')
    me_t1uni  = create_key('sub-{subject}/anat/sub-{subject}_echo_acq-UNI_run-{item:02d}_MP2RAGE')

    me_t1inv1_ce = create_key('sub-{subject}/anat/sub-{subject}_inv-1_run-{item:02d}_MEMP2RAGE')
    me_t1_ce     = create_key('sub-{subject}/anat/sub-{subject}_acq-MEMP2RAGE_run-{item:02d}_T1w')
    me_t1inv2_ce = create_key('sub-{subject}/anat/sub-{subject}_inv-2_run-{item:02d}_MEMP2RAGE')
    me_t1uni_ce  = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_run-{item:02d}_MEMP2RAGE')

    # DIR T2 #
    dir_t2       = create_key('sub-{subject}/anat/sub-{subject}_acq-DIR_T2w')
    DIS2D_dir_t2 = create_key('sub-{subject}/anat/sub-{subject}_acq-DIR_rec-DIS2D_T2w')

    info = { inv1_mp2rage:[],t1map:[],t1w:[],uni_mp2rage:[],inv2_mp2rage:[],
             DIS2D_inv1_mp2rage:[],DIS2D_t1map:[],DIS2D_t1w:[],DIS2D_inv2_mp2rage:[],DIS2D_uni_mp2rage:[],
             DIS3D_inv1_mp2rage:[],DIS3D_t1map:[],DIS3D_t1w:[],DIS3D_inv2_mp2rage:[],DIS3D_uni_mp2rage:[],

             me_t1:[],me_t1map:[],me_t1inv1:[],me_t1inv1:[],me_t1inv2:[],me_t1uni:[],
             me_t1inv1_ce:[],me_t1_ce:[],me_t1inv2_ce:[],me_t1uni_ce:[],

			
             TOF_angio:[], DIS2D_TOF_SAG:[], DIS2D_TOF_COR:[], DIS2D_TOF_TRA:[], DIS2D_TOF_angio:[], DIS3D_TOF_angio:[],

             mag_echo_GRE:[],
		phase_echo_GRE:[],
		DIS2D_mag_echo_GRE:[],
		DIS2D_phase_echo_GRE:[],
		DIS3D_mag_echo_GRE:[],
		DIS3D_phase_echo_GRE:[],

	     T2_star:[],
	     DIS2D_T2_star:[],
	     DIS3D_T2_star:[],

             spc_T2w:[], DIS2D_spc_T2w:[], DIS3D_spc_T2w:[],
            
             inv_1_sa2rage:[],inv_2_sa2rage:[],b1Div_sa2rage:[],b1map_sa2rage:[],
                        DIS2D_inv_1_sa2rage:[],DIS2D_inv_2_sa2rage:[],DIS2D_b1Div_sa2rage:[],DIS2D_b1map_sa2rage:[],
                        DIS3D_b1map_sa2rage:[],

             t2_tse:[], DIS2D_t2_tse:[], DIS3D_t2_tse:[],


             rest:[],rest_sbref:[],
             rest_psf:[],rest_psf_dico:[],

             dwi:[],dwi_sbref:[],

             fmap_PA:[],fmap_PA_sbref:[],fmap_diff:[],fmap_magnitude:[],

             
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
        if ('sa2rage' in s.series_description):
                    if ('ND' in (s.image_type[3].strip())):
			if ('invContrast1' in s.series_description):
				info[inv_1_sa2rage].append({'item': s.series_id})
			if ('invContrast2' in s.series_description):
				info[inv_2_sa2rage].append({'item': s.series_id})
                        if ('OTHER' in (s.image_type[2].strip())):
				info[b1map_sa2rage].append({'item': s.series_id})
			if ('b1DivImg' in s.series_description):
				info[b1Div_sa2rage].append({'item': s.series_id})
                    if ('DIS2D' in (s.image_type[3].strip())):
			if ('invContrast1' in s.series_description):
				info[DIS2D_inv_1_sa2rage].append({'item': s.series_id})
			if ('invContrast2' in s.series_description):
				info[DIS2D_inv_2_sa2rage].append({'item': s.series_id})
                        if ('OTHER' in (s.image_type[2].strip())):
				info[DIS2D_b1map_sa2rage].append({'item': s.series_id})
			if ('b1DivImg' in s.series_description):
				info[DIS2D_b1Div_sa2rage].append({'item': s.series_id})
                    if ('DIS3D' in (s.image_type[3].strip())):
                        if ('OTHER' in (s.image_type[2].strip())):
				info[DIS3D_b1map_sa2rage].append({'item': s.series_id})
	

  
        #t2 tse
        if ('t2_tse' in s.series_description): 
	            if ('ND' in (s.image_type[3].strip())):
    		        info[t2_tse].append({'item': s.series_id})
                    if ('DIS3D' in (s.image_type[3].strip())):
    		        info[DIS3D_t2_tse].append({'item': s.series_id})
                    if ('DIS2D' in (s.image_type[3].strip())):
    		        info[DIS2D_t2_tse].append({'item': s.series_id})


       
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
            if ( s.dim4 > 1 and ('mbep2d_diff' in (s.series_description).strip()) ) :
                info[dwi].append({'item': s.series_id})
            if ( s.dim4 == 1 and ('mbep2d_diff' in (s.series_description).strip()) and 'SBRef' in (s.series_description).strip() ) :
                info[dwi_sbref].append({'item': s.series_id})

        #susceptibility ND multiecho
	if ('susc' in s.series_description):
	    if ('M' in (s.image_type[2].strip())):
                 if ('ND' in (s.image_type[3].strip())):
    	            info[mag_echo_GRE].append({'item': s.series_id})
                 if ('DIS2D' in (s.image_type[3].strip())):
    	            info[DIS2D_mag_echo_GRE].append({'item': s.series_id})
                 if ('DIS3D' in (s.image_type[3].strip())):
    	            info[DIS3D_mag_echo_GRE].append({'item': s.series_id})

	    if ('P' in (s.image_type[2].strip())):
                 if ('ND' in (s.image_type[3].strip())):
        	    info[phase_echo_GRE].append({'item': s.series_id})
                 if ('DIS2D' in (s.image_type[3].strip())):
    	            info[DIS2D_phase_echo_GRE].append({'item': s.series_id})
                 if ('DIS3D' in (s.image_type[3].strip())):
    	            info[DIS3D_phase_echo_GRE].append({'item': s.series_id})

	#T2star
	if ('T2Star' in s.series_description):
            if ('ND' in (s.image_type[3].strip())):
    	        info[T2_star].append({'item': s.series_id})
            if ('DIS2D' in (s.image_type[3].strip())):
    	        info[DIS2D_T2_star].append({'item': s.series_id})
            if ('DIS3D' in (s.image_type[3].strip())):
    	        info[DIS3D_T2_star].append({'item': s.series_id})

 	#spc T2w
        if ('spc_T2' in s.series_description): 
            if ('ND' in (s.image_type[3].strip())):
	        info[spc_T2w].append({'item': s.series_id})
            if ('DIS2D' in (s.image_type[3].strip())):
	        info[DIS2D_spc_T2w].append({'item': s.series_id})
            if ('DIS3D' in (s.image_type[3].strip())):
                info[DIS3D_spc_T2w].append({'item': s.series_id})

	#TOF angio
        if ('3D_TOF' in s.series_description): 
            if (s.dim3>1):
     	        if ('ND' in (s.image_type[3].strip())):
   	            info[TOF_angio].append({'item': s.series_id})
                if ('DIS2D' in (s.image_type[3].strip())):
                    info[DIS2D_TOF_angio].append({'item': s.series_id})
                if ('DIS3D' in (s.image_type[3].strip())):
    	            info[DIS3D_TOF_angio].append({'item': s.series_id})
            if (s.dim4==1):
                if ('DIS2D' in (s.image_type[3].strip())):
	           if ('SAG' in (s.series_description).strip()):
		        info[DIS2D_TOF_SAG].append({'item': s.series_id})
                   if ('COR' in (s.series_description).strip()):
			info[DIS2D_TOF_COR].append({'item': s.series_id})
		   if ('TRA' in (s.series_description).strip()):
			info[DIS2D_TOF_TRA].append({'item': s.series_id})


            

   
    return info
