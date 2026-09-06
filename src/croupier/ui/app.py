import streamlit as st
import pandas as pd
import plotly.express as px

from croupier.strats import BasicStrategy, Strategy
from croupier.simulation import run_simulation

STRATEGY_OPTIONS = {
    BasicStrategy: "Basic (stop at 17)"
}

st.set_page_config(page_title="Croupier", page_icon=":material/playing_cards:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

# DEFAULT DF
if 'results_df' not in st.session_state:
    df = pd.read_csv('default_data/simulation_results.csv')

    df['result'] = df['result'].astype(str).str.replace('Result.', '')
    df['is_win'] = (df['result'] == 'win').astype(int)

    st.session_state["results_df"] = df

# RUN SIMULATION
@st.cache_data
def load_simulation_data(iterations: int, strategy: Strategy, dealer_stand_threshold: int = 17) -> pd.DataFrame:
    df = run_simulation(
        iterations=iterations,
        strategy=strategy(),
        dealer_stand_threshold=dealer_stand_threshold
    )

    df['result'] = df['result'].astype(str).str.replace('Result.', '')
    df['is_win'] = (df['result'] == 'win').astype(int)

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
        st.rerun()

# RESULTS STATS 

st.title("Croupier")
st.subheader("Here are some of your simulation stats: ")

# SIM INFO

col_strat, col_iter, col_deal = st.columns(3)
col_strat.metric(label="Strategy", value=STRATEGY_OPTIONS.get(strategy, 'N/A'), border=True)
col_iter.metric(label="Iterations", value=iterations, border=True)
col_deal.metric(label="Dealer stand threshold", value=dealer_stand_threshold, border=True)

st.subheader("Charts:")

df_current = st.session_state["results_df"]
col_rates, col_bust = st.columns(2)

# WIN RATES

win_rates = df_current['result'].value_counts(normalize=True)

fig1 = px.bar(
    x=win_rates.index, 
    y=win_rates.values,
    title="Results Distribution (Win/Loss/Draw)",
    labels={'x': 'Result', 'y': 'Percentage (%)'},
    color=win_rates.index,
    color_discrete_map={'win': '#2ecc71', 'loss': '#e74c3c', 'draw': '#95a5a6'}
)

col_rates.plotly_chart(fig1)

# BUSTS

bust_rate = df_current['player_bust'].value_counts(normalize=True)

fig2 = px.pie(
    names=["No Bust", "Bust"],
    values=bust_rate.values,
    title="Bust Distribution",
    color=['no_bust', 'bust'],
    color_discrete_map={'bust': '#e74c3c', 'no_bust': '#2ecc71'}
)

col_bust.plotly_chart(fig2)

# HEATMAP

heatmap_data = df_current.pivot_table(
    index='player_initial_score',
    columns='dealer_upcard_value',
    values='is_win',
    aggfunc='mean'
)

fig3 = px.imshow(
    heatmap_data,
    title="Win Rate vs Dealer Upcard Heatmap",
    labels=dict(x="Dealer Upcard", y="Player Hand", color="Win Rate"),
    color_continuous_scale='RdYlGn',
    origin='lower',
    aspect='auto'
)

st.plotly_chart(fig3, width='stretch')

# EXPORT 

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

st.download_button(
    label="Download CSV",
    data=convert_for_download(df_current),
    file_name="croupier_data.csv",
    mime="text/csv",
    icon=":material/download:",
)