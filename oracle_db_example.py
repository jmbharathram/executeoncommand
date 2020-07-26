import cx_Oracle
#import click

#@click.command()
#@click.argument('sql')
def main():
    sql="select file#, name from v$datafile"
    db_user = "test_user"
    db_pass = "xx#"
    dbun = "db"
    db_dsn = cx_Oracle.makedsn("host", 1521, service_name=dbun)
    #print(db_dsn)
    conn = cx_Oracle.connect(db_user, db_pass, dsn=db_dsn) #mode=cx_Oracle.SYSDBA
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)



main()
