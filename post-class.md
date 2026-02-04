# **Post-Class Assignment: Mission Debrief**

**Status:** Mission Complete via `forensic_investigation.ipynb`.  
**Next Objective:** Independent Field Work.

---

## **📝 Part 1: Mission Debrief (Recap)**

Reflect on the **Operation Nightfall** investigation. You used `pandas` to solve a crime.

### **Technique Review**
1.  **Why did filtering for `powershell.exe` fail initially?**
    *   *Answer:* The attacker used "dirty data" (trailing spaces) to evade simple filters. We had to use `.str.strip()` to sanitize the input.
2.  **How did we prove the malware was communicating externally?**
    *   *Answer:* We **merged** the Process Log (which had the PID) with the Network Log (which had the IP addresses) using `pd.merge(on='PID')`.
3.  **What was the "Smoking Gun"?**
    *   *Answer:* A connection to a known C2 IP on Port 4444 (Metasploit default), transferring 5MB of data.

---

## **⚔️ Part 2: The Independent Challenge**

Now that you have learned the tools, it's time to work on real data.

### **Dataset: Cybercrime Forensic Dataset**
We have included a real-world dataset in the `assets/` folder:
`assets/cybercrime-forensic-dataset/cybercrime_files.csv`

**Your Objective:**
1.  Create a new notebook.
2.  Load this new dataset.
3.  **Find the Anomalies:**
    *   Filter for `Anomaly_Type == 'Data_Exfil'`.
    *   Sort by `File_Size` to see the largest thefts.
    *   Use `value_counts()` on `Activity_Type` to see the most common attack vectors.

> **⚠️ Warning:** This is real-world structure, which means it might be cleaner or messier than our simulation. Treat it with the same rigorous process: **Triage -> Hunt -> Correlate.**

---
## **📊 Part 3: Building a Threat Dashboard**

The CISO wants a visual report. Using the Cybercrime Dataset, you will build a "Command Center" view.

### **1. The Metric Counters**
Write code to count and display these critical events.
*   **Remote Logins:** Count how many times `Activity_Type` is "Remote Login".
*   **Destruction:** Count how many times `Activity_Type` is "File Deletion".
*   **The Most Attacked Resource:** Use `value_counts()` on `Resource_Accessed`.

### **2. The Timeline Flagging**
We need to see *when* the attacks happened.
1.  Convert the `Timestamp` column to actual datetime objects: `df['Timestamp'] = pd.to_datetime(df['Timestamp'])`
2.  **Visual Flag:** Plot the attacks over time using a simple bar chart:
    ```python
    # Count activities by Hour
    df['Hour'] = df['Timestamp'].dt.hour
    df['Hour'].value_counts().sort_index().plot(kind='bar', title='Attacks by Hour')
    ```

---
## **📚 Part 4: Advanced Topics (Optional)**

*   **Reindexing:** Changing the row labels to align different datasets.
*   **Dropping Entries:** Removing noise using `df.drop()`.


