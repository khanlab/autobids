#! /usr/bin/env python
'''
find duplicate(two .nii.gz files have no difference) runs of .nii.gz.
keep only the first run (nomally run-01), remove others(*.nii.gz and *.json).

'''
import os
import sys
import hashlib


def hashfile(path):
    with open(path, 'rb') as f:
        buf = f.read()
        hasher = hashlib.md5(buf)

    return hasher.hexdigest()


def find_hashs(dir):
    # Dups in format {hash:[names]}
    hashs = {}
    for current_dir, sub_dirs, filenames in os.walk(dir):
        for filename in filenames:
            path = os.path.join(current_dir, filename)
            if path.endswith('.nii.gz'):
                file_hash = hashfile(path)
                if file_hash in hashs:
                    hashs[file_hash].append(path)
                else:
                    hashs[file_hash] = [path]
    return hashs


def main(bids_dir, sub, ses=None):
    # ses not None
    if ses:
        sub_prefix = '{}_{}'.format(sub, ses)
        sub_path_prefix = os.path.join(sub, ses)
    else:
        sub_prefix = '{}'.format(sub)
        sub_path_prefix = sub_prefix

    sub_dir = os.path.join(bids_dir, sub_path_prefix)

    # find dups
    hashs = find_hashs(sub_dir)
    dups = list(filter(lambda x: len(x) > 1, hashs.values()))

    # remove dup .nii.gz and .json 
    for e in dups:
        # order by run-01,run-02,...
        e.sort()

        for i in range(1, len(e)):
            nii_gz_filename = e[i]
            json_filename = nii_gz_filename.replace('.nii.gz', '.json')

            # debug
            #print nii_gz_filename
            #print json_filename

            os.remove(nii_gz_filename)
            os.remove(json_filename)


if __name__ == "__main__":
    if len(sys.argv)-1 < 2:
        print ("Usage: python " + os.path.basename(__file__) + " 'bids_dir' 'sub' ")
        sys.exit(1)
    else:
        bids_dir = sys.argv[1]
        sub = sys.argv[2]

        main(bids_dir, sub)

# test
# Usage: python removeDuplicateRuns.py 'bids_dir' 'sub'
# python removeDuplicateRuns.py /mnt/hgfs/data/correct_runs/bids sub-P019
