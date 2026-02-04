# About Dataset: Cybercrime Forensic Dataset

## Overview
**Observations:** 7,400  
**Description:** This dataset simulates various cyber activities and anomalies for cybercrime forensic analysis. It contains information about user network activities, file management, and system access, with flagged security threats.

## Key Features

*   **Timestamp:** Exact date and time of the activity. Crucial for timeline analysis.
*   **User_ID:** Unique identifier for the user.
*   **IP_Address:** Originating IP address (geolocation/internal vs external).
*   **Activity_Type:** Action performed:
    *   Login
    *   File Access
    *   File Modification
    *   File Deletion
    *   Network Traffic
    *   Remote Login
    *   USB Insert
*   **Resource_Accessed:** File or system resource involved.
*   **File_Name:** Name of the file (if applicable).
*   **Action:** Outcome (e.g., successful login, file read, deletion).
*   **Login_Attempts:** Number of attempts (useful for brute-force detection).
*   **File_Size:** Size of the file (useful for detecting data exfiltration).
*   **Anomaly_Type:** Flag for suspicious activities:
    *   Brute_Force
    *   DDoS_Attempt
    *   Data_Exfil
    *   USB_Access
    *   None (Normal)
*   **Label:** Binary classification:
    *   `Normal`: No suspicious behavior.
    *   `Suspicious`: Flagged anomalies.

## Purpose
Designed for developing machine learning models (IDS, Anomaly Detection) and training forensic analysis skills.

## Potential Applications
*   **Cybersecurity:** Identifying breaches and unauthorized access.
*   **Incident Response:** Forensic evidence analysis.
*   **Machine Learning:** Training threat detection models.
