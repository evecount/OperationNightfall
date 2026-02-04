
import streamlit as st
import pandas as pd
import plotly.express as px

# === CONFIGURATION ===
st.set_page_config(
    page_title="Sentinel | Operation Nightfall",
    page_icon="🦅",
    layout="wide"
)

# === HEADER & SPONSORSHIP ===
st.title("🦅 Sentinel: Forensic Threat Console")
st.markdown("**Powered by Eve Count | Co-created by Gwendalynn Lim and Gemini**")
st.markdown("---")

# === SIDEBAR: FILE UPLOAD ===
# === SIDEBAR: FILE UPLOAD ===
st.sidebar.header("📂 Case Evidence")
uploaded_file = st.sidebar.file_uploader("Upload Network/Process Logs (CSV)", type=["csv"])

st.sidebar.markdown("---")

# === SIDEBAR: GLOBAL GRID ===
st.sidebar.header("🌍 Contribute to Grid")
st.sidebar.markdown("Join the decentralized forensic network.")
repo_url = st.sidebar.text_input("GitHub Repo URL", placeholder="https://github.com/username/repo")
asset_path = st.sidebar.text_input("CSV Asset Path", placeholder="data/attack_vector.csv")

if st.sidebar.button("📝 Sign Petition & Transmit"):
    if repo_url and asset_path:
        st.sidebar.success("✅ Contribution Registered to Grid Petition.")
        st.sidebar.info("Acknowledgement: You have successfully validated using Sentinel and pledged your analysis to the decentralized stream.")
    else:
        st.sidebar.error("⚠️ Please provide both Repo URL and Asset Path.")

st.sidebar.markdown("---")

# === SIDEBAR: SPONSORSHIP ===
st.sidebar.header("❤️ Sponsor the Grid")
st.sidebar.markdown("""
**Sentinel is currently running in Local Mode.**
To build the real-time **Cloud Backend** for the Global Grid, we need server resources.
""")
if st.sidebar.button("💸 Fund the Backend"):
    st.sidebar.balloons()
    st.sidebar.success("Thank you for your interest! Contact **Eve Count** to sponsor the infrastructure.")

# === APP LOGIC ===
if uploaded_file is not None:
    # 1. LOAD DATA
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"Evidence Loaded: {uploaded_file.name} ({len(df)} rows)")
        
        # Check for Timestamp and convert
        time_col = None
        for col in df.columns:
            if 'Time' in col or 'Timestamp' in col:
                time_col = col
                df[time_col] = pd.to_datetime(df[time_col])
                break
        
        if not time_col:
            st.warning("⚠️ No Timestamp column found. Timeline analysis disabled.")

        # === TAB 1: TRIAGE (AUTO-HUNT) ===
        st.subheader("🔬 Triage & Auto-Hunt")
        
        col1, col2, col3 = st.columns(3)
        
        # Metric 1: Volume
        col1.metric("Total Events", len(df))
        
        # Metric 2: Unique Entities
        if 'Process_Name' in df.columns:
            unique_procs = df['Process_Name'].nunique()
            col2.metric("Unique Processes", unique_procs)
            
            # SUSPICIOUS HUNT
            suspicious_list = ['nmap', 'powershell', 'mimikatz', 'cmd', 'netcat']
            # Clean and check
            df['clean_proc'] = df['Process_Name'].astype(str).str.lower().str.strip()
            hits = df[df['clean_proc'].str.contains('|'.join(suspicious_list), na=False)]
            
            if not hits.empty:
                col3.metric("🚨 Threat Hits", len(hits), delta="-CRITICAL")
                st.error(f"⚠️ DETECTED SUSPICIOUS PROCESSES: {hits['clean_proc'].unique()}")
                st.dataframe(hits.head(10))
            else:
                col3.metric("Threat Hits", 0, delta="Safe")
                st.info("No known bad binaries detected in top-level triage.")

        elif 'Destination_Port' in df.columns:
            # Network Mode
            unique_ips = df['Destination_IP'].nunique()
            col2.metric("Unique Destination IPs", unique_ips)
            
            high_port_traffic = df[df['Destination_Port'] > 1024]
            col3.metric("High Port Traffic", len(high_port_traffic))

        # === TAB 2: VISUALIZATION (THE THREAT CONSOLE) ===
        st.markdown("---")
        st.subheader("📊 Threat Hunting Console")
        
        # Controls
        c1, c2, c3 = st.columns(3)
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        # Smart Defaults
        default_x = time_col if time_col else df.columns[0]
        default_y = 'Destination_Port' if 'Destination_Port' in df.columns else (numeric_cols[0] if numeric_cols else df.columns[1])
        default_color = 'Protocol' if 'Protocol' in df.columns else ('Process_Name' if 'Process_Name' in df.columns else None)
        
        x_axis = c1.selectbox("X-Axis", options=df.columns, index=df.columns.get_loc(default_x))
        y_axis = c2.selectbox("Y-Axis", options=df.columns, index=df.columns.get_loc(default_y))
        color_by = c3.selectbox("Color By (Z-Axis)", options=df.columns, index=df.columns.get_loc(default_color) if default_color else 0)
        
        # Plot
        if st.checkbox("Show 3D Scatter (Time vs Y vs Color)", value=False):
             fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=color_by, color=color_by, title="3D Attack Vector Analysis")
        else:
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_by, hover_data=df.columns, title="2D Attack Vector Analysis")
            
        st.plotly_chart(fig, use_container_width=True)
        
        # === AI BRIDGE ===
        st.info("""
        **🤖 The AI Bridge:**
        What you see above as "clusters" or "lines" are what Machine Learning models use to detect attacks:
        *   **Vertical Lines:** Often indicate Scanning (Same Time, Many Ports).
        *   **Dense Clusters:** Often indicate Brute Force or Exfiltration.
        """)

    except Exception as e:
        st.error(f"Error parsing file: {e}")

else:
    # LANDING PAGE
    st.info("👋 Welcome to Sentinel. Please upload `process_log.csv` or `network_log.csv` to begin.")
    
    st.markdown("""
    ### Features
    *   **Auto-Triage:** Instantly flags `nmap`, `powershell`, and `mimikatz`.
    *   **Vector Analysis:** Interactive Plotly dashboard for time-series forensics.
    *   **AI-Ready:** Visualizes the patterns that ML models look for.
    """)
