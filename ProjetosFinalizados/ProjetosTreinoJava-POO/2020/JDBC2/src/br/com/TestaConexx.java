package br.com;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import br.com.fiap.factory.ConnectionFactory;

public class TestaConexx {

	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub
		
		//Cria a conexao com o banco
		//Connection con = DriverManager.getConnection("jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL", "RM86405", "070302");
		Connection con = new ConnectionFactory().getConnection();
		//Cria uma query
		Statement stmt = con.createStatement();
		
		//stmt.execute("INSERT INTO PRODUTO (NOME,DESCRICAO) VALUES ('Impressora','Impressora Epson')");
		stmt.execute("SELECT ID, NOME, DESCRICAO FROM PRODUTO");
		
		//pega os dados de retorno
		ResultSet rs = stmt.getResultSet();
		
		//percorrer os dados do rs
		while(rs.next()) {
			int id = rs.getInt("ID");
			String nome = rs.getString("NOME");
			String descricao = rs.getString("DESCRICAO");
			System.out.println("ID: " + id + " NOME: " + nome + " DESCRICAO " + descricao);
		
		
		rs.close();
		stmt.close();
		con.close();
			
			
			
		}

		
		

	}

}
