package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;

public class TestaAlteracaoClientePF {

	public static void main(String[] args) throws SQLException {
		
		
		Connection con = new ConnectionFactory().getConnection();
		PreparedStatement stmt = con.prepareStatement("UPDATE ClientePF SET NOME = ?, EMAIL = ?, ENDERECO = ?, TELEFONE = ?, CPF = ?, RG = ?, CNH = ? WHERE ID=?");
		stmt.setString(1,"EricPessoa");
		stmt.setString(2,"Pessooo@gmail.com");
		stmt.setString(3,"rua epica");
		stmt.setString(4,"9998-99909");
		stmt.setString(5,"17632925848");
		stmt.setString(6,"787777777");
		stmt.setString(7,"66656");
		stmt.setInt(8, 3);
		stmt.execute();
		System.out.println("Query update executada");
		stmt.close();

	}

}
