select *
from cleaning_data c;

WITH RFM_Base 
AS
(
  SELECT c.ID AS ID,
    c.Recency AS Recency_Value,
   (c.Num_Deals_Purchases + c.Num_Catalog_Purchases + c.Num_Store_Purchases + c.Num_Web_Purchases) as Frequency_Value,
    (c.Liquor + c.Vegetables + c.Pork + c.Seafood + c.Candy + c.Jewellery) AS Monetary_Value
  FROM cleaning_data c
)
, RFM_Score 
AS
(
  SELECT *,
    NTILE(5) OVER (ORDER BY Recency_Value DESC) as R_Score,
    NTILE(5) OVER (ORDER BY Frequency_Value ASC) as F_Score,
    NTILE(5) OVER (ORDER BY Monetary_Value ASC) as M_Score
  FROM RFM_Base
)
,RFM_Final
AS
(
SELECT *,
  CONCAT(R_Score, F_Score, M_Score) as RFM_Overall
FROM RFM_Score
)
SELECT f.*, s.Segment
FROM RFM_Final f
JOIN segment_scores s ON f.RFM_Overall = s.Scores