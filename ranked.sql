SELECT
    day,
    timeUsed,
    applicationId,
    dense_rank() OVER (
        ORDER BY
            total_time DESC
    ) AS rank
FROM (
    SELECT
        day,
        timeUsed,
        applicationId,
        sum(timeUsed) OVER (PARTITION BY applicationId) AS total_time
    FROM usageStats
    WHERE
        hidden = 0
        AND day > 0 -- epoch day
) AS t
WHERE applicationId IN (
    SELECT applicationId -- only list top used applicationId -- noqa: RF02
    FROM (
        SELECT
            applicationId,
            sum(timeUsed) AS total_time
        FROM usageStats
        WHERE
            hidden = 0
            AND day > 0
        GROUP BY applicationId
        ORDER BY
            total_time DESC
        LIMIT 10 -- avoid Python ValueError: Invalid property specified for object of type plotly.graph_objs.Scattergl: 'stackgroup' -- noqa: LT05
    ) AS top_rank
)