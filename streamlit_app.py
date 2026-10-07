import os
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Customer Data Dashboard",
    page_icon=":material/group:",
    layout="wide",
)

conn = st.connection("snowflake")

TABLE = "TASTY_BYTES_DBT_DB.RAW.SELECT_CUSTOMER_DATA"


@st.cache_data(ttl=600)
def load_customers() -> pd.DataFrame:
    df = conn.query(f"SELECT FIRST_NAME, LAST_NAME, RECORD_SOURCE FROM {TABLE}")
    df.columns = df.columns.str.lower()
    return df


def render_page_header(title: str):
    with st.container(
        horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"
    ):
        st.markdown(title)
        if st.button(":material/restart_alt: Reset", type="tertiary"):
            st.session_state.clear()
            st.rerun()


render_page_header("# Customer Data Dashboard")

try:
    df = load_customers()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.info(
        "Make sure your Snowflake connection is configured in "
        "`.streamlit/secrets.toml` or via environment variables."
    )
    st.stop()

# --- Filters ---
with st.popover("Filters", type="tertiary"):
    sources = df["record_source"].unique().tolist()
    selected_sources = st.multiselect("Record Source", sources, default=sources)
    search_name = st.text_input("Search by name")

filtered = df[df["record_source"].isin(selected_sources)]
if search_name:
    mask = (
        filtered["first_name"].str.contains(search_name, case=False, na=False)
        | filtered["last_name"].str.contains(search_name, case=False, na=False)
    )
    filtered = filtered[mask]

# --- KPI Cards ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(filtered))
col2.metric("Distinct First Names", filtered["first_name"].nunique())
col3.metric("Record Sources", filtered["record_source"].nunique())

st.divider()

# --- Charts ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Customers by Last Name Initial")
    last_init = filtered["last_name"].str[0].value_counts().reset_index()
    last_init.columns = ["initial", "count"]
    last_init = last_init.sort_values("count", ascending=False)
    chart = (
        alt.Chart(last_init)
        .mark_bar()
        .encode(
            x=alt.X("initial:N", sort="-y", title="Last Name Initial"),
            y=alt.Y("count:Q", title="Count"),
            tooltip=["initial", "count"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

with chart_col2:
    st.subheader("Most Common First Names")
    name_counts = filtered["first_name"].value_counts().head(10).reset_index()
    name_counts.columns = ["first_name", "count"]
    chart = (
        alt.Chart(name_counts)
        .mark_bar()
        .encode(
            x=alt.X("count:Q", title="Count"),
            y=alt.Y("first_name:N", sort="-x", title="First Name"),
            tooltip=["first_name", "count"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

st.divider()

# --- Data Table ---
st.subheader("Customer Records")
st.dataframe(
    filtered.sort_values(["last_name", "first_name"]).reset_index(drop=True),
    use_container_width=True,
    height=400,
)
