package com.postgresqlexample;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectDB {
	
	private final String url = "jdbc:postgresql://aa.bbb.ccc.dd/postgres?sslmode=require&sslcert=/root/.postgresql/postgresql.crt&sslkey=/root/.postgresql/postgresql.pk8&sslrootcert=/root/.postgresql/root.crt&sslpassword=<password>";

    private final String user = "postgres";
    private final String password = "password";

    /**
     * Connect to the PostgreSQL database
     *
     * @return a Connection object
     */
    public Connection connect() {
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("Connected to the PostgreSQL server successfully.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;
    }

	public static void main(String[] args) {
		
		ConnectDB db = new ConnectDB();
		db.connect();

	}

}
