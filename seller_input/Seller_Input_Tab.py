
import streamlit as st

# Seller Input Scoring Tab

st.title("Seller Input Scoring")

# Inputs
st.write("### Seller Readiness & Market Execution Scoring")
seller_readiness = st.slider("Seller Readiness (1 - Low, 5 - High)", 1, 5, 3)
win_rate_potential = st.slider("Win Rate Potential (1 - Low, 5 - High)", 1, 5, 3)
deal_size_potential = st.slider("Deal Size Potential (1 - Low, 5 - High)", 1, 5, 3)
client_footprint = st.slider("Client Footprint (1 - Low, 5 - High)", 1, 5, 3)
cross_sell_potential = st.slider("Cross-Sell Penetration (1 - Low, 5 - High)", 1, 5, 3)

# Calculations based on your earlier Replit app scoring logic
bottom_up_score = (seller_readiness + win_rate_potential + deal_size_potential) / 3
installed_base_score = (client_footprint + cross_sell_potential) / 2
combined_score = (bottom_up_score * 0.6) + (installed_base_score * 0.4)

# Right-sizing assumptions
if combined_score >= 4:
    share_adjustment = 0.8
    confidence = "High"
elif combined_score >= 3:
    share_adjustment = 0.5
    confidence = "Medium"
else:
    share_adjustment = 0.2
    confidence = "Low"

# Placeholder for imported 5-Year Revenue Potential from Customer Tab
st.write("#### Baseline 5-Year Revenue Potential (from Customer Tab)")
baseline_revenue = st.number_input("Input baseline 5-Year Revenue Potential ($M)", min_value=0, value=100)

# Adjusted Potential
adjusted_revenue = baseline_revenue * share_adjustment

# Outputs
st.write(f"### Combined Score: {combined_score:.1f}")
st.write(f"### Confidence Level: {confidence}")
st.write(f"### Adjusted 5-Year Revenue Potential: ${adjusted_revenue:.1f}M")
