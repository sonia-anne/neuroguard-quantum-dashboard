import streamlit as st
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="NeuroGuard Quantum Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Custom dark theme override
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    .css-18ni7ap {
        background-color: #0d1117;
    }
    .block-container {
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🧠 NeuroGuard Quantum Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Visual Comparative Analysis of NeuroGuard vs Traditional Brain Cancer Therapies</h3>", unsafe_allow_html=True)
st.markdown("---")

# Section 1: Comparative Bar Chart
st.subheader("Comparative Treatment Performance Metrics")

treatments = ['Surgery', 'Chemotherapy', 'CAR-T', 'Oncolytic Viruses', 'NeuroGuard']
effectiveness = [30, 22, 18, 25, 89]
non_recurrence = [30, 22, 20, 26, 89]
regeneration = [5, 2, 1, 3, 95]
speed = [70, 79, 75, 86, 97]  # Inverted days for intuitive score

fig = go.Figure()
fig.add_trace(go.Bar(x=treatments, y=effectiveness, name='Effectiveness (%)', marker_color='#1f77b4'))
fig.add_trace(go.Bar(x=treatments, y=non_recurrence, name='Non-Recurrence (%)', marker_color='#2ca02c'))
fig.add_trace(go.Bar(x=treatments, y=regeneration, name='Regeneration Capability', marker_color='#d62728'))
fig.add_trace(go.Bar(x=treatments, y=speed, name='Response Speed', marker_color='#9467bd'))

fig.update_layout(
    barmode='group',
    template='plotly_dark',
    title="NeuroGuard vs. Traditional Therapies",
    xaxis_title="Treatment Type",
    yaxis_title="Performance Score",
    legend_title="Metric",
    height=550
)

st.plotly_chart(fig, use_container_width=True)

# Section 2: Donut Chart - NeuroGuard Component Breakdown
st.subheader("NeuroGuard System Architecture Breakdown")

components = ['AI Core', 'Nanobots', 'Oncolytic Viruses', 'CRISPR Editing', '3D Bioprinting', 'EM Fields']
distribution = [20, 25, 15, 15, 15, 10]

fig_donut = go.Figure(data=[go.Pie(
    labels=components,
    values=distribution,
    hole=.5,
    textinfo='label+percent',
    marker=dict(colors=[
        '#58a6ff', '#00ff7f', '#ffcc00', '#ff66cc', '#ff8c69', '#87ceeb'
    ])
)])

fig_donut.update_layout(
    title="Distribution of Functional Modules in NeuroGuard",
    annotations=[dict(text='NeuroGuard', x=0.5, y=0.5, font_size=18, showarrow=False)],
    template='plotly_dark',
    height=500
)

st.plotly_chart(fig_donut, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>© 2025 NeuroGuard Project – Designed by Annette for the UNESCO-Al Fozan Prize</p>", unsafe_allow_html=True)
