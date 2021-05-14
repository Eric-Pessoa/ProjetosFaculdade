package br.com.fiap.testes;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.*;

public class TestaInsercaoClientePF {

	public static void main(String[] args) throws SQLException {
		
		ClientePF p = new ClientePF();
		p.setNome("eric");
		p.setCnh("232323");
		p.setCpf("45258819806");
		p.setEmail("pessoa.eric@gmail.com");
		p.setEndereco("rua oba");
		p.setRg("605055415");
		p.setTelefone("2323232");

		Connection con = new ConnectionFactory().getConnection();
		

		PreparedStatement stmt = con.prepareStatement("INSERT INTO CLIENTEPF (NOME,EMAIL,TELEFONE,ENDEREÇO,CPF,RG,CNH) VALUES (?,?,?,?,?,?,?)");
		stmt.setString(1,p.getNome());
		stmt.setString(2,p.getEmail());
		stmt.setString(3,p.getTelefone());
		stmt.setString(4,p.getEndereco());
		stmt.setString(5,p.getCpf());
		stmt.setString(6,p.getRg());
		stmt.setString(7,p.getCnh());


		
		stmt.execute();
		
		System.out.println("Query executada");
		
		stmt.close();
		con.close();

	}

}
