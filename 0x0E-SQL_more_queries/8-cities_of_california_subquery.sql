-- list cities in california that can be found in list
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name="California") 
ORDER BY id ASC;
