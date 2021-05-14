package br.com.fiap.app.main;

import br.com.fiap.app.ControleRemoto;
import br.com.fiap.app.Televisao;

public class Main {

	public static void main(String[] args) {
		
		Televisao tv = new Televisao();
		
		ControleRemoto controle = new ControleRemoto();
		
		controle.AumentarVolume(tv);
		controle.AumentarVolume(tv);


		controle.DiminuirVolume(tv);

		controle.DiminuirCanal(tv);
		
		controle.AumentarCanal(tv);
		
		
		controle.SelecionarCanal(tv, 90);
		
		controle.ConsultaVolumeECanal(tv);
				


	}

}
