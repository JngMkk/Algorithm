-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
SELECT h24, COUNT(time) AS cnt
FROM (SELECT CONVERT(DATE_FORMAT(datetime, '%H'), UNSIGNED) AS time
        FROM animal_outs
    ) t1
RIGHT OUTER JOIN (SELECT (@h := @h + 1) h24 FROM animal_outs, (SELECT @h := -1) m LIMIT 24) t2
ON t1.time = t2.h24
GROUP BY h24
ORDER BY 1
