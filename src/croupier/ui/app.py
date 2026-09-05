import streamlit as st
import pandas as pd

from croupier.strats import BasicStrategy, Strategy
from croupier.simulation import run_simulation

STRATEGY_OPTIONS = {
    BasicStrategy: "Basic (stop at 17)"
}

st.set_page_config(page_title="Croupier", page_icon=":material/playing_cards:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

# DEFAULT DF
if 'results_df' not in st.session_state:
    st.session_state["results_df"] = pd.read_csv('default_data/simulation_results.csv')

# RUN SIMULATION
@st.cache_data
def load_simulation_data(iterations: int, strategy: Strategy, dealer_stand_threshold: int = 17) -> pd.DataFrame:
    df = run_simulation(iterations=iterations, strategy=strategy, dealer_stand_threshold=dealer_stand_threshold)
    return df

# SIDEBAR
with st.sidebar:
    st.title("Simulation Options")

    strategy = st.selectbox(
        label="Strategy",
        placeholder="Select an strategy",
        accept_new_options=False,
        options=STRATEGY_OPTIONS,
        format_func=lambda x: STRATEGY_OPTIONS.get(x, "N/A")
    )

    iterations = st.slider(
        label="Iterations",
        min_value=0,
        max_value=500000,
        step=1,
        value=500000
    )

    with st.expander(label="Advanced Options", type="compact"):
        dealer_stand_threshold = st.slider(
            label="Dealer Stand Threshold",
            min_value=0,
            max_value=21,
            step=1,
            value=17
        )

    if st.button(label="Run simulation", width="stretch"):
        with st.spinner(text="Dealing cards..."):
            st.session_state['results_df'] = load_simulation_data(iterations=iterations, strategy=strategy, dealer_stand_threshold=dealer_stand_threshold)
        st.toast("Simulation completed successfully!")

# RESULTS STATS 

st.title("Croupier")
st.subheader("Here are some of your simulation stats: ")

col_strat, col_iter, col_deal = st.columns(3)
col_strat.metric(label="Strategy", value=STRATEGY_OPTIONS.get(strategy, 'N/A'), border=True)
col_iter.metric(label="Iterations", value=iterations, border=True)
col_deal.metric(label="Dealer stand threshold", value=dealer_stand_threshold, border=True)