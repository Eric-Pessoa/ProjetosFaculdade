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
		
		Funcionario Z� = new Funcionario();
		Z�.nomeFuncionario = "Z�";
		Z�.credenciaisFuncionario = "Habilita��o ABC";
		
		Servico Servico3 = new Servico();
		Servico3.tipoServi�o = "manutencao";
		Servico3.nomeServi�o = "TrocaDeOleo";
		Servico3.precoServi�o = 3000;
		Servico3.funcionario = Z�;
		Servico3.cliente = joao;
		
		
		
		System.out.println(joao.carro.cor);
		
		System.out.println(Servico3.cliente.nome);
		
		
		//N�o coloquei construtores, mas eu iniciaria com os construtores padr�o.
		
		
		
		

		
		
		
		
		
	}

}
