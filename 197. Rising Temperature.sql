--197. Rising Temperature

-- Solution 1
# Write your MySQL query statement below
-- Select w1.id
-- from Weather AS w1 , Weather AS w2
-- WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate , w2.recordDate) = 1

-- Solution 2
SELECT W1.id as Id
FROM Weather W1
INNER JOIN Weather W2
WHERE W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY) 
AND W1.temperature > W2.temperature
