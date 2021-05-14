package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;

public class TestaListagemClientePF {

	public static void main(String[] args) throws SQLException {
		

		Connection con = new ConnectionFactory().getConnection();
		
		PreparedStatement stmt = con.prepareStatement("SELECT * FROM CLIENTEPF");
		stmt.execute();
		
		ResultSet rs = stmt.getResultSet();
		
		while (rs.next()) {
			int id = rs.getInt("ID");
			String nome = rs.getString("NOME");
			String email =  rs.getString("EMAIL");
			String endereco =  rs.getString("ENDERECO");
			String telefone =  rs.getString("TELEFONE");
			String cpf =  rs.getString("CPF");
			String rg =  rs.getString("RG");
			String cnh =  rs.getString("CNH");

			

			System.out.println("ID: " + id);
			System.out.println("NOME: " + nome);
			System.out.println("EMAIL: "+ email);
			System.out.println("ENDERE�O: "+ endereco);
			System.out.println("TELEFONE: "+ telefone);
			System.out.println("CPF: "+ cpf);
			System.out.println("RG: "+ rg);
			System.out.println("CNH: "+ cnh);
	
			}
		
		rs.close();
		stmt.close();
		con.close();
		
			
		}
		
		
		

	}


