-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

-- 나의 풀이
SELECT
    n,
    CASE
        WHEN p IS NULL THEN 'Root'
        WHEN n IN (SELECT DISTINCT p FROM bst) THEN 'Inner'
        ELSE 'Leaf'
    END AS node
FROM
    bst
ORDER BY
    1
;



-- 다른 사람 풀이 (테이블이 커질 시 더 효율적으로 동작)
SELECT
    n,
    IF(p IS NULL, 'Root', IF((SELECT COUNT(*) FROM bst WHERE p = tmp.n) > 0, 'Inner', 'Leaf'))
FROM
    bst AS tmp
ORDER BY
    1
;
