SELECT
	CustomerID, 
    CountryResidence,
    CustomerAge
FROM
	Customers
ORDER BY
	Countryresidence ASC,
    Customerage DESC;
    
SELECT
	customerid,
    amountposition
FROM
	PortfolioAmounts
ORDER BY
	amountposition DESC
LIMIT 10
    