
import streamlit as st
import openai

# Set your OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Offering Calculator - Customer-Only Tab")

# Tabs
tab1, tab2 = st.tabs(["Customer-Only", "Seller Input (Coming Soon)"])

with tab1:
    # Offering Input
    offering_title = st.text_input("Offering Title")
    offering_description = st.text_area("Offering Description (optional but the more specific the better)")

    if st.button("Analyze Offering"):
        with st.spinner("AI analyzing offering..."):
            # Prompt for AI
            prompt = (
                f"Estimate TAM (in $B), SAM % of TAM, Need % of SAM, and Capture Rate % for the following offering.\n"
                f"Offering Title: {offering_title}\n"
                f"Description: {offering_description}\n"
                "Provide the answer as:\n"
                "1. TAM (in $B):\n"
                "2. SAM % of TAM:\n"
                "3. Need % of SAM:\n"
                "4. Capture Rate %:\n"
                "Give short reasoning for each."
            )

            # OpenAI API Call
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a market sizing assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            result = response['choices'][0]['message']['content']
            st.write("### AI Reasoning & Suggested Values")
            st.write(result)

            # Example static extracted values (manually entered for now)
            tam_suggested = 20  # in $B
            sam_percent_suggested = 15
            need_percent_suggested = 35
            capture_rate_suggested = 1

            # Human-in-the-loop sliders
            st.write("### Adjust Suggested Values")
            tam_actual = st.slider("Adjust TAM ($B)", 1, 100, tam_suggested)
            sam_percent_actual = st.slider("Adjust SAM %", 1, 100, sam_percent_suggested)
            need_percent_actual = st.slider("Adjust Need %", 1, 100, need_percent_suggested)
            capture_rate_actual = st.slider("Adjust Capture Rate %", 0, 10, capture_rate_suggested)

            # Calculations
            sam_value = tam_actual * (sam_percent_actual / 100)
            nao_value = sam_value * (need_percent_actual / 100)
            rev_potential = nao_value * (capture_rate_actual / 100)

            st.write(f"**Calculated SAM:** ${sam_value:.1f}B")
            st.write(f"**Need-Aligned Opportunity:** ${nao_value:.1f}B")
            st.write(f"**5-Year Revenue Potential:** ${rev_potential:.1f}B")

with tab2:
    st.info("Seller Input Scoring will be implemented in the next phase.")
