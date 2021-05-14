package projeto.polimorfismo.app;

public class Mamifero extends Animal{
	
	private String corPelo;
	
	
	
	public String getCorPelo() {
		return corPelo;
	}

	public void setCorPelo(String corPelo) {
		this.corPelo = corPelo;
	}

	@Override
	public void locomover() {
		
		System.out.println("Andando nas 4 patas");
		
	}

	@Override
	public void alimentar() {
		System.out.println("SLurp slurp");
		
	}

	@Override
	public void emitirSom() {
		System.out.println("AUAU");
		
	}
	
	
	

}
