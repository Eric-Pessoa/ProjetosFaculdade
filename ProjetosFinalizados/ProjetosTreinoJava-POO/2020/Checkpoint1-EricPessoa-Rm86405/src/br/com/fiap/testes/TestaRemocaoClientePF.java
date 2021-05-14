package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;

public class TestaRemocaoClientePF {

	public static void main(String[] args) throws SQLException {
		
		Connection con = new ConnectionFactory().getConnection();
		PreparedStatement stmt = con.prepareStatement("DELETE FROM ClientePF WHERE ID=1");
		stmt.execute();
		System.out.println("Query delete executada");
		stmt.close();
		con.close();

	}

}
