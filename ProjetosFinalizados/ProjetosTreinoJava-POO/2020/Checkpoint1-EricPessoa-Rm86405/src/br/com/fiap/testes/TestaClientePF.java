package br.com.fiap.testes;

import br.com.fiap.model.ClientePF;

public class TestaClientePF {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ClientePF teste = new ClientePF();
		
		teste.setEmail("pessoa.eric@gmail.com");
		teste.setEndereco("rua 000");
		teste.setTelefone("33323232");
		teste.setNome("jubileu");
		teste.setCnh("333333");
		teste.setCpf("32323");
		teste.setRg("2333");
		
		System.out.println(teste.getEmail());
		System.out.println(teste.getEndereco());
		System.out.println(teste.getNome());
		System.out.println(teste.getTelefone());
		System.out.println(teste.getCnh());
		System.out.println(teste.getCpf());
		System.out.println(teste.getRg());



	}

}
