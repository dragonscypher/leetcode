# Write your MySQL query statement below
select query_name,round(avg(rating/position),2) quality, 
round(avg(IF(rating < 3, 1, 0))*100, 2)poor_query_percentage from Queries 
where query_name is not null group by query_name
