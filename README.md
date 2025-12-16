#Avatar Open Data UI
This project provides a GUI interface for publishing brainwave data (Open Data) as part of the Avatar system. The GUI integrates with the file-opendata/opendata.py script, which automates data augmentation for Brain-Computer Interface (BCI) datasets. The tool replicates and shuffles data across six thought categories: forward, backward, land, takeoff, right, and left.
This submission uses dummy CSV files for testing purposes. No real brainwave data is included to comply with privacy and GitHub storage limitations.
Features
•	Data Sanitization: Renames all CSV files to sequential numbers (1.csv, 2.csv, etc.) across categories.
•	Balanced Replication: Randomly replicates files evenly (50 per category), tracking usage to avoid duplicates until originals are exhausted.
•	Size Monitoring: Tracks replicated files until a 60% increase is achieved.
•	File Organization: Uses temporary directories for staging, then integrates copies into the original folders.
•	Final Shuffling: Renames all files to renamed_1.csv, renamed_2.csv, etc., and shuffles order for additional anonymization.
•	Reporting: Outputs final dataset size, replicated files per category, and total file count.
Directory Structure
avatar-opendata-ui/
├── main.py
├── avatar_backend.py
├── CloudComputingTab.qml
├── OpenDataSection.qml
├── file-opendata/
│   └── opendata.py
      └── data_clean/
        └── data_clean/        
        ├── forward/
        ├── backward/
        ├── land/
        ├── takeoff/
        ├── right/
        └── left/

Output Example
Total size of the new dataset: 0.00 GB
Number of replicated files per category:
  - ('testdata', 'backward'): 150
  - ('testdata', 'forward'): 150
  - ('testdata', 'land'): 150
  - ('testdata', 'left'): 150
  - ('testdata', 'right'): 150
  - ('testdata', 'takeoff'): 150
Total number of files in the new dataset: 2112
--------------------------------------------------
Open Data finished successfully.

•	Dependencies: Python 3.9+ and PySide6 only. No other external libraries required.
