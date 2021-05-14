package br.com.fiap.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.ClientePF;

public class ClientePFDAO {
	
	//atributo
	
		private Connection con;
		
		
		
		//construtor
		
		public ClientePFDAO() throws SQLException{
			 con = new ConnectionFactory().getConnection();
			
		}
		
		//adiciona
		
		public void adiciona(ClientePF p) throws SQLException {
			
			PreparedStatement stmt = con.prepareStatement("INSERT INTO CLIENTEPF (NOME,EMAIL,TELEFONE,ENDEREÇO,CPF,RG,CNH) VALUES (?,?,?,?,?,?,?)");
			stmt.setString(1,p.getNome());
			stmt.setString(2,p.getEmail());
			stmt.setString(3,p.getTelefone());
			stmt.setString(4,p.getEndereco());
			stmt.setString(5,p.getCpf());
			stmt.setString(6,p.getRg());
			stmt.setString(7,p.getCnh());
			
			System.out.println("Query adiciona executada");
			
			stmt.close();
			
		}
		
		// remove
		
		public void remove (ClientePF p) throws SQLException {
			
			PreparedStatement stmt = con.prepareStatement("DELETE FROM ClientePF WHERE ID=?");
			stmt.setInt(1, p.getId());
			stmt.execute();
			System.out.println("Query delete executada");
			stmt.close();
			
			
			
			
		}
		
		
		//altera
		
		public void altera (ClientePF p) throws SQLException {
			
			PreparedStatement stmt = con.prepareStatement("UPDATE ClientePF SET NOME = ?, EMAIL = ?, TELEFONE = ?, ENDERECO = ?, CPF = ?, RG = ?, CNH = ? WHERE ID=?");
			stmt.setString(1, p.getNome());
			stmt.setString(2,p.getEmail());
			stmt.setString(3,p.getTelefone());
			stmt.setString(4,p.getEndereco());
			stmt.setString(5,p.getCpf());
			stmt.setString(6,p.getRg());
			stmt.setString(7,p.getCnh());
			stmt.setInt(8, p.getId());
			stmt.execute();
			System.out.println("Query update executada");
			stmt.close();
			
			
		}

		
		// busca
		
		public List<ClientePF> getClientePF() throws SQLException{
			
			ArrayList<ClientePF> Clientes = new ArrayList<ClientePF>();
				
			
			PreparedStatement stmt = con.prepareStatement("SELECT * FROM ClientePF");
			stmt.execute();
			ResultSet rs = stmt.getResultSet();
			
			while(rs.next()) {
				ClientePF p = new ClientePF();
				p.setId(rs.getInt("ID"));
				p.setNome(rs.getString("NOME"));
				p.setEmail(rs.getString("EMAIL"));
				p.setTelefone(rs.getString("TELEFONE"));
				p.setEndereco(rs.getString("ENDERECO"));
				p.setCpf(rs.getString("CPF"));
				p.setRg(rs.getString("RG"));
				p.setCnh(rs.getString("CNH"));
				
				Clientes.add(p);
			
			}
			
			return Clientes;
			
			
		}
		


}
