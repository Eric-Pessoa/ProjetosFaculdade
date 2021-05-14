package projeto.emoji.app;

public class Lutador implements LutadorInterface {
	private String nome;
	private String nacionalidade;
	private int idade;
	private double altura;
	private double peso;
	private String categoria;
	private int vitorias;
	private int derrotas; 
	private int empates;
	
	
	//Construtor
	
	public Lutador(String nome, String nacionalidade, int idade, double altura, double peso,
			int vitorias, int derrotas, int empates) {
		this.nome = nome;
		this.nacionalidade = nacionalidade;
		this.idade = idade;
		this.altura = altura;
		this.setPeso(peso);
		this.vitorias = vitorias;
		this.derrotas = derrotas;
		this.empates = empates;
	}
	
	
	//Getters e setters
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getNacionalidade() {
		return nacionalidade;
	}
	public void setNacionalidade(String nacionalidade) {
		this.nacionalidade = nacionalidade;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	public double getAltura() {
		return altura;
	}
	public void setAltura(double altura) {
		this.altura = altura;
	}
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso = peso;
		this.setCategoria();
	}
	public String getCategoria() {
		return categoria;
	}
	public void setCategoria() {
		if(this.getPeso() >= 120) {
			this.categoria = "pesado";
		} else if (this.getPeso() < 120 && this.getPeso() >= 80) {
			this.categoria = "medio";
		} else {
			this.categoria = "leve";
		}
	}
	public int getVitorias() {
		return vitorias;
	}
	public void setVitorias(int vitorias) {
		this.vitorias = vitorias;
	}
	public int getDerrotas() {
		return derrotas;
	}
	public void setDerrotas(int derrotas) {
		this.derrotas = derrotas;
	}
	public int getEmpates() {
		return empates;
	}
	public void setEmpates(int empates) {
		this.empates = empates;
	}
	
	
	//Métodos da interface
	
	
	
	public void apresentar() {
		System.out.println("CONTEMPLEM AGORA O INCRÍVEL "+this.getNome()+ " O DESTRUIDOR!!!");
		System.out.println("DIRETAMENTE DE " +this.getNacionalidade());
		System.out.println("COM " +this.getIdade()+ " ANOS DE IDADE");
		System.out.println("COM "+ this.getAltura() + " METROS E PESANDO "+ this.getPeso() +" KILOS");
		if(this.getDerrotas() == 0) {
			System.out.println("ESTANDO INVICTO COM "+this.getVitorias()+ " E " +this.getEmpates() +" EMPATES");
		} else {
			System.out.println("CONTANDO COM "+ this.getVitorias() + " VITÓRIAS " +this.getDerrotas()+ " DERROTAS E " +this.getEmpates() + " EMPATES");
		}
		
	}
	public void status() {
		System.out.println(this.getNome());
		System.out.println("PESO E ALTURA " + this.getPeso() + this.getAltura());
		System.out.println("CATEGORIA "+ this.getCategoria());
		System.out.println("W/L/D" + this.getVitorias() + this.getDerrotas() + this.getEmpates());
		
		
	}
	public void ganharLuta() {
		this.setVitorias(this.getVitorias() + 1);
	}
	public void perderLuta() {
		this.setDerrotas(this.getDerrotas() + 1);
	}
	
	public void empatarLuta() {
		this.setEmpates(this.getEmpates() +1);
	}

}
