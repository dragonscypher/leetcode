# Write your MySQL query statement below
select round((count(if(order_date = customer_pref_delivery_date, customer_id, null))*100)/count(*),2) immediate_percentage  from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);
