package petshop.negocio.aplicacoes.classes;

public class Cliente {
	private String nome;
	private float dinheiroGasto;
	
	public Cliente() {
		nome = "";
		dinheiroGasto = (float) 0.0;		
	}
	
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public float getdinheiroGasto() {
		return dinheiroGasto;
	}
	public void setdinheiroGasto(float dinheiroGasto) {
		this.dinheiroGasto = dinheiroGasto;
	}
	
	
	
	
} 

