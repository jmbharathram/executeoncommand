#session 1
set autocommit=0;
start transaction;
drop table ECOMM_STORE.t1;
create table ECOMM_STORE.t1 ( c1 int primary key);
insert into ECOMM_STORE.t1 values (1);
commit;

update ECOMM_STORE.t1 set c1 = 2 where c1 = 1;


#session 2
set session transaction isolation level read committed;
show variables like '%isolation%';
select * from ECOMM_STORE.t1;

show session variables like '%isolation%';
set session transaction isolation level read uncommitted;
show session variables like '%isolation%';
select * from ECOMM_STORE.t1;

set session transaction isolation level repeatable read;
show variables like '%isolation%';
select * from ECOMM_STORE.t1;

set session transaction isolation level serializable;
show session variables like '%isolation%';
select * from ECOMM_STORE.t1;
