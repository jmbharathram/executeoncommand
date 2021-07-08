#Session 1

update PRODUCTS set quantity=quantity+25 where product_id=1;

#Session 2

update PRODUCTS set price=price+2 where product_id=2;

update PRODUCTS set price=price+2 where product_id=1;

#Session 1

update PRODUCTS set quantity=quantity+10 where product_id=2;
#ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
