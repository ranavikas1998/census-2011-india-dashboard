import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("Final india.csv")

# Sidebar options
list_of_states = list(df["State"].unique())
list_of_states.insert(0, "Overall India")

st.sidebar.title("India Data Dashboard")

selected_state = st.sidebar.selectbox("Select State", list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[5:]))

view_option = st.sidebar.radio("View Mode", ["Show All Charts", "Tabs View"])

plot = st.sidebar.button("Generate Charts")

if plot:
    if selected_state == "Overall India":
        state_df = df.copy()
    else:
        state_df = df[df['State'] == selected_state]

    st.subheader(f"Analysis for: {selected_state}")

    # Define charts (reusable)
    def get_map():
        return px.scatter_mapbox(
            state_df, lat="Latitude", lon="Longitude",
            size=primary, color=secondary, zoom=3,
            size_max=35, mapbox_style="carto-positron",
            width=1200, height=600, hover_name="District"
        )

    def get_bar():
        top10 = state_df.nlargest(10, primary)
        return px.bar(
            top10, x=primary, y="District", orientation="h",
            color=secondary, title=f"Top 10 Districts by {primary}"
        )

    def get_tree():
        return px.treemap(
            state_df, path=["State", "District"], values=primary,
            color=secondary, color_continuous_scale="Viridis",
            title=f"Treemap of {selected_state}"
        )

    # --- OPTION 1: Show All Charts Together ---
    if view_option == "Show All Charts":
        st.markdown("### 🌍 Map Visualization")
        st.plotly_chart(get_map(), use_container_width=True)

        st.markdown("### 📊 Top 10 Districts (Bar Chart)")
        st.plotly_chart(get_bar(), use_container_width=True)

        st.markdown("### 🌳 Treemap")
        st.plotly_chart(get_tree(), use_container_width=True)

    # --- OPTION 2: Show in Tabs ---
    else:
        tab1, tab2, tab3 = st.tabs(["🌍 Map", "📊 Bar Chart", "🌳 Treemap"])

        with tab1:
            st.markdown("### 🌍 Map Visualization")
            st.plotly_chart(get_map(), use_container_width=True)

        with tab2:
            st.markdown("### 📊 Top 10 Districts (Bar Chart)")
            st.plotly_chart(get_bar(), use_container_width=True)

        with tab3:
            st.markdown("### 🌳 Treemap")
            st.plotly_chart(get_tree(), use_container_width=True)
