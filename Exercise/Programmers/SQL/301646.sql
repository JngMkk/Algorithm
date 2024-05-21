SELECT
    COUNT(*) AS COUNT
FROM
    ECOLI_DATA
WHERE
    -- 0010(2)와 AND 비트연산해서 0 -> 2번 형질을 가지지 않아야 함
    (GENOTYPE & 2) = 0
    AND
    -- 0101(2)와 AND 비트연산해서 1이상 -> 1번 혹은 3번 형질을 가졌다는 것
    (GENOTYPE & 5) > 0
;
