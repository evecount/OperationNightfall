# **Lesson Plan: Pandas for Digital Forensics**

**Total Duration:** Self-Paced (Approx. 3 hours)  
**Format:** Dual Pathway (Technical Skills + Applied Forensic Mission)  
**Prerequisite:** Completion of `pre-class.md` setup.

---

## **🎯 Learning Pathway**

This course matches technical skills with forensic applications. You should alternate between the two notebooks:

| **Phase** | **Topic** | **📘 Field Manual** (`pandas_lesson.ipynb`) | **🕵️‍♀️ Operation Nightfall** (`forensic_investigation.ipynb`) |
| :--- | :--- | :--- | :--- |
| **1** | **Structures** | Create DataFrames, inspect columns, types. | Load "Process Logs", finding volume of "Noise". |
| **2** | **Selection** | `.loc`, `.iloc`, Boolean filtering. | Filter for `powershell.exe`, find "Patient Zero". |
| **3** | **Analysis** | String operations, Merging datasets. | Clean hidden spaces in process names, Correlate IP traffic. |
| **4** | **Reporting** | Sorting, Grouping, Aggregation. | Calculate total bytes stolen, generate damage report. |

---

## **📚 Part 1: Basic Training (Syntax Focus)**

**Goal:** Master the tools before entering the field.  
**Notebook:** `pandas_lesson.ipynb`

### **1. Structures & Modification**
*   **Concept:** A DataFrame is like a programmable spreadsheet.
*   **Key Skills:**
    *   Creating data from scratch (Dictionaries).
    *   `df.head()`, `df.info()`.
    *   Adding columns: `df['Price'] = ...`

### **2. The Art of Selection**
*   **Concept:** Finding specific data points without scrolling.
*   **Key Skills:**
    *   **Label vs Position:** `.loc[]` (by name) vs `.iloc[]` (by number).
    *   **Filtering:** `df[df['Value'] > 100]` (Show me only the big transactions).

### **3. Operations**
*   **Concept:** Changing data at scale.
*   **Key Skills:**
    *   **Sorting:** `sort_values()` to rank data.
    *   **Applying Functions:** Using `.apply()` for custom logic.

---

## **🕵️‍♀️ Part 2: Operation Nightfall (Applied Mission)**

**Goal:** Catch the hacker using your new skills.  
**Notebook:** `forensic_investigation.ipynb`

### **Mission Briefing**
You are investigating `FIN-WS-01`. User "Alice" denies running malicious scripts.

### **Phase 1: Triage**
*   **Task:** Load `process_log.csv`.
*   **Challenge:** The data is large. Use `value_counts()` to identify what is running the most (e.g., Chrome, Teams).

### **Phase 2: The Hunt**
*   **Task:** Filter for `powershell.exe`.
*   **Twist:** The attacker is hiding. You will learn to use `.str.strip()` to clean dirty data and expose the malware.

### **Phase 3: Connection**
*   **Task:** Connect the Process ID (PID) to the Network Log.
*   **Skill:** `pd.merge()`. This proves that the PowerShell script was the one communicating with the Russian IP.

### **Phase 4: Damage Report**
*   **Task:** How much data was lost?
*   **Skill:** `groupby('Destination_IP')['Bytes']`. Sum up the total exfiltration.

---

## **✅ Definition of Done**
You are ready to move on when:
1.  You have completed the exercises in `pandas_lesson.ipynb`.
2.  You have successfully generated the `final_report.csv` in `forensic_investigation.ipynb`.
