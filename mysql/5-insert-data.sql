desc ECOMM_STORE.PRODUCTS_1;

INSERT INTO `ECOMM_STORE`.`PRODUCTS_1`
(`PRODUCT_NAME`,
`PRODUCT_TYPE`,
`PRICE`,
`QUANTITY`)
VALUES
('Deep Work','Book',14.99,100);

INSERT INTO `ECOMM_STORE`.`PRODUCTS_1`
(`PRODUCT_ID`,
`PRODUCT_NAME`,
`PRODUCT_TYPE`,
`PRICE`,
`QUANTITY`)
VALUES
(2,'Digital Minimalism','Book',18.99,150);

INSERT INTO `ECOMM_STORE`.`PRODUCTS_1`
(`PRODUCT_ID`,
`PRODUCT_NAME`,
`PRODUCT_TYPE`,
`PRICE`,
`QUANTITY`)
VALUES
(10,'Art of possibilities','Book',10.99,50);

INSERT INTO `ECOMM_STORE`.`PRODUCTS_1`
(`PRODUCT_NAME`,
`PRODUCT_TYPE`,
`PRICE`,
`QUANTITY`)
VALUES
('Mind at its Home','Book',12.99,100);


TRUNCATE TABLE ECOMM_STORE.PRODUCTS_1;

insert into `ECOMM_STORE`.`PRODUCTS_1` 
SELECT `PRODUCTS_3`.`PRODUCT_ID`,
    `PRODUCTS_3`.`PRODUCT_NAME`,
    `PRODUCTS_3`.`PRODUCT_TYPE`,
    `PRODUCTS_3`.`PRICE`,
    `PRODUCTS_3`.`QUANTITY`
FROM `ECOMM_STORE`.`PRODUCTS_3`;

TRUNCATE TABLE ECOMM_STORE.PRODUCTS_1;

INSERT INTO `ECOMM_STORE`.`PRODUCTS_1`
(`PRODUCT_NAME`,
`PRODUCT_TYPE`,
`PRICE`,
`QUANTITY`)
VALUES
('Deep Work','Book',14.99,100),('Mind at its Home','Book',12.99,100);
