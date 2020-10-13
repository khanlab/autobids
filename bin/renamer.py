#!/usr/bin/env python3

import re
import argparse
import os

parser = argparse.ArgumentParser(description='Launches JupyterLab in an interactive compute canada job, creating the required ssh tunnel.')

parser.add_argument('--in_parse',help='Regular expression to parse subject (and session optionally) from PatientName (default: %(default)s)',required=True,
                    default='(?:[\w]*)(?<=[Tt][Oo][Pp][Ss][Yy]_)(?P<subject>[A-Za-z0-9]+)_*(?P<session>[A-Za-z0-9]+)*')
parser.add_argument('--in_tar',help='Tar filename',required=True)
parser.add_argument('--out_reformat',help='Format string to rename output file (can use subject, session, pi, project, yyyymmdd, instance, hash, extension) (default: %(default)s)',
                    default='{pi}_{project}_{yyyymmdd}_{subject}_{session}_{instance}.{hash}.{extension}')
parser.add_argument('--default_session',help='If session not found, use this as default session')

args = parser.parse_args()

def renamer (tar, parse_patientname_regex, rename_format_string,default_session=None):

    """
    #patient_name = yyyy_mm_dd_{study}_{subject}[_{session}] 
    patient_name = '?P<date>[\d]{4}_[\d]{2}_[\d]{2})'\
                    '_(?P<study>[A-Za-z0-9]+)'\
                    '_(?P<subject>[A-Za-z0-9]+)'\
                    '_*(?P<session>[A-Za-z0-9]+)*',
    
    # input: search string for patient_name
    #patient_name = *_{subject}[_{session}] 
    patient_name = '(?:[\w]+)_(?P<subject>[A-Za-z0-9]+)_*(?P<session>[A-Za-z0-9]+)*'

    # input: rename formatting string
    #rename formatting string
    rename_string = '{pi}_{project}_{yyyymmdd}_{subject}_{session}_{instance}.{hash}.{extension}'
    """
    
    #define the search list (entries will be joined by underscores)
    search_list = ['(?P<pi>[A-Za-z0-9]+)',
                '(?P<project>[A-Za-z0-9]+)',
                '(?P<yyyymmdd>[0-9]{8})',
                '(?P<patient_name>(' + parse_patientname_regex + ')',
                '(?P<instance>[0-9]+).(?P<hash>[0-9A-F]{8}).(?P<extension>tar(.gz)*)']

    #do the search, and get the matching group terms as a dict
    match_dict = re.search('_'.join(search_list),tar).groupdict()
    #set default values, e.g. ensures session is set
    if match_dict['session'] == None:
        match_dict['session'] = default_session

    #create renamed tarfile name
    renamed = rename_format_string.format(**match_dict)
    
    return renamed


basename = os.path.basename(args.in_tar)
print(renamer(basename, args.in_parse, args.out_reformat,default_session=args.default_session))
