package petshop.negocio.aplicacoes.classes;

public class Produto {
	private String nomeProduto;
	private float preçoProduto;
	
	public Produto() {
		nomeProduto = "";
		preçoProduto = (float) 0.0;	
	}
	
	
	public String getNomeProduto() {
		return nomeProduto;
	}
	public void setNomeProduto(String nomeProduto) {
		this.nomeProduto = nomeProduto;
	}
	public float getPreçoProduto() {
		return preçoProduto;
	}
	public void setPreçoProduto(float preçoProduto) {
		this.preçoProduto = preçoProduto;
	}

}
