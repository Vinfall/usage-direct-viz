SELECT day,
    timeUsed,
    applicationId
FROM usageStats
WHERE hidden = 0
    AND day > 0 -- epoch day