-- https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true

SELECT
    CONCAT(name, "(", LEFT(occupation, 1), ")") AS name
FROM
    occupations
ORDER BY
    1
;
SELECT
    CONCAT("There are a total of ", COUNT(occupation), " ", LOWER(occupation), "s.") AS s
FROM
    occupations
GROUP BY
    occupation
ORDER BY
    COUNT(occupation), s
;
