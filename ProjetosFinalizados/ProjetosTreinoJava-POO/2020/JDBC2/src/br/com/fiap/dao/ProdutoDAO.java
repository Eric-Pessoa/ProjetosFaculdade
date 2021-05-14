package br.com.fiap.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import br.com.fiap.factory.ConnectionFactory;
import br.com.fiap.model.Produto;

public class ProdutoDAO {
	
	//atributo
	
	private Connection con;
	
	
	
	//construtor
	
	public ProdutoDAO() throws SQLException{
		 con = new ConnectionFactory().getConnection();
		
	}
	
	//adiciona
	
	public void adiciona(Produto p) throws SQLException {
		
		PreparedStatement stmt = con.prepareStatement("INSERT INTO PRODUTO (NOME,DESCRICAO) VALUES (?,?)");
		stmt.setString(1,p.getNome());
		stmt.setString(2, p.getDescricao());
		stmt.execute();
		
		System.out.println("Query adiciona executada");
		
		stmt.close();
		
	}
	
	// remove
	
	public void remove (Produto p) throws SQLException {
		
		PreparedStatement stmt = con.prepareStatement("DELETE FROM PRODUTO WHERE ID=?");
		stmt.setInt(1, p.getId());
		stmt.execute();
		System.out.println("Query delete executada");
		stmt.close();
		
		
		
		
	}
	
	
	//altera
	
	public void altera (Produto p) throws SQLException {
		
		PreparedStatement stmt = con.prepareStatement("UPDATE PRODUTO SET NOME = ?, DESCRICAO = ? WHERE ID=?");
		stmt.setString(1, p.getNome());
		stmt.setString(2, p.getDescricao());
		stmt.setInt(3,p.getId());
		stmt.execute();
		System.out.println("Query update executada");
		stmt.close();
		
		
		
	}

	
	// busca
	
	public List<Produto> getProdutos() throws SQLException{
		
		ArrayList<Produto> Produtos = new ArrayList<Produto>();
			
		
		PreparedStatement stmt = con.prepareStatement("SELECT * FROM PRODUTO");
		stmt.execute();
		ResultSet rs = stmt.getResultSet();
		
		while(rs.next()) {
			Produto produto = new Produto();
			produto.setId(rs.getInt("ID"));
			produto.setNome(rs.getString("NOME"));
			produto.setDescricao(rs.getString("DESCRICAO"));
			
			Produtos.add(produto);
		
		}
		
		return Produtos;
		
		
	}
	

}
