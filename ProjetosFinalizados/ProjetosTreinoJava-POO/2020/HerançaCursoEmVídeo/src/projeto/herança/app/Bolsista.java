package projeto.heran�a.app;

//Exemplo de como � imposs�vel criar uma subclasse pra aluno, j� que ela � uma classe final.

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
	
	
	//Exemplo de como tentar sobrepor um m�todo final d� erro
	
	@Override
	public void pagarMensalidade() {
		System.out.println("N�o paga mensalidade.");
	}

}
