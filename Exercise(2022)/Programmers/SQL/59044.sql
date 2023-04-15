-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT
    i.name,
    i.datetime
FROM
    animal_ins i
LEFT OUTER JOIN
    animal_outs o
    on i.animal_id = o.animal_id
WHERE o.animal_id IS NULL
ORDER BY 2
LIMIT 3
