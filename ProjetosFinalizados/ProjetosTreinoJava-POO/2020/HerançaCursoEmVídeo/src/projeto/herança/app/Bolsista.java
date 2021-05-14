package projeto.herança.app;

//Exemplo de como é impossível criar uma subclasse pra aluno, já que ela é uma classe final.

public class Bolsista extends Aluno {
	
	private double bolsa;

	public double getBolsa() {
		return bolsa;
	}

	public void setBolsa(double bolsa) {
		this.bolsa = bolsa;
	}
	
	public void renovarBolsa() {
		System.out.println("Bolsa renovada");
	}
	
	
	//Exemplo de como tentar sobrepor um método final dá erro
	
	@Override
	public void pagarMensalidade() {
		System.out.println("Não paga mensalidade.");
	}

}
