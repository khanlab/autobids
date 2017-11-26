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


	##########################
	########## ANAT ##########
	##########################

        dc_dir='derivatives/distortion_corrected'

        #MP2RAGE:
	inv1_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-1_MP2RAGE')
	inv2_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_inv-2_MP2RAGE')
	t1map = create_key('sub-{subject}/anat/sub-{subject}_T1map')
	t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
	uni_mp2rage = create_key('sub-{subject}/anat/sub-{subject}_acq-UNI_MP2RAGE')

        #Dist. corrected versions:
        DIS3D_inv1_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_inv-1_rec-DIS3D_MP2RAGE')
	DIS3D_inv2_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_inv-2_rec-DIS3D_MP2RAGE')
	DIS3D_t1map = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS3D_T1map')
	DIS3D_t1w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS3D_T1w')
	DIS3D_uni_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-UNI_rec-DIS3D_MP2RAGE')

        DIS2D_inv1_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_inv-1_rec-DIS2D_MP2RAGE')
	DIS2D_inv2_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_inv-2_rec-DIS2D_MP2RAGE')
	DIS2D_t1map = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS2D_T1map')
	DIS2D_t1w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS2D_T1w')
	DIS2D_uni_mp2rage = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-UNI_rec-DIS2D_MP2RAGE')

	#T2 SPACE
	spc_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-spc_T2w')

        #Dist. corr. versions:
	DIS2D_spc_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-spc_rec-DIS2D_T2w')
	DIS3D_spc_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-spc_rec-DIS3D_T2w')

	#2D TSE Transverse
	tse_tra_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-tsetra_T2w')
	
	DIS2D_tse_tra_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-tsetra_rec-DIS2D_T2w')
	DIS3D_tse_tra_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-tsetra_rec-DIS3D_T2w')

        #2D TSE Coronal
	tse_cor_T2w = create_key('sub-{subject}/anat/sub-{subject}_acq-tsecor_T2w')
	
	DIS2D_tse_cor_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-tsecor_rec-DIS2D_T2w')
	DIS3D_tse_cor_T2w = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-tsecor_rec-DIS3D_T2w')


	#Time-of-flight Angio
	TOF_angio = create_key('sub-{subject}/anat/sub-{subject}_acq-TOF_angio')

	DIS2D_TOF_angio = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-TOF_rec-DIS2D_angio')
	DIS3D_TOF_angio = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-TOF_rec-DIS3D_angio')

        #Derived MIPS -- seem to only be calculated with DIS2D
	DIS2D_TOF_SAG = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-TOFSAG_rec-DIS2D_mip')
	DIS2D_TOF_COR = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-TOFCOR_rec-DIS2D_mip')
	DIS2D_TOF_TRA = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_acq-TOFTRA_rec-DIS2D_mip')


	#########################
	#### Multi-echo GRE #####
	#########################


	#Multi-echo GRE (Susc3D)
	mag_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-mag_echo_GRE')
	phase_echo_GRE = create_key('sub-{subject}/anat/sub-{subject}_part-phase_echo_GRE')

	DIS2D_mag_echo_GRE = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_part-mag_rec-DIS2D_echo_GRE')
	DIS2D_phase_echo_GRE = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_part-phase_rec-DIS2D_echo_GRE')
	DIS3D_mag_echo_GRE = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_part-mag_rec-DIS3D_echo_GRE')
	DIS3D_phase_echo_GRE = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_part-phase_rec-DIS3D_echo_GRE')

	#Derived T2 star - seem to only be calculated with DIS2D
	T2_star = create_key('sub-{subject}/anat/sub-{subject}_T2star')
	DIS2D_T2_star = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS2D_T2star')
	DIS3D_T2_star = create_key(dc_dir+'/sub-{subject}/anat/sub-{subject}_rec-DIS3D_T2star')


	#########################
	########## DWI ##########
	#########################

	AP_dwi = create_key('sub-{subject}/dwi/sub-{subject}_acq-AP_dwi')
	PA_b0_dwi = create_key('sub-{subject}/dwi/sub-{subject}_acq-PAb0_dwi')

	##########################
	########## FMAP ##########
	##########################

	##Sequence #3 - 6 (rel B1)
	#mag_rel_B1 = create_key('sub-{subject}/fmap/sub-{subject}_part-mag_acq-rel_B1')
	#phase_rel_B1 = create_key('sub-{subject}/fmap/sub-{subject}_part-phase_acq-rel_B1')
	#mag_rel_B1_rel_B1 = create_key('sub-{subject}/fmap/sub-{subject}_part-mag_acq-rel_B1_rel_B1')
	#phase_rel_B1_rel_B1 = create_key('sub-{subject}/fmap/sub-{subject}_part-phase_acq-rel_B1_rel_B1')

	##Sequence #7 - 9 (abs B1)
	#mag_absB1 = create_key('sub-{subject}/fmap/sub-{subject}_acq-absB1_B1')
	#phase_absB1 = create_key('sub-{subject}/fmap/sub-{subject}_acq-absB1_B1')
	#absB1_AFI = create_key('sub-{subject}/fmap/sub-{subject}_acq-absB1_AFI')

	#Sa2RAGE B1 mapping
	inv_1_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-1_SA2RAGE')
	inv_2_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_inv-2_SA2RAGE')
	b1map_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1map_SA2RAGE')
	b1Div_sa2rage = create_key('sub-{subject}/fmap/sub-{subject}_acq-b1Div_SA2RAGE')

        #only calculated for DIS2D 
        DIS2D_inv_1_sa2rage = create_key(dc_dir+'/sub-{subject}/fmap/sub-{subject}_inv-1_rec-DIS2D_SA2RAGE')
	DIS2D_inv_2_sa2rage = create_key(dc_dir+'/sub-{subject}/fmap/sub-{subject}_inv-2_rec-DIS2D_SA2RAGE')
	DIS2D_b1Div_sa2rage = create_key(dc_dir+'/sub-{subject}/fmap/sub-{subject}_acq-b1Div_rec-DIS2D_SA2RAGE')
	DIS2D_b1map_sa2rage = create_key(dc_dir+'/sub-{subject}/fmap/sub-{subject}_acq-b1map_rec-DIS2D_SA2RAGE')

	DIS3D_b1map_sa2rage = create_key(dc_dir+'/sub-{subject}/fmap/sub-{subject}_acq-b1map_rec-DIS3D_SA2RAGE')

	#GRE Field Map (phase diff, 2 magnitude images)
        fmap_diff = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
        fmap_magnitude = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')



	info = {inv1_mp2rage:[],t1map:[],t1w:[],uni_mp2rage:[],inv2_mp2rage:[],
                        DIS2D_inv1_mp2rage:[],DIS2D_t1map:[],DIS2D_t1w:[],DIS2D_inv2_mp2rage:[],DIS2D_uni_mp2rage:[],
                        DIS3D_inv1_mp2rage:[],DIS3D_t1map:[],DIS3D_t1w:[],DIS3D_inv2_mp2rage:[],DIS3D_uni_mp2rage:[],

			
			spc_T2w:[], DIS2D_spc_T2w:[], DIS3D_spc_T2w:[],

			tse_tra_T2w:[], DIS2D_tse_tra_T2w:[], DIS3D_tse_tra_T2w:[],
			tse_cor_T2w:[], DIS2D_tse_cor_T2w:[], DIS3D_tse_cor_T2w:[],

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


			AP_dwi:[],  PA_b0_dwi:[],

                        inv_1_sa2rage:[],inv_2_sa2rage:[],b1Div_sa2rage:[],b1map_sa2rage:[],
                        DIS2D_inv_1_sa2rage:[],DIS2D_inv_2_sa2rage:[],DIS2D_b1Div_sa2rage:[],DIS2D_b1map_sa2rage:[],
                        DIS3D_b1map_sa2rage:[],

			fmap_diff:[], fmap_magnitude:[]
			}


	for idx, s in enumerate(seqinfo):

		##########################
		########## ANAT ##########
		##########################

		#mp2rage
		if ('mp2rage' in s.series_description):
    			if ('_INV1' in (s.series_description).strip()):
                                if ('DIS2D' in (s.image_type[3].strip())):
    		    		    info[DIS2D_inv1_mp2rage].append({'item': s.series_id})
                                if ('DIS3D' in (s.image_type[3].strip())):
    		    		    info[DIS3D_inv1_mp2rage].append({'item': s.series_id})
                                if ('ND' in (s.image_type[3].strip())):
    		    		    info[inv1_mp2rage].append({'item': s.series_id})
			if ('_T1_Images' in (s.series_description).strip()):
                                if ('DIS2D' in (s.image_type[3].strip())):
                                    info[DIS2D_t1map].append({'item': s.series_id})                                
                                if ('DIS3D' in (s.image_type[3].strip())):
                                    info[DIS3D_t1map].append({'item': s.series_id})
                                if ('ND' in (s.image_type[3].strip())):
    		    		    info[t1map].append({'item': s.series_id})
			if ('_UNI-DEN' in (s.series_description).strip()):
                                if ('DIS2D' in (s.image_type[3].strip())):
                                    info[DIS2D_t1w].append({'item': s.series_id})
                                if ('DIS3D' in (s.image_type[3].strip())):
                                    info[DIS3D_t1w].append({'item': s.series_id})
                                if ('ND' in (s.image_type[3].strip())):
    		    		    info[t1w].append({'item': s.series_id})
			if ('_UNI_Images' in (s.series_description).strip()):
                                if ('DIS2D' in (s.image_type[3].strip())):
    		    		    info[DIS2D_uni_mp2rage].append({'item': s.series_id})
                                if ('DIS3D' in (s.image_type[3].strip())):
    		    	            info[DIS3D_uni_mp2rage].append({'item': s.series_id})
                                if ('ND' in (s.image_type[3].strip())):
    		    		    info[uni_mp2rage].append({'item': s.series_id})
			if ('_INV2' in (s.series_description).strip()):
                                if ('DIS2D' in (s.image_type[3].strip())):
    		    		    info[DIS2D_inv2_mp2rage].append({'item': s.series_id})
                                if ('DIS3D' in (s.image_type[3].strip())):
    		    		    info[DIS3D_inv2_mp2rage].append({'item': s.series_id})
                                if ('ND' in (s.image_type[3].strip())):
    		    		    info[inv2_mp2rage].append({'item': s.series_id})

		#spc T2w
                if ('spc_T2' in s.series_description): 
	            if ('ND' in (s.image_type[3].strip())):
    		        info[spc_T2w].append({'item': s.series_id})
                    if ('DIS2D' in (s.image_type[3].strip())):
    		        info[DIS2D_spc_T2w].append({'item': s.series_id})
                    if ('DIS3D' in (s.image_type[3].strip())):
    		        info[DIS3D_spc_T2w].append({'item': s.series_id})

		#tse tra T2w
                if ('t2_tse_tra' in s.series_description): 
	            if ('ND' in (s.image_type[3].strip())):
    		        info[tse_tra_T2w].append({'item': s.series_id})
                    if ('DIS3D' in (s.image_type[3].strip())):
    		        info[DIS3D_tse_tra_T2w].append({'item': s.series_id})
                    if ('DIS2D' in (s.image_type[3].strip())):
    		        info[DIS2D_tse_tra_T2w].append({'item': s.series_id})


                #tse cor T2w
                if ('t2_tse_cor' in s.series_description): 
	            if ('ND' in (s.image_type[3].strip())):
    		        info[tse_cor_T2w].append({'item': s.series_id})
                    if ('DIS3D' in (s.image_type[3].strip())):
    		        info[DIS3D_tse_cor_T2w].append({'item': s.series_id})
                    if ('DIS2D' in (s.image_type[3].strip())):
    		        info[DIS2D_tse_cor_T2w].append({'item': s.series_id})



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

                                
                #susceptibility ND multiecho
		if ('susc3d' in s.series_description):
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

                #########################
		########## DWI ##########
		#########################

		#mbep2d dwi
                if ('diff' in s.protocol_name):
                    if ( s.dim4 > 1):
                        if ('AP' in (s.series_description).strip()) :
                            info[AP_dwi].append({'item': s.series_id})
                        if ('PA' in (s.series_description).strip()) :
                            info[PA_b0_dwi].append({'item': s.series_id})
            

		##########################
		########## FMAP ##########
		##########################


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
	
	#GRE field map 
                if ('field_mapping' in s.protocol_name):   
                    if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                        if('P' in (s.image_type[2].strip()) ):
                            info[fmap_diff].append({'item': s.series_id})
                        if('M' in (s.image_type[2].strip()) ):
                            info[fmap_magnitude].append({'item': s.series_id})

	   		



	return info


		
