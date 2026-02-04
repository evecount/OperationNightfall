# 🛠️ The Sentinel Tech Stack

**"Why these tools?"**

In `forensic_investigation.ipynb`, we used **Jupyter** for exploration. For **Sentinel**, we use **Streamlit** for deployment.

---

## **1. Streamlit (The Web Framework)**
*   **What it is:** A Python library that turns data scripts into shareable web apps in minutes.
*   **Why we use it:**
    *   **No HTML/CSS/JS required:** We write pure Python.
    *   **Rapid Prototyping:** Perfect for building internal tools like a Forensic Dashboard.
    *   **Interactive:** Native support for checkboxes, dropdowns, and file uploaders.

## **2. Plotly (The Visualization Engine)**
*   **What it is:** A graphing library that makes interactive, publication-quality graphs.
*   **Why we use it:**
    *   **Interactive:** Unlike `matplotlib` (static images), Plotly allows you to **Zoom**, **Pan**, and **Hover** to see details on specific data points (e.g., hovering over a dot to see the Source IP).
    *   **3D Support:** Excellent for complex vector analysis (Time vs Port vs Density).

---

## **How IT Fits Together**
1.  **Pandas:** Loads and filters the logs (The Engine).
2.  **Plotly:** Draws the interactive chart (The Display).
3.  **Streamlit:** Puts it all on a webpage (The Interface).
