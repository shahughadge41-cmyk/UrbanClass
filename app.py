import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="UrbanCool AI Dashboard", layout="wide")

# --- SIDEBAR ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Indian_Space_Research_Organisation_Logo.svg", width=100)
st.sidebar.title("EcoHeat AI Dashboard")
menu = st.sidebar.radio("NAVIGATION MENU", ["🔴 1. Identify Hotspots", "📊 2. Driver Analysis", "🎮 3. Cooling Simulator", "🛰️ 4. Satellite Data Feed"])

# --- DATA MAPPING ---
city_metrics = {
    "Mumbai": {"temp": 43.8, "air": 36.2, "wards": 4, "lat": [19.076, 19.082], "lon": [72.877, 72.885], "base": 34.0, "factor": 0.07},
    "Bengaluru": {"temp": 38.5, "air": 32.1, "wards": 3, "lat": [12.971, 12.982], "lon": [77.594, 77.610], "base": 29.5, "factor": 0.12},
    "Delhi": {"temp": 45.2, "air": 38.0, "wards": 6, "lat": [28.613, 28.625], "lon": [77.209, 77.220], "base": 38.0, "factor": 0.09}
}

# --- LOGIC ---
if menu == "🔴 1. Identify Hotspots":
    city = st.selectbox("Select City", list(city_metrics.keys()))
    data = city_metrics[city]
    c1, c2, c3 = st.columns(3)
    c1.metric("Peak Surface Temp", f"{data['temp']}°C")
    c2.metric("Ambient Air Temp", f"{data['air']}°C")
    c3.metric("High-Risk Wards", data['wards'])
    st.map(pd.DataFrame({'lat': data['lat'], 'lon': data['lon']}))

elif menu == "📊 2. Driver Analysis":
    st.title("Urban Heat Attribution")
    df = pd.DataFrame({"Factor": ["Concrete", "Albedo", "Vegetation", "Waste Heat"], "Impact": [4.2, 2.1, 3.5, 1.2]})
    st.bar_chart(df.set_index("Factor"))

elif menu == "🎮 3. Cooling Simulator":
    city = st.selectbox("Select City for Simulation", list(city_metrics.keys()))
    data = city_metrics[city]
    st.info(f"📍 {city} का बेस तापमान: {data['base']}°C")
    g = st.slider("Greening (%)", 0, 100, 10)
    r = st.slider("Cool Roofs (%)", 0, 100, 15)
    w = st.slider("Water Bodies (%)", 0, 50, 5)
    reduction = (g * data['factor']) + (r * 0.05) + (w * 0.15)
    st.success(f"Projected Cooling Impact: -{reduction:.1f}°C")
    st.progress(min(int(reduction * 10), 100))

elif menu == "🛰️ 4. Satellite Data Feed":
    st.title("🛰️ Live Satellite Data Pipelines")
    df_data = pd.DataFrame({
        "Product": ["Landsat 8", "Sentinel-2", "ECOSTRESS", "ERA5"],
        "Resolution": ["100m", "10m", "70m", "25km"],
        "Status": ["Active", "Active", "Syncing", "Active"]
    })
    st.table(df_data)
    st.line_chart(np.random.randn(10, 2))