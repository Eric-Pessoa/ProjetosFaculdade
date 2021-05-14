package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;

public class TestaListagemClientePJ {

	public static void main(String[] args) throws SQLException {

		Connection con = new ConnectionFactory().getConnection();
		
		PreparedStatement stmt = con.prepareStatement("SELECT * FROM CLIENTEPJ");
		stmt.execute();
		
		ResultSet rs = stmt.getResultSet();
		
		while (rs.next()) {
			int id = rs.getInt("ID");
			String nome = rs.getString("NOME");
			String email =  rs.getString("EMAIL");
			String endereco =  rs.getString("ENDERECO");
			String telefone =  rs.getString("TELEFONE");
			String cnpj =  rs.getString("CNPJ");

			

			System.out.println("ID: " + id);
			System.out.println("NOME: " + nome);
			System.out.println("EMAIL: "+ email);
			System.out.println("ENDEREÇO: "+ endereco);
			System.out.println("TELEFONE: "+ telefone);
			System.out.println("CNPJ: "+ cnpj);
	
			}
		
		rs.close();
		stmt.close();
		con.close();
		
			
		}
		
		
	}


