package projeto.herança.app;

// essa classe é folha, final. Não tem como ela gerar filhos.

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
	
	//exemplo de método final, ou seja, não pode ser dado override nele.
	
	public final void pagarMensalidade() {
		System.out.println("Mensalidade paga.");
	}
	

}
