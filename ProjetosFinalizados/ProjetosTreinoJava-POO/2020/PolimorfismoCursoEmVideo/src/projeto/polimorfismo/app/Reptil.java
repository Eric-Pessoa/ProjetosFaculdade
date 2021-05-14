package projeto.polimorfismo.app;

public class Reptil extends Animal {
	
	public String corEscama;
	

	public String getCorEscama() {
		return corEscama;
	}

	public void setCorEscama(String corEscama) {
		this.corEscama = corEscama;
	}

	@Override
	public void locomover() {
		System.out.println("Lagatixa andante");
	}

	@Override
	public void alimentar() {
		System.out.println("nhom nhom nhom");
	}

	@Override
	public void emitirSom() {
		System.out.println("AAAAAAAAAAAAAAAAAAAAAAAAAA");
	}
	
	public void esconder() {
		System.out.println("Modo camuflado on");
	}
	
	
	
		

}
