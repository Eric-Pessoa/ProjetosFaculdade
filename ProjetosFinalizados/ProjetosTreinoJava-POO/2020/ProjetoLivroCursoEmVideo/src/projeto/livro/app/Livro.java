package projeto.livro.app;
import java.util.Random;

public class Livro implements Publicacao {
	private String título;
	private String autor;
	private int totalPags;
	private int pagAtual;
	private boolean aberto;
	private Pessoa leitor;
	
	
	
	public String getTítulo() {
		return título;
	}
	public void setTítulo(String título) {
		this.título = título;
	}
	public String getAutor() {
		return autor;
	}
	public void setAutor(String autor) {
		this.autor = autor;
	}
	public int getTotalPags() {
		return totalPags;
	}
	public void setTotalPags(int totalPags) {
		this.totalPags = totalPags;
	}
	public int getPagAtual() {
		return pagAtual;
	}
	public void setPagAtual(int pagAtual) {
		this.pagAtual = pagAtual;
	}
	public boolean isAberto() {
		return aberto;
	}
	public void setAberto(boolean aberto) {
		this.aberto = aberto;
	}
	public Pessoa getLeitor() {
		return leitor;
	}
	public void setLeitor(Pessoa leitor) {
		this.leitor = leitor;
	}
	
	public void detalhes() {
		System.out.println("Autor do livro: " + this.getAutor());
		System.out.println("Título do livro: " + this.getTítulo());
		System.out.println("Quantidade de páginas do livro: " + this.getTotalPags());
		System.out.println("Página atual:  " + this.getPagAtual());
		System.out.println("Está aberto?  " + this.isAberto());

		
		
	}
	public void abrir() {
		this.setAberto(true);
		
	}
	public void fechar() {
		this.setAberto(false);
		
	}
	public void folhear() {
		Random gerador = new Random();
		int pagNova = gerador.nextInt(this.getTotalPags() + 1);
		this.setPagAtual(pagNova);
		System.out.println("Você caiu na página: " + pagNova);
		
		
		
	}
	public void avançarPag() {
		this.setPagAtual(pagAtual + 1);
		
	}
	
	public void voltarPag() {
		this.setPagAtual(pagAtual - 1); 
		
	}
	
	
	

}
