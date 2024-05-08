SELECT applicationId,
    SUM(timeUsed) AS totalUsage -- Unix timestamp
FROM usageStats
WHERE hidden = 0
GROUP BY applicationId
ORDER BY totalUsage DESC;