# Superseded — TUH_BIDS prototype

> **This repository is archived and retained only for historical provenance.**

`TUH_BIDS` was an early prototype for converting TUH EEG EDF recordings to BIDS with MNE/MNE-BIDS.

The prototype contains two small, path-specific scripts created around a single local TUH setup. The current repository audit found that it is not a maintained converter: paths are hard-coded to the original workstation, montage handling is limited, and `code/single_edf_file_conversion.py` does not currently pass Python syntax compilation because of an indentation error in the legacy script.

## Maintained successor

The maintained implementation is now:

**epilepsy2bids**

https://github.com/andraderenew/epilepsy2bids

That project provides a packaged Python library with tests and dataset-specific converters, including support for the TUH EEG Seizure Corpus and a dedicated `tuep2bids` CLI for the TUH EEG Epilepsy corpus.

The current TUEP implementation includes dataset indexing, EEG standardization, BIDS writing, participants/per-recording metadata, and `*.csv_bi` seizure annotation handling. Its remaining limitations are documented in the maintained repository.

## Historical contents

The original files are intentionally preserved here to document the development path:

- `code/single_edf_file_conversion.py`
- `code/several-edfs_one-patient_several-sessions&runs_EDF2BIDS_file_conversion.py`

They should be treated as historical prototypes, not as the recommended conversion workflow.

## Data access

TUH EEG data remain subject to the original TUH access and licensing conditions. No TUH source data are distributed through this repository.

## Status

**Superseded / archived**

For maintained code, use `epilepsy2bids`.
