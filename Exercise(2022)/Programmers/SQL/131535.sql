-- https://school.programmers.co.kr/learn/courses/30/lessons/131535

SELECT
    COUNT(*) AS users
FROM
    user_info
WHERE
    age BETWEEN 20 AND 29
    AND
    YEAR(joined) = 2021
;
