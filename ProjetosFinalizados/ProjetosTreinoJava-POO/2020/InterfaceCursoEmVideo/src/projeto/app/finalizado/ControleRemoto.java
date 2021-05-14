package projeto.app.finalizado;

public class ControleRemoto implements Controlador {
	private int volume;
	private boolean ligado;
	private boolean tocando;
	
	
	
	public ControleRemoto() {
		this.volume = 50;
		this.ligado = false;
		this.tocando = false;
	}

	
	
	public int getVolume() {
		return volume;
	}

	public void setVolume(int volume) {
		this.volume = volume;
	}

	public boolean getLigado() {
		return ligado;
	}

	public void setLigado(boolean ligado) {
		this.ligado = ligado;
	}

	public boolean getTocando() {
		return tocando;
	}

	public void setTocando(boolean tocando) {
		this.tocando = tocando;
	}



	
	public void ligar() {
		this.setLigado(true);
	}



	public void desligar() {
		this.setLigado(false);
	}



	public void abrirMenu() {
		if(this.getLigado() == false) {
			System.out.println("Não dá pra abrir o menu com a tv desligada.");
		} else {
			System.out.println("Está ligada");
			System.out.println("Está tocando? " + this.getTocando());
			System.out.println("Volume: " + this.getVolume());
			for (int i = 0; i <= this.getVolume(); i+=5) {
				System.out.print("|");
			}
			System.out.println();
		}
		
	}



	public void fecharMenu() {
		System.out.println("Fechando menu...");
	}



	public void maisVolume() {
		if(this.getLigado() == false) {
			System.out.println("Impossível aumentar com a tv desligada");
		} else {
			this.setVolume(this.getVolume() +5);
		}
	}



	public void menosVolume() {
		if(this.getLigado() == false) {
			System.out.println("Impossível diminuir com a tv desligada");
		} else {
			this.setVolume(this.getVolume() -5);
		}
		
	}



	public void ligarMudo() {
		if(this.getLigado() == true && this.getVolume() > 0) {
			this.setVolume(0);
		}
		
	}



	
	public void desligarMudo() {
		if(this.getLigado() == true && this.getVolume() == 0) {
			this.setVolume(25);
		}
		
	}



	public void play() {
		if(this.getLigado() == true && this.getTocando() == false) {
			this.setTocando(true);
		}
		
	}



	
	public void pause() {
		if(this.getLigado() == true && this.getTocando() == true) {
			this.setTocando(false);
		}
	}
	
	

}
