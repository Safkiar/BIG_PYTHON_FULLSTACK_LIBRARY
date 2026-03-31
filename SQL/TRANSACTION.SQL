-- SAVE ONLY WHEN ALL OPERATIONS SUCCED 

BEGIN TRANSACTION;

-- everything is correct

COMMIT;

-- Error

ROLLBACK;



------------------------
ACID 

ATOMICITY - wszystko albo nic 
CONSISTENCY - nie łamie własnych reguł
ISOLATION - oddziela od siebie transakcje 
DURABILITY - po commit jest zapisane