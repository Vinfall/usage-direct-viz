#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3
import plotly.express as px

# Connect to SQLite DB
DB = "usageDirect-history.sqlite3"
conn = sqlite3.connect(DB)


def sql_query(query_file, conn):
    # Read query from file
    with open(query_file, "r") as file:
        query = file.read()

    # Run SQL query and save to DataFrame
    df = pd.read_sql_query(query, conn)

    return df


# print(sql_query("query.sql", conn))
df = sql_query("grouped.sql", conn)

conn.close()

fig = px.sunburst(df, path=["applicationId"], values="totalUsage")
fig.show()
