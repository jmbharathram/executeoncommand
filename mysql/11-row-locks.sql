#session 1

set autocommit=0;

set session transaction isolation level read committed;

update PRODUCTS set quantity=quantity+50 where PRODUCT_ID=1;

commit;

#session 2

set autocommit=0;

set session transaction isolation level read committed;

update PRODUCTS set quantity=quantity-1 where PRODUCT_ID=1;

select * from PRODUCTS;

#session 3

set autocommit=0;

set session transaction isolation level read committed;

update PRODUCTS set quantity=quantity-1 where PRODUCT_ID=2;

# MySQL Workbench

select * from performance_schema.data_locks;

show processlist;

select * from information_schema.processlist;
