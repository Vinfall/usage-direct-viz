#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Database schema
# https://codeberg.org/fynngodau/usageDirect/src/branch/main/Application/schemas/godau.fynn.usagedirect.persistence.HistoryDatabase/5.json
# Plotly sunburst
# https://plotly.com/python/sunburst-charts/

import os
import pandas as pd
import sqlite3
import plotly.graph_objects as go
import plotly.io as pio


# Connect to SQLite DB
DB = "usageDirect-history.sqlite3"
conn = sqlite3.connect(DB)
output_dir = "output"


def sql_query(query_file, conn):
    # Read query from file
    with open(query_file, "r") as file:
        query = file.read()

    # Run SQL query and save to DataFrame
    df = pd.read_sql_query(query, conn)

    return df


def generate_sunburst_chart(df):
    data = dict(
        type="sunburst",
        labels=df["applicationId"],
        parents=[""] * len(df),
        values=df["totalUsage"],
    )
    # Create layout
    layout = go.Layout(margin=dict(t=0, l=0, r=0, b=0))

    fig = go.Figure(data=[data], layout=layout)

    output_file = os.path.join(output_dir, "sunburst.html")
    pio.write_html(fig, output_file)


def generate_nested_treemap(df):
    fig = go.Figure(
        go.Treemap(
            labels=df["applicationId"], parents=[""] * len(df), values=df["totalUsage"]
        )
    )

    output_file = os.path.join(output_dir, "nested-treemap.html")
    pio.write_html(fig, output_file)


# print(sql_query("query.sql", conn))
df = sql_query("grouped.sql", conn)
conn.close()


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

generate_sunburst_chart(df)
generate_nested_treemap(df)
