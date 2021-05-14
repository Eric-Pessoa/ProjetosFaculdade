package petshop.negocio.aplicacoes.classes;

public class Animal {
	private String tipoDeAnimal;
	private String raca;
	private float preçoAnimal;
	
	
	public Animal() {
		tipoDeAnimal = "";
		raca = "";
		preçoAnimal = (float) 0.0;	
	}
	
	public String getTipoDeAnimal() {
		return tipoDeAnimal;
	}
	public void setTipoDeAnimal(String tipoDeAnimal) {
		this.tipoDeAnimal = tipoDeAnimal;
	}
	public String getRaca() {
		return raca;
	}
	public void setRaca(String raca) {
		this.raca = raca;
	}
	public float getPreçoAnimal() {
		return preçoAnimal;
	}
	public void setPreçoAnimal(float preçoAnimal) {
		this.preçoAnimal = preçoAnimal;
	}

	
}
