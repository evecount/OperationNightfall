# **Pre-Class Self-Study: Introduction to Pandas**

⏱️ **Estimated Time:** 45-60 minutes  
📅 **Complete Before:** Starting the Case Files

## **🎯 What to Expect**

This course consists of **two parallel tracks**:

1.  **📘 The Field Manual (`pandas_lesson.ipynb`):** A standard, syntax-focused guide. You will use this to learn the basics of Pandas (DataFrames, Series, Selection) using simple concepts like fruit inventories.
2.  **🕵️‍♀️ Operation Nightfall (`forensic_investigation.ipynb`):** A high-stakes forensic investigation. You will apply your new skills to catch a hacker in a simulated corporate breach.

**We recommend keeping both notebooks open.** Use the Field Manual to learn "How do I filter?", then switch to Operation Nightfall to ask "How do I filter for the attacker's IP?"

---

## **💻 Part 1: Environment Setup (15-20 min)**

We highly recommend using **Google Colab** for this course as it requires no local installation.

### **Option 1: Google Colab (Recommended)**
**Best for:** Most students, Chromebooks, Tablets.

#### **Step 1: Get the Course Files**
1.  Download this entire repository from GitHub as a **ZIP file** (Click `Code` -> `Download ZIP`).
2.  Unzip the folder on your computer.

#### **Step 2: Upload to Google Drive**
1.  Go to your **Google Drive**.
2.  Create a folder named `Pandas_Forensics_Course`.
3.  Upload the **unzipped folder** into this new Drive folder.

#### **Step 3: Open the Notebook**
1.  Go to [colab.research.google.com](https://colab.research.google.com).
2.  Click **File > Upload Notebook**.
3.  Select `pandas_lesson.ipynb` locally from the `notebooks/` folder you just extracted. (Or open it directly from Drive if you navigated there).

#### **Step 4: Linking Assets (Google Drive Mount)**
To access the `assets/` folder (for the post-class challenge), you need to mount your Drive.
*   Run the following code in a cell if you need to access files from Drive:
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    # Now you can access files at: /content/drive/My Drive/Pandas_Forensics_Course/...
    ```

---

### **Option 2: Local Setup (VS Code / Jupyter)**
**Best for:** Students relying on privacy/offline access.
**Prerequisites:** Python 3.8+ installed.

1.  Open your terminal and run:
    ```bash
    pip install pandas numpy
    ```
2.  Open VS Code or Jupyter Lab.
3.  Navigate to the `notebooks/` folder and open `pandas_lesson.ipynb`.

---

## **📚 Part 2: What Is Pandas?**
Pandas is the "Excel" of Python. It takes data that might look like a messy pile of lists or dictionaries and organizes it into a clean, tabular format called a **DataFrame**.

### **Why This Matters for Forensics**
*   **Volume:** Excel crashes with 1 million rows. Pandas handles millions of logs in seconds.
*   **Filtering:** Find a specific IP address in a sea of traffic with one line of code.
*   **Correlation:** Automatically link a Process ID (PID) to a Network Connection (Port) to find malware "calling home."

---

## **🧠 Part 3: The Core Concepts**

### **Concept 1: The Series**
*   **Definition:** A one-dimensional labeled array.
*   **Analogy:** A single column in an Excel sheet.
*   **Forensic Example:** A list of all IP addresses connected to a server.

### **Concept 2: The DataFrame**
*   **Definition:** A 2-dimensional structure (rows and columns).
*   **Analogy:** The entire Spreadsheet.
*   **Forensic Example:** A firewall log table containing Timestamp, Source IP, Dest IP, and Port.

---

## **✅ Self-Check**
Before proceeding, ensure you can:
* [ ] Import pandas (`import pandas as pd`).
* [ ] Create a simple Series.
* [ ] Open the `pandas_lesson.ipynb` notebook without errors.
