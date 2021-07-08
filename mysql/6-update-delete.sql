USE ECOMM_STORE;

select * from PRODUCTS;

UPDATE PRODUCTS 
SET 
    quantity = quantity + 50
WHERE
    product_id = 1;
    
commit;
    
select * from PRODUCTS;

UPDATE PRODUCTS 
SET 
    quantity = quantity + 50
WHERE
    product_id in (1,2,3);
    
commit;
    
select * from PRODUCTS;
    
UPDATE PRODUCTS 
SET quantity = CASE
    WHEN product_id = 1 THEN quantity + 50
    WHEN product_id = 2 THEN quantity + 100
    ELSE 100
    END
WHERE
    product_id in (1,2,3);
    
commit;
    
select * from PRODUCTS;

DELETE FROM PRODUCTS 
WHERE PRODUCT_ID = 3;

commit;

select * from PRODUCTS;

select * from PRODUCTS_3;

DELETE FROM PRODUCTS_3
WHERE quantity < 10;

select * from PRODUCTS_3;

DELETE FROM PRODUCTS_3
LIMIT 10;

commit;

select * from PRODUCTS_3;

DELETE FROM PRODUCTS_3
ORDER BY PRODUCT_ID
LIMIT 10;

COMMIT;
