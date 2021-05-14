package petshop.negocio.aplicacoes.classes;

public class Funcionario {
	private String nome;
	private String genero;
	private String cargo;
	private float salario;
	private int tempoNaEmpresa;
	
	public Funcionario () {
		nome = "";
		genero = "";
		cargo = "";
		salario = (float) 0.0;
		tempoNaEmpresa = 0;	
	}
	
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String gênero) {
		this.genero = gênero;
	}
	public String getCargo() {
		return cargo;
	}
	public void setCargo(String cargo) {
		this.cargo = cargo;
	}
	public float getSalario() {
		return salario;
	}
	public void setSalario(float salário) {
		this.salario = salário;
	}
	public int getTempoNaEmpresa() {
		return tempoNaEmpresa;
	}
	public void setTempoNaEmpresa(int tempoNaEmpresa) {
		this.tempoNaEmpresa = tempoNaEmpresa;
	}
}

