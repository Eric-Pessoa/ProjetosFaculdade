package projeto.livro.app;
import java.util.Random;

public class Livro implements Publicacao {
	private String t�tulo;
	private String autor;
	private int totalPags;
	private int pagAtual;
	private boolean aberto;
	private Pessoa leitor;
	
	
	
	public String getT�tulo() {
		return t�tulo;
	}
	public void setT�tulo(String t�tulo) {
		this.t�tulo = t�tulo;
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
		System.out.println("T�tulo do livro: " + this.getT�tulo());
		System.out.println("Quantidade de p�ginas do livro: " + this.getTotalPags());
		System.out.println("P�gina atual:  " + this.getPagAtual());
		System.out.println("Est� aberto?  " + this.isAberto());

		
		
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
		System.out.println("Voc� caiu na p�gina: " + pagNova);
		
		
		
	}
	public void avan�arPag() {
		this.setPagAtual(pagAtual + 1);
		
	}
	
	public void voltarPag() {
		this.setPagAtual(pagAtual - 1); 
		
	}
	
	
	

}
