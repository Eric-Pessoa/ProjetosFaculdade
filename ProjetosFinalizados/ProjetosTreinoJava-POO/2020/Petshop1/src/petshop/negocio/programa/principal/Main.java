package petshop.negocio.programa.principal;

import petshop.negocio.aplicacoes.classes.Animal;
import petshop.negocio.aplicacoes.classes.Cliente;
import petshop.negocio.aplicacoes.classes.Funcionario;
import petshop.negocio.aplicacoes.classes.Produto;
import petshop.negocio.aplicacoes.classes.Venda;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		Cliente joao = new Cliente();
		System.out.println(joao.getNome());
		System.out.println(joao.getdinheiroGasto());
		joao.setNome("joao");
		joao.setdinheiroGasto((float) 3000);
		System.out.println(joao.getNome());
		
		Funcionario Joana = new Funcionario();
		System.out.println(Joana.getNome());
		Joana.setNome("Joana");
		System.out.println(Joana.getNome());
		Joana.setGenero("Mulher");
		Joana.setCargo("Gerente");
		Joana.setSalario(1990);
		Joana.setTempoNaEmpresa(12);
		
		Animal papagaio = new Animal();
		System.out.println(papagaio.getRaca());
		System.out.println(papagaio.getPreçoAnimal());
		System.out.println(papagaio.getTipoDeAnimal());
		papagaio.setTipoDeAnimal("Papagaio");
		papagaio.setRaca("Papagaio-do-Congo");
		papagaio.setPreçoAnimal(3000);
		
		Produto racaoDeGato = new Produto();
		racaoDeGato.setNomeProduto("racao boa");
		racaoDeGato.setPreçoProduto(5);
		
		Venda venda1 = new Venda();
		venda1.setCliente(joao);
		venda1.setAnimal(papagaio);
		venda1.setFunc(Joana);
		venda1.setProduto(racaoDeGato);
		
	
		
		
		System.out.println(venda1.getAnimal().getTipoDeAnimal());
		
		
	
	}
	
	
	
	
}
