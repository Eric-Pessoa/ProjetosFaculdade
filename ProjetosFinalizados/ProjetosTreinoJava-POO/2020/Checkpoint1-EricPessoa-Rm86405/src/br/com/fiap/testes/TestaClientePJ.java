package br.com.fiap.testes;
import br.com.fiap.model.*;

public class TestaClientePJ {

	public static void main(String[] args) {
		
		ClientePJ teste = new ClientePJ();
		
		teste.setNome("jubileu");
		teste.setCnpj("23333444");
		teste.setEmail("pessoa.eric@gmail.com");
		teste.setEndereco("rua 000");
		teste.setTelefone("33323232");
		
		System.out.println(teste.getCnpj());
		System.out.println(teste.getEmail());
		System.out.println(teste.getEndereco());
		System.out.println(teste.getNome());
		System.out.println(teste.getTelefone());
	}

}
