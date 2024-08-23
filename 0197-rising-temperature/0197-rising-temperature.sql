# Write your MySQL query statement below
select w1.id from Weather w1 join Weather w2 on DATE_SUB(w1.recordDate, Interval 1 day) = w2.recordDate where w2.temperature<w1.temperature