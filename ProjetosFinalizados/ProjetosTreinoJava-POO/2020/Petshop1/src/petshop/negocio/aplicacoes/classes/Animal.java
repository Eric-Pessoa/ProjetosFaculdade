package petshop.negocio.aplicacoes.classes;

public class Animal {
	private String tipoDeAnimal;
	private String raca;
	private float pre�oAnimal;
	
	
	public Animal() {
		tipoDeAnimal = "";
		raca = "";
		pre�oAnimal = (float) 0.0;	
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
	public float getPre�oAnimal() {
		return pre�oAnimal;
	}
	public void setPre�oAnimal(float pre�oAnimal) {
		this.pre�oAnimal = pre�oAnimal;
	}

	
}
