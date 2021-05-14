package projeto.automovel.aplicacao;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Automovel Nissan = new Automovel();
		Nissan.ano = "2002";
		Nissan.cor = "prata";
		Nissan.modelo = "Nissan";
		Nissan.placa = "abc-123";
		
		Cliente joao = new Cliente();
		joao.nome = "joao";
		joao.sexo = "homem";
		joao.carro = Nissan;
		
		Funcionario Zé = new Funcionario();
		Zé.nomeFuncionario = "Zé";
		Zé.credenciaisFuncionario = "Habilitação ABC";
		
		Servico Servico3 = new Servico();
		Servico3.tipoServiço = "manutencao";
		Servico3.nomeServiço = "TrocaDeOleo";
		Servico3.precoServiço = 3000;
		Servico3.funcionario = Zé;
		Servico3.cliente = joao;
		
		
		
		System.out.println(joao.carro.cor);
		
		System.out.println(Servico3.cliente.nome);
		
		
		//Não coloquei construtores, mas eu iniciaria com os construtores padrão.
		
		
		
		

		
		
		
		
		
	}

}
