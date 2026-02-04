# 🦅 Sentinel User Guide

**Welcome to Operation Sentinel.**
This guide explains how to install, launch, and use the forensic dashboard.

---

## **1. How to Run Sentinel**

You can run the dashboard in two ways: **Locally** (on your computer) or in the **Cloud** (browser-only).

### **Option A: Local Execution (Recommended for Speed)**
Run the app on your own machine. Best for privacy and speed.

1.  **Open Terminal:** Open Command Prompt or PowerShell in the `Pandas_Forensics_Course` folder.
2.  **Install Requirements:** (One time only)
    ```
    pip install -r requirements.txt
    ```
3.  **Launch:**
    ```
    streamlit run app.py
    ```
4.  The app will open automatically at `http://localhost:8501`.

---

### **Option B: Cloud Deployment (Streamlit Cloud)**
Run the app online so you can share the link with others.

1.  **GitHub:** Ensure this project is uploaded to your GitHub repository.
2.  **Streamlit Cloud:**
    *   Go to [share.streamlit.io](https://share.streamlit.io) and sign up with GitHub.
    *   Click **"New App"**.
    *   Select your repository (`Pandas_Forensics_Course`).
    *   Set Main File path to `app.py`.
    *   Click **Deploy**.
3.  Wait 1-2 minutes. Your app is now live on the internet!

---

## **3. Using the Dashboard**

### **Step 1: Evaluation Upload**
*   In the **Sidebar** (left panel), upload your CSV evidence file.
*   **Supported Files:** `process_log.csv` or `network_log.csv` (generated from `forensic_investigation.ipynb`).

### **Step 2: Auto-Triage**
The main screen will instantly display:
*   **Total Events:** The volume of data.
*   **Unique Processes:** How many distinct programs are running.
*   **🚨 Threat Hits:** Our engine automatically scans for known bad binaries (`nmap`, `mimikatz`, `powershell`) and flags them in RED.

### **Step 3: The Threat Console (3D)**
Scroll down to the interactive chart.
*   **Controls:** Use the dropdowns to change the X, Y, and Color axes.
    *   **Hunt for Scans:** Set X=`Time`, Y=`Destination_Port`. Look for vertical lines.
    *   **Hunt for Exfiltration:** Set X=`Bytes_Sent`, Y=`Time`. Look for outliers.
*   **Interaction:**
    *   **Zoom:** Click and drag to zoom in.
    *   **Hover:** Hover over any dot to see the exact PID and Process Name.
    *   **Pan:** Click and hold to move around the graph.

---

## **4. Troubleshooting**
*   **"Command not found":** Ensure you installed Python and added it to your PATH.
*   **"Port 8501 is already in use":** Streamlit will automatically try the next port (8502, 8503, etc.). Check your terminal for the correct URL.
