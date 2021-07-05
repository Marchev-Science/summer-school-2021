SELECT 
	customerclass,
    COUNT(customerid) AS NrOfCustomers,
    ROUND(AVG(customerage),0) AS AvgAge,
    ROUND(MIN(customerage),0) AS MinAge,
    ROUND(MAX(customerage),0) AS MaxAge,
    COUNT(DISTINCT countryresidence) AS UnqNrOfCountries,
    COUNT(DISTINCT accountmanagerid) AS UnqNrOfManagers
FROM 
	Customers
WHERE
	countryresidence = 'Germany'
GROUP BY
	customerclass
HAVING
	AvgAge < 45
ORDER BY 
	customerclass DESC