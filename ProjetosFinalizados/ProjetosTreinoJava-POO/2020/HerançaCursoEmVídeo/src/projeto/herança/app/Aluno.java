package projeto.heran�a.app;

// essa classe � folha, final. N�o tem como ela gerar filhos.

public  class Aluno extends Pessoa {
	
	private int matricula;
	private String curso;
	
	
	public int getMatricula() {
		return matricula;
	}
	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}
	public String getCurso() {
		return curso;
	}
	public void setCurso(String curso) {
		this.curso = curso;
	}
	
	//exemplo de m�todo final, ou seja, n�o pode ser dado override nele.
	
	public final void pagarMensalidade() {
		System.out.println("Mensalidade paga.");
	}
	

}
