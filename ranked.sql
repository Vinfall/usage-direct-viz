SELECT day,
    timeUsed,
    applicationId
FROM usageStats
WHERE hidden = 0
    AND day > 0 -- epoch day
    AND applicationId IN (
        SELECT applicationId -- only list top used applicationId
        FROM (
                SELECT applicationId,
                    SUM(timeUsed) as total_time
                FROM usageStats
                WHERE hidden = 0
                    AND day > 0
                GROUP BY applicationId
                ORDER BY total_time DESC
                LIMIT 10 -- avoid Python ValueError: Invalid property specified for object of type plotly.graph_objs.Scattergl: 'stackgroup'
            ) AS top_rank
    )