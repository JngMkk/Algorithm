-- https://school.programmers.co.kr/learn/courses/30/lessons/59045
WITH
tmp AS (
    SELECT animal_id, sex_upon_intake
    FROM animal_ins
    WHERE sex_upon_intake LIKE "I%"
)
SELECT o.animal_id, animal_type, name
FROM animal_outs o
JOIN tmp t ON o.animal_id = t.animal_id
WHERE o.sex_upon_outcome != t.sex_upon_intake
ORDER BY 1
