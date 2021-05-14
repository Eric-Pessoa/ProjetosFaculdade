package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;

public class TestaAlteracaoClientePJ {

	public static void main(String[] args) throws SQLException {
		
		Connection con = new ConnectionFactory().getConnection();
		PreparedStatement stmt = con.prepareStatement("UPDATE ClientePJ SET NOME = ?, EMAIL = ?, ENDERECO = ?, TELEFONE = ?, CNPJ = ? WHERE ID=?");
		stmt.setString(1,"EricPessoa");
		stmt.setString(2,"Pessooo@gmail.com");
		stmt.setString(3,"rua epica");
		stmt.setString(4,"9998-99909");
		stmt.setString(5,"17632925848");
		stmt.setInt(6, 2);
		stmt.execute();
		System.out.println("Query update executada");
		stmt.close();

	}

}
