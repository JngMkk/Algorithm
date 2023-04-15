-- https://school.programmers.co.kr/learn/courses/30/lessons/77487
WITH
tmp AS (
    SELECT host_id
    FROM places
    GROUP BY host_id
    HAVING COUNT(1) > 1
)
SELECT *
FROM places
WHERE host_id IN (SELECT * FROM tmp)
