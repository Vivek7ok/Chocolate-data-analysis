-- Which chocolate products generate the highest revenue, and how do they rank by profit margin?
select 
p.product_name ,
round(sum(s.revenue),0) as total_revenue,
round(sum(s.profit),0) as toal_profit,
round(sum((s.profit/s.revenue)*100),0) as profit_margin
from products as p
left join sales as s
on p.product_id = s.product_id
group by p.product_name
order by total_revenue desc;

-- What are the monthly/quarterly sales trends — are there seasonal peaks (e.g., Valentine's Day, Christmas)?
with cte as 
(select 
case
when MONTH(order_date) = 2 AND DAY(order_date) = 14 then "Valentine's"
when MONTH(order_date) = 12 AND DAY(order_date) = 25 then "Christmas"
when MONTH(order_date) = 3 AND DAY(order_date) = 10 then 'Normal day'
end as Fuction_days,
revenue ,
profit ,
profit/revenue as profit_margin
from sales)
select 
Fuction_days,
round(sum(revenue),0) as total_revenue,
round(sum(profit),0) as total_profit,
round(sum(profit_margin),0) as total_profit_margin
from cte
group by Fuction_days;

-- Which sales category are consistently over/underperforming ?
WITH product_data AS (
    SELECT 
        p.product_id,
        p.category,
        s.revenue
    FROM products p
    JOIN sales s 
        ON p.product_id = s.product_id
),
category_avg AS (
    SELECT 
        p.category,
        AVG(s.revenue) AS category_avg
    FROM products p
    JOIN sales s 
        ON p.product_id = s.product_id
    GROUP BY p.category
)
SELECT 
    pd.product_id,
    pd.category,
    AVG(pd.revenue) AS product_avg,
    CASE 
        WHEN AVG(pd.revenue) > ca.category_avg THEN 'over_performing'
        ELSE 'under_performing'
    END AS performance
FROM product_data pd
JOIN category_avg ca 
    ON pd.category = ca.category
GROUP BY pd.product_id, pd.category, ca.category_avg;

-- . Which customer segments (retail, wholesale, online) contribute the most to total revenue?
select 
s1.store_type,
round((sum(s2.revenue) / sum(sum(s2.revenue)) over() * 100),0) as contribution
from stores as s1
left join sales as s2
on s1.store_id = s2.store_id
group by store_type;

-- What is the average order value per customer, and how has it changed over time
with cte as 
(select 
c.customer_id,
s.order_id,
sum(s.revenue) as total_rev,
year(s.order_date) as year
from customers as c
left join sales as s
on c.customer_id = s.customer_id
group by s.order_id ,c.customer_id,year(s.order_date))
select 
customer_id,
year,
avg(total_rev)
from cte
group by customer_id ,year
order by year desc;
