package br.com;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

import br.com.fiap.factory.ConnectionFactory;

public class TestaRemocao {
	public static void main(String[] args) throws SQLException {
		Connection con = new ConnectionFactory().getConnection();
		//Cria uma query
		Statement stmt = con.createStatement();
		
		stmt.execute("DELETE FROM PRODUTO WHERE ID = 1");
		
		stmt.close();
		con.close();

		
	}


}
