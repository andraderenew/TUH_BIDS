# TUH_BIDS
Code that converts the EEG epilepsy TUEP corpus of the repository to BIDS format (if you want to use it in your data see point 5). 

Requirements to test this code (see further specifications below):

1. EDF files from TUH epilepsy database

2. MNE Python

3. Modify the paths depending on your subject ID, or path to save the output files.

4. For the codes I have used a patient with montage 02_tcp_le_montage (linked-ears) meaning if you use a patient different than the one listed you should verify to have the same montage type. There are 4 types named: 01_tcp_ar_montage, 02_tcp_le_montage, 03_tcp_ar_a_montage, 04_tcp_le_a_montage. Other montages will possibly be used in another code future release to be announced soon.

5. If you wanted to use this in another data other than TUH Epilepsy database. Then possibly you could try eeg data from this tutorial. https://mne.tools/mne-bids/dev/auto_examples/convert_eeg_to_bids.html. 


Further specifications:

1. You can access TUH database under their permission in this website you have all the information. https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml

2. Install MNE Python any version should work but this has been tested in version 1.6 stable and development version 1.7.0.dev39+g7ce9aa178 (devel, latest release is 1.6.0). If development version mne_bids package should be installed separately. In MAC OS you could install with "python3 -m pip install mne_bids". 

3. Depending on the code there are different paths to change.

Paths to change in ... :

... "single_edf_file_conversion.py"
1) edf_path --> path to edf files saved from TUH database
2) bidsroot -->  path to output of BIDS format files
3) in raw.save line 56 change /Users/andraderenew/Downloads/TUH_EEG/aaaaaaac_s002_t000.fif to whatever the path you will save the files in FIF format (EEG format file of MNE). You can commment adding "#" before the code in L56 if you don't want to save this type of file. 

... "several-edfs_one-patient_several-sessions&runs_EDF2BIDS_file_conversion.py"
1) edf_directory --> path to edf files saved from TUH database
2) root --> path to output of BIDS format files
3) in "raw.save" line 62 change /Users/andraderenew/Downloads/TUH_EEG/{session_id}.fif to whatever the path you will save the files in FIF format (EEG format file of MNE).

5. Then change the paths as indicated in point 3 in further  specifications. Although the montage you will need to change as well. Probably you should comment all the lines referring to this part of channel mappings. You can use the code in the tutorial to adapt it your montage. 

It has been tested in:
macOS-14.2.1-arm64-arm-64bit
Python 3.11.6


This command output python -c "import mne; mne.sys_info()" for further details gave:

Platform             macOS-14.2.1-arm64-arm-64bit
Python               3.11.6 | packaged by conda-forge | (main, Oct  3 2023, 10:37:07) [Clang 15.0.7 ]
Executable           /Users/andraderenew/anaconda3/envs/mne/bin/python
CPU                  arm (8 cores)
Memory               8.0 GB

Core
├☑ mne               1.7.0.dev39+g7ce9aa178 (devel, latest release is 1.6.0)
├☑ numpy             1.26.2 (OpenBLAS 0.3.25 with 8 threads)
├☑ scipy             1.11.4
├☑ matplotlib        3.8.2 (backend=MacOSX)
├☑ pooch             1.8.0
└☑ jinja2            3.1.2

Numerical (optional)
├☑ sklearn           1.3.2
├☑ numba             0.58.1
├☑ nibabel           5.2.0
├☑ nilearn           0.10.2
├☑ dipy              1.7.0
├☑ openmeeg          2.5.7
├☑ pandas            2.1.4
└☐ unavailable       cupy

Visualization (optional)
├☑ pyvista           0.43.0 (OpenGL 4.1 Metal - 88 via Apple M1)
├☑ pyvistaqt         0.11.0
├☑ vtk               9.2.6
├☑ qtpy              2.4.1 (PyQt5=5.15.8)
/Users/andraderenew/anaconda3/envs/mne/lib/python3.11/site-packages/h5py/__init__.py:36: UserWarning: h5py is running against HDF5 1.14.3 when it was built against 1.14.2, this may cause problems
  _warn(("h5py is running against HDF5 {0} when it was built against {1}, "
├☑ pyqtgraph         0.13.3
├☑ mne-qt-browser    0.6.1
├☑ ipywidgets        8.1.1
├☑ trame_client      2.14.1
├☑ trame_server      2.13.1
├☑ trame_vtk         2.6.2
├☑ trame_vuetify     2.3.1
└☐ unavailable       ipympl

Ecosystem (optional)
├☑ mne-bids          0.14
├☑ mne-connectivity  0.6.0
└☐ unavailable       mne-nirs, mne-features, mne-icalabel, mne-bids-pipeline



