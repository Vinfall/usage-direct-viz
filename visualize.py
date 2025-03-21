#!/usr/bin/env python3

# Database schema
# https://codeberg.org/fynngodau/usageDirect/src/branch/main/Application/schemas/godau.fynn.usagedirect.persistence.HistoryDatabase/5.json
# Plotly sunburst: https://plotly.com/python/sunburst-charts/

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas>=2.2.3",
#   "plotly>=5.22.0"
# ]
# ///

import os
import sqlite3

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Connect to SQLite DB
DB = "usageDirect-history.sqlite3"
DB_CONN = sqlite3.connect(DB)
OUTPUT_DIR = "output"


def sql_query(query_file, conn):
    # Read query from file
    with open(query_file, encoding="utf-8") as file:
        query = file.read()

    # Run SQL query and save to DataFrame
    return pd.read_sql_query(query, conn)


def generate_sunburst_chart(df):
    data = {
        "type": "sunburst",
        "labels": df["applicationId"],
        "parents": [""] * len(df),
        "values": df["totalUsage"],
    }
    # Create layout
    layout = go.Layout(margin={"t": 0, "l": 0, "r": 0, "b": 0})

    fig = go.Figure(data=[data], layout=layout)

    output_file = os.path.join(OUTPUT_DIR, "sunburst.html")
    pio.write_html(fig, output_file)


def generate_nested_treemap(df):
    fig = go.Figure(
        go.Treemap(
            labels=df["applicationId"], parents=[""] * len(df), values=df["totalUsage"]
        )
    )

    output_file = os.path.join(OUTPUT_DIR, "nested-treemap.html")
    pio.write_html(fig, output_file)


def generate_stacked_line_chart(df):
    fig = px.line(
        df,
        x="day",
        y="timeUsed",
        title="Stacked Line Chart",
        labels={"day": "Day", "timeUsed": "Time Used"},
        line_group="applicationId",
        color="applicationId",
        line_dash="rank",
    )
    fig.update_traces(mode="lines", legendgroup="one")

    output_file = os.path.join(OUTPUT_DIR, "stacked-line.html")
    pio.write_html(fig, output_file)


df_ranked = sql_query("ranked.sql", DB_CONN)
df_grouped = sql_query("grouped.sql", DB_CONN)
DB_CONN.close()


if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

generate_stacked_line_chart(df_ranked)
generate_sunburst_chart(df_grouped)
generate_nested_treemap(df_grouped)
