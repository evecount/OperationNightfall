# 🕵️‍♀️ Operation Nightfall: Introduction to Pandas for Digital Forensics

Welcome to **Operation Nightfall**. This workshop reimagines the classic "Introduction to Pandas" curriculum through the lens of a Digital Forensics & Incident Response (DFIR) investigation.

Instead of analyzing fruit inventories or exam scores, you will step into the shoes of a **Senior Forensic Analyst**. You have been handed a "disk image" (logs) from a compromised workstation, and your mission is to use Python and Pandas to catch the hacker.

## 🎯 Mission Objectives
By the end of this investigation, you will understand:
*   **The Pandas Library:** How to use the industry-standard data analysis tool for security logs.
*   **Forensic Concepts:** Triage, Baselining, Indicator of Compromise (IoC) hunting, and correlation.

You will be able to:
1.  **Create & Modify Evidence:** Load CSV logs into DataFrames and clean "messy" attacker data.
2.  **Hunt (Indexing & Selection):** Use `.loc`, boolean filtering, and string operations to find "Patient Zero" (malware).
3.  **Correlate (Mapping & Merging):** Join Process logs with Network logs to prove data exfiltration.
4.  **Report (Sorting & Ranking):** Aggregating data to assess the total damage to the organization.

## 📂 Case Files (Course Structure)
Refer to the following sections for your briefing:

- **[Pre-Class](./pre-class.md):** Setting up your forensic lab (Environment Setup).
- **[Operation Nightfall (Lesson)](./notebooks/forensic_investigation.ipynb):** The core investigation workbook.
- **[Sentinel Web App (New!)](./app.py):** The interactive Threat Hunting Console. ([Guide](./sentinel_guide.md))
- **[Post-Class](./post-class.md):** Further reading and practice.
- **[Bonus: The Human Eye](./bonus_manual_forensics.md):** Manual inspection techniques.
- **[Future Vision: The Grid](./future_vision.md):** A proposal for global decentralized defense.
- **[Reference](./reference.md):** Cheat sheets for Pandas commands.

## 🦅 Operation Sentinel (Web App)
Want to run the analysis in a dashboard?
1.  Install requirements: `pip install -r requirements.txt`
2.  Run the app: `streamlit run app.py`
3.  Upload your evidence files.

*Powered by Eve Count | Co-created by Gwendalynn Lim and Gemini*

## ⚠️ Data Safety Warning
This course primarily uses **Synthetic Data** generated securely within the notebook to simulate an attack without risk. 

However, we also provide a sample real-world dataset in `assets/cybercrime-forensic-dataset/` sourced from Kaggle.
> **Analyst Note:** Always verify data sources when downloading from the internet. In the security world, downloading unverified files is a major risk.

---
Project Nightfall (Sentinel): The Open Source Forensic Grid

We believe cybersecurity education shouldn't just be about reading logs; it should be about hunting threats.

This repository houses Operation Nightfall, a complete forensic simulation where students track a hacker's lateral movement using Data Science. It culminates in the deployment of Sentinel, a browser-based Threat Console that allows analysts to visualize attack vectors in 3D and pledge their findings to a decentralized global intelligence grid.

Stack: Python, Pandas, Streamlit, Plotly, Jupyter. Status: Live & Deployed.


