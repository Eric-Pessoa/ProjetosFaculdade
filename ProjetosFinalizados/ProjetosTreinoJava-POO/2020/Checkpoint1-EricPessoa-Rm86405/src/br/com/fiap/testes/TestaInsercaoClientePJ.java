package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.ClientePJ;

public class TestaInsercaoClientePJ {

	public static void main(String[] args) throws SQLException {
		ClientePJ p = new ClientePJ();
		p.setNome("eric");
		p.setEmail("pessoa.eric@gmail.com");
		p.setEndereco("rua oba");
		p.setTelefone("2323232");
		p.setCnpj("333333");

		Connection con = new ConnectionFactory().getConnection();
		

		PreparedStatement stmt = con.prepareStatement("INSERT INTO CLIENTEPJ (NOME,EMAIL,ENDERECO,TELEFONE,CNPJ) VALUES (?,?,?,?,?)");
		stmt.setString(1,p.getNome());
		stmt.setString(2,p.getEmail());
		stmt.setString(3,p.getEndereco());
		stmt.setString(4,p.getTelefone());
		stmt.setString(5,p.getCnpj());

		stmt.execute();
		
		System.out.println("Query executada");
		
		stmt.close();
		con.close();

	}


	}


