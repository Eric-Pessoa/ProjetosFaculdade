package petshop.negocio.aplicacoes.classes;

public class Produto {
	private String nomeProduto;
	private float pre�oProduto;
	
	public Produto() {
		nomeProduto = "";
		pre�oProduto = (float) 0.0;	
	}
	
	
	public String getNomeProduto() {
		return nomeProduto;
	}
	public void setNomeProduto(String nomeProduto) {
		this.nomeProduto = nomeProduto;
	}
	public float getPre�oProduto() {
		return pre�oProduto;
	}
	public void setPre�oProduto(float pre�oProduto) {
		this.pre�oProduto = pre�oProduto;
	}

}
