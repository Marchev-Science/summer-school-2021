SELECT 
	*
FROM 
	Customers
WHERE
	customeremail LIKE '%.edu' 
    AND countryresidence IS NOT NULL
    AND customerclass NOT IN ('Top','Middle')