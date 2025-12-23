1️⃣ Table Creation
CREATE TABLE customer_churn (
    customer_id VARCHAR(50),
    gender VARCHAR(10),
    senior_citizen INT,
    tenure INT,
    contract VARCHAR(50),
    payment_method VARCHAR(50),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(12,2),
    churn VARCHAR(5)
);

2️⃣ Overall Churn Rate
SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_percentage
FROM customer_churn;

3️⃣ Churn by Contract Type
SELECT 
    contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_churn
GROUP BY contract
ORDER BY churn_rate DESC;

4️⃣ High-Risk Customers (Target Segment)
SELECT *
FROM customer_churn
WHERE churn = 'Yes'
AND tenure < 12
AND monthly_charges > 70;
