insert into PRODUCTS values (1,'The Common Path To Uncommon Success','Book',16.99,40);
insert into PRODUCTS values (2,'Tiny Habits','Book',20.39,100);

#session 1

mysql> set autocommit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> lock table PRODUCTS write;
Query OK, 0 rows affected (0.00 sec)

mysql> unlock TABLES;

update PRODUCTS set quantity=quantity+60 where PRODUCT_ID=1;

commit;

#session 2

mysql> set autocommit=0;

mysql> update PRODUCTS set quantity=quantity-2 where PRODUCT_ID=1;

update PRODUCTS set quantity=quantity-2 where PRODUCT_ID=1;

commit;

#session 3

mysql> select * from PRODUCTS;

update PRODUCTS set quantity=quantity-2 where PRODUCT_ID=2;

commit;


# MySQL Workbench

select * from performance_schema.data_locks;

show processlist;

select * from information_schema.processlist;
