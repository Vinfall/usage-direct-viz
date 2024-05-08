SELECT applicationId,
    SUM(timeUsed) AS totalUsage
FROM usageStats
WHERE hidden = 0
GROUP BY applicationId
ORDER BY totalUsage DESC;