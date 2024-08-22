# Write your MySQL query statement below
select p.product_name,s1.year,s1.price from Sales s1 left join Product p on s1.product_id = p.product_id;