import os  # Importing the 'os' module for operating system related functionalities
import mne  # Importing the 'mne' library for EEG/MEG data analysis
from mne.datasets import eegbci  # Importing EEGBCI dataset functionality from 'mne.datasets'
from mne_bids import write_raw_bids, BIDSPath, print_dir_tree  # Importing necessary functions from 'mne_bids'
from mne_bids.stats import count_events  # Importing 'count_events' from 'mne_bids.stats'

# Directory containing your EDF files
edf_directory = '/Users/andraderenew/Downloads/TUH_EEG/patients/'

# List all EDF files in the directory
edf_files = [file for file in os.listdir(edf_directory) if file.endswith('.edf')]

for edf_file in edf_files:
    # Extract subject, session, and run IDs from the file name
    file_parts = edf_file.split('_')
    subject_id = file_parts[0]  # Assuming the subject ID is the first part of the file name
    session_id = file_parts[1]  # Assuming the session ID is the second part of the file name
    run_id = file_parts[2].split('.')[0][1:]  # Assuming the run ID is the third part of the file name

    # Construct the BIDS path
    bids_path = BIDSPath(
        subject=subject_id,
        session=session_id,
        run=run_id,
        task='rest',
        root='/Users/andraderenew/Downloads/TUHBIDS/'
    )

    # Read the raw data from the EDF file
    edf_path = os.path.join(edf_directory, edf_file)
    raw = mne.io.read_raw_edf(edf_path, preload=False)
    raw.info["line_freq"] = 50  # specify power line frequency as required by BIDS

    # Mapping channel names to standard names
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

    # Renaming channels using the provided mapping
    raw.rename_channels(channel_mapping)

    # Applying a standard 10-20 montage to the raw data
    montage = mne.channels.make_standard_montage('standard_1020')

    # Checking for missing or mismatched channels
    missing_channels = set(raw.ch_names) - set(montage.ch_names)
    if missing_channels:
        print("The following channels are missing from the montage:", missing_channels)
        # Handle the missing channels here, either by ignoring them or renaming them

    # Setting the montage (handling missing channels as needed)
    raw.set_montage(montage, on_missing='ignore')

    # Saving the modified Raw object to a new file (optional)
    raw.save(f'/Users/andraderenew/Downloads/TUH_EEG/{session_id}.fif', overwrite=True)

    # Displaying the electrode positions
    raw.plot_sensors()

    # Writing the data in BIDS format
    write_raw_bids(raw, bids_path, overwrite=True)
