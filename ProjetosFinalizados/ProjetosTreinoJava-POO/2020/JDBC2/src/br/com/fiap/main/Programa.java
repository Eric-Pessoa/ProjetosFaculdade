package br.com.fiap.main;

import java.sql.SQLException;
import java.util.List;

import br.com.fiap.dao.ProdutoDAO;
import br.com.fiap.model.Produto;

public class Programa {

	public static void main(String[] args) throws SQLException {
		
		Produto p = new Produto();
		p.setNome("trambolho");
		p.setDescricao("Celular até q bom");
		
		ProdutoDAO dao = new ProdutoDAO();
		List<Produto> produtos = dao.getProdutos();
		
		for(Produto z: produtos) {
			System.out.println("ID: " + z.getId());
			System.out.println("NOME: " + z.getNome());
			System.out.println("DESCRICAO: "+ z.getDescricao());
		}
		
		//dao.adiciona(p);
		//dao.altera(p);
		//dao.remove(p);

	}

}
