package br.com.fiap.app;

public class Televisao {
	
	private int canal ;
	private int volume;
	
	
	
	public Televisao() {
		canal = 1;
		volume = 10;
	}
	
	public int getCanal() {
		return canal;
	}
	
	public void setCanal(int canal) {
		this.canal = canal;
	}
	
	public int getVolume() {
		return volume;
	}
	
	public void setVolume(int volume) {
		this.volume = volume;
	}

}
