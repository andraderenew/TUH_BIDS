# Authors: Stefan Appelhoff <stefan.appelhoff@mailbox.org>
#
# License: BSD-3-Clause

# We import necessary libraries
import os.path as op
import shutil

import mne
from mne.datasets import eegbci

from mne_bids import write_raw_bids, BIDSPath, print_dir_tree
from mne_bids.stats import count_events

# Download the EEG data from PhysioBank
# -------------------------------------
# Here we download EEG data from the PhysioBank database.
# We will be working with a dataset containing experimental runs related to eye movement and motor imagery tasks.

# Load the EEG data and set power line frequency
edf_path = '/Users/andraderenew/Downloads/TUH_EEG/aaaaaaac_s002_t000.edf'
raw = mne.io.read_raw_edf(edf_path, preload=False)
raw.info["line_freq"] = 50  # specifying power line frequency as required by BIDS

# Prepare channel mapping and apply standard montage
# -------------------------------------------------
# We modify the channel mapping dictionary and apply the standard 10-20 montage.

# Your updated channel mapping dictionary
channel_mapping = {
    'EEG FP1-LE': 'FP1', 'EEG F7-LE': 'F7', 'EEG T3-LE': 'T3', 'EEG T5-LE': 'T5',
    'EEG FP2-LE': 'FP2', 'EEG F8-LE': 'F8', 'EEG T4-LE': 'T4', 'EEG T6-LE': 'T6',
    'EEG A1-LE': 'A1', 'EEG C3-LE': 'C3', 'EEG CZ-LE': 'Cz', 'EEG C4-LE': 'C4',
    'EEG F3-LE': 'F3', 'EEG P3-LE': 'P3', 'EEG F4-LE': 'F4', 'EEG P4-LE': 'P4', 
    'EEG A2-LE': 'A2', 'EEG O1-LE': 'O1', 'EEG O2-LE': 'O2', 'EEG FZ-LE': 'Fz', 
    'EEG PZ-LE': 'Pz', 'EEG OZ-LE': 'Oz','EEG PG1-LE': 'PG1', 'EEG PG2-LE': 'PG2', 
    'EEG EKG-LE': 'EKG', 'EEG SP2-LE': 'SP2', 'EEG SP1-LE': 'SP1', 'EEG RLC-LE': 'RLC', 
    'EEG LUC-LE': 'LUC', 'EEG 30-LE': '30', 'EEG T1-LE': 'T1', 'EEG T2-LE': 'T2',
    }

raw.rename_channels(channel_mapping)

# Load or create your raw data before applying the standard montage
# raw = mne.io.read_raw_fif('your_data.fif', preload=True)

montage = mne.channels.make_standard_montage('standard_1020')

missing_channels = set(raw.ch_names) - set(montage.ch_names)
if missing_channels:
    # Handle missing channels here

# Set the montage (handle missing channels as needed)
raw.set_montage(montage, on_missing='ignore')

# Save the modified Raw object to a new file
raw.save('/Users/andraderenew/Downloads/TUH_EEG/aaaaaaac_s002_t000.fif', overwrite=True)

# Visualize electrode positions
raw.plot_sensors()

# Convert EEG data to BIDS format
# -------------------------------
# Use MNE-BIDS to convert the EEG data to a BIDS-compatible directory structure.

subject_id = "aaaaaaac"
task = "rest"
bids_root = '/Users/andraderenew/Downloads/TUHBIDS/'

if op.exists(bids_root):
    shutil.rmtree(bids_root)

# Automatically extract events and write BIDS data
bids_path = BIDSPath(subject=subject_id, task=task, root=bids_root)
write_raw_bids(raw, bids_path, overwrite=True)

# Display the BIDS directory structure
print_dir_tree(bids_root)

# Count events on the whole dataset
counts = count_events(bids_root)
counts

# Cite mne-bids
# -------------
# Cite MNE-BIDS in manuscripts or dataset publications.
readme = op.join(bids_root, "README")
with open(readme, "r", encoding="utf-8-sig") as fid:
    text = fid.read()
print(text)

# Manually check the BIDS directory and meta files
# ------------------------------------------------
# Check BIDS directory and meta files for any missing information.
# Use the BIDS-validator tool to validate your BIDS directories.

# Web version: https://bids-standard.github.io/bids-validator/
# Command line tool: https://www.npmjs.com/package/bids-validator
