-- https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true

-- 내 풀이
SELECT
    MIN(doctor), MIN(professor), MIN(singer), MIN(actor)
FROM
    (
    SELECT
        CASE WHEN occupation = "doctor" THEN name END AS doctor,
        CASE WHEN occupation = "professor" THEN name END AS professor,
        CASE WHEN occupation = "singer" THEN name END AS singer,
        CASE WHEN occupation = "actor" THEN name END AS actor,
        ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS rnk
    FROM
        occupations
    ) r
GROUP BY rnk
;



-- 다른 사람 풀이
SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT
    MIN(doctor), MIN(professor), MIN(singer), MIN(actor)
FROM
    (
    SELECT
        CASE
            WHEN occupation = "doctor" THEN (@r1:=@r1+1)
            WHEN occupation = "professor" THEN (@r2:=@r2+1)
            WHEN occupation = "singer" THEN (@r3:=r3+1)
            WHEN occupation = "actor" THEN (@r4:=r4+1)
        END AS rnk,
        CASE WHEN occupation = "doctor" THEN name END AS doctor,
        CASE WHEN occupation = "professor" THEN name END AS professor,
        CASE WHEN occupation = "singer" THEN name END AS singer,
        CASE WHEN occupation = "actor" THEN name END AS actor
    FROM
        occupations
    ) r
GROUP BY rnk
;
