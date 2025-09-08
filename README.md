# Census 2011 India Dashboard

Streamlit-based data app for analyzing and visualizing India’s Census 2011 at state and district levels.

---

## 📌 Project Overview
This project provides an interactive dashboard built using **Streamlit** to explore Census of India 2011 data at both state and district levels. It enables users to visualize population distribution, literacy rates, and other key demographic statistics across India.

---

## 📂 Project Structure
census-2011-india-dashboard/
├── app.py # Main Streamlit app
├── appv1.py # Alternate / earlier version
├── Final india.csv # Cleaned India-level data
├── india.csv # Raw India-level data
├── india-districts-census-2011.csv # District-level Census data
├── district wise centroids.csv # Centroid coordinates per district
├── state wise centroids_2001.csv # State centroids for 2001
├── state wise centroids_2011.csv # State centroids for 2011
├── district wise population for year 2001 and 2011.csv # Comparative populations
├── india_census_housing-hlpca-full.csv # Housing data for HL/PCA
├── hlpca-colnames.csv # Column names mapping for housing data
├── .idea/ # IDE project settings
└── requirements.txt # Dependency list


---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/ranavikas1998/census-2011-india-dashboard.git
   cd census-2011-india-dashboard
✨ Features

Interactive visualizations showcasing:

State and district-wise population distribution

Literacy rates

Housing and demographic trends

Map-based visualizations using centroid coordinates

Comparison of 2001 vs 2011 census metrics

Easy-to-use UI thanks to Streamlit

🛠️ Tech Stack

Python for data processing and backend logic

Streamlit for building the interactive dashboard

Pandas for data manipulation

Matplotlib / Plotly for visualizations

🔮 Future Enhancements

Enhance visuals using Plotly for richer interactivity

Add filters such as state dropdowns, variable selectors, or timelines

Deploy the app via Streamlit Cloud, Heroku, or similar platforms

Include geospatial maps (choropleth) overlaying district boundaries for better insights

👤 Author

Vikas Rana https://github.com/ranavikas1998
