SELECT 
	* ,
    CASE 
    	WHEN portfoliopositionsid = 15 THEN "Cash"
     -- WHEN condition2 THEN result 2
    	ELSE 'Other'
    END AS PositionName
FROM 
	PortfolioAmounts 