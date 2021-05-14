package projeto.curso.video.app;

public class Visualizacao {
	
	private Viewer espectador;
	private Video filme;
	
	
	public Visualizacao(Viewer espectador, Video filme) {
		this.espectador = espectador;
		this.filme = filme;
		this.espectador.setTotAssistindo(this.espectador.getTotAssistindo() + 1);
		this.filme.setViews(this.filme.getViews() + 1);
	}
	
	public Viewer getEspectador() {
		return espectador;
	}
	public void setEspectador(Viewer espectador) {
		this.espectador = espectador;
	}
	public Video getFilme() {
		return filme;
	}
	public void setFilme(Video filme) {
		this.filme = filme;
	}
	
	@Override
	public String toString() {
		return "Visualizacao [espectador=" + espectador + ", filme=" + filme + "]";
	}
	
	public void avaliar() {
		this.filme.setAvaliacao(5);
		
	}
	
	public void avaliar(int nota) {
		this.filme.setAvaliacao(nota);
		
	}
	


}
