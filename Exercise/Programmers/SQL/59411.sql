-- https://school.programmers.co.kr/learn/courses/30/lessons/59411
SELECT
    i.animal_id,
    i.name
FROM
    animal_ins i
JOIN
    animal_outs o
ON
    i.animal_id = o.animal_id
ORDER BY
    DATEDIFF(o.datetime, i.datetime) DESC
LIMIT 2
