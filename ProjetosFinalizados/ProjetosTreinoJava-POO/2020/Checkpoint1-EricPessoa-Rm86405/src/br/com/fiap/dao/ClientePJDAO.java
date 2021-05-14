package br.com.fiap.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.ClientePJ;

public class ClientePJDAO {
	
	//atributo
	
			private Connection con;
			
			
			
			//construtor
			
			public ClientePJDAO() throws SQLException{
				 con = new ConnectionFactory().getConnection();
				
			}
			
			//adiciona
			
			public void adiciona(ClientePJ p) throws SQLException {
				
				PreparedStatement stmt = con.prepareStatement("INSERT INTO CLIENTEPJ (NOME,EMAIL,TELEFONE,ENDEREÇO,CNPJ) VALUES (?,?,?,?,?)");
				stmt.setString(1,p.getNome());
				stmt.setString(2,p.getEmail());
				stmt.setString(3,p.getTelefone());
				stmt.setString(4,p.getEndereco());
				stmt.setString(5,p.getCnpj());
				
				System.out.println("Query adiciona executada");
				
				stmt.close();
				
			}
			
			// remove
			
			public void remove (ClientePJ p) throws SQLException {
				
				PreparedStatement stmt = con.prepareStatement("DELETE FROM ClientePJ WHERE ID=?");
				stmt.setInt(1, p.getId());
				stmt.execute();
				System.out.println("Query delete executada");
				stmt.close();
				
				
				
				
			}
			
			
			//altera
			
			public void altera (ClientePJ p) throws SQLException {
				
				PreparedStatement stmt = con.prepareStatement("UPDATE ClientePJ SET NOME = ?, EMAIL = ?, TELEFONE = ?, ENDERECO = ?, CNPJ = ? WHERE ID = ?");
				stmt.setString(1, p.getNome());
				stmt.setString(2,p.getEmail());
				stmt.setString(3,p.getTelefone());
				stmt.setString(4,p.getEndereco());
				stmt.setString(5,p.getCnpj());
				stmt.setInt(6, p.getId());
				stmt.execute();
				System.out.println("Query update executada");
				stmt.close();
				
				
			}

			
			// busca
			
			public List<ClientePJ> getClientePJ() throws SQLException{
				
				ArrayList<ClientePJ> Clientes = new ArrayList<ClientePJ>();
					
				
				PreparedStatement stmt = con.prepareStatement("SELECT * FROM ClientePJ");
				stmt.execute();
				ResultSet rs = stmt.getResultSet();
				
				while(rs.next()) {
					ClientePJ p = new ClientePJ();
					p.setId(rs.getInt("ID"));
					p.setNome(rs.getString("NOME"));
					p.setEmail(rs.getString("EMAIL"));
					p.setTelefone(rs.getString("TELEFONE"));
					p.setEndereco(rs.getString("ENDERECO"));
					p.setCnpj(rs.getString("CNPJ"));
					
					Clientes.add(p);
				
				}
				
				return Clientes;
				
				
			}
			

}
