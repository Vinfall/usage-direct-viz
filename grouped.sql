SELECT
    applicationId,
    sum(timeUsed) AS totalUsage -- Unix timestamp
FROM usageStats
WHERE
    hidden = 0
    AND day > 0 -- epoch day
GROUP BY applicationId
ORDER BY
    totalUsage DESC;