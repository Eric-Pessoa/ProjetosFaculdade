package br.com;


import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.Produto;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TestaInsercParametros {

	public static void main(String[] args) throws SQLException {
		
		Produto p = new Produto();
		p.setNome("TV");
		p.setDescricao("TV mt boa");
		
		Connection con = new ConnectionFactory().getConnection();
		

		PreparedStatement stmt = con.prepareStatement("INSERT INTO PRODUTO (NOME,DESCRICAO) VALUES (?,?)");
		stmt.setString(1,p.getNome());
		stmt.setString(2, p.getDescricao());
		stmt.execute();
		
		System.out.println("Query executada");
		
		stmt.close();
		con.close();
	}

}
