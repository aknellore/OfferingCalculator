
# Offering Calculator App

This app helps estimate the 5-year revenue potential of an offering by combining:
1. Customer demand estimation (TAM, SAM, Need %, Capture Rate)
2. Seller readiness and market execution scoring (Kyndryl-specific adjustments)

---

## Structure

- `/customer_only` — Contains the Customer-Only calculator app (Phase 1 & 2)
- `/seller_input` — Will contain Seller Input scoring app (Phase 3)
- `/docs` — Supporting documents, prompts, and explanations

---

## How to Run

1. Clone the repo
2. Install dependencies:
    ```bash
    pip install streamlit openai
    ```
3. Run the app:
    ```bash
    streamlit run customer_only/Offering_Calculator_App.py
    ```

## Requirements

- Streamlit
- OpenAI API Key (add to Replit secrets as `OPENAI_API_KEY`)

