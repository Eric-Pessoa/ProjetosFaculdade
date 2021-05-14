package br.com.fiap.app;

public class ControleRemoto {
	
	public void AumentarVolume (Televisao televisao) {
		

		if(televisao.getVolume() == 100) {
			System.out.println("J� est� no volume m�ximo.");
		} else {
		
		int volume = televisao.getVolume();
		televisao.setVolume(volume + 1);
		System.out.println(televisao.getVolume());
		
		}
	
	}
	
	public void DiminuirVolume (Televisao televisao) {
		
		if(televisao.getVolume() == 0) {
			System.out.println("J� est� no volume m�nimo.");
		} else {
	
		int volume = televisao.getVolume();
		televisao.setVolume(volume - 1);
		System.out.println(televisao.getVolume());
		
		}
		
	
	}
	
	
	public void AumentarCanal (Televisao televisao) {
		
		
		int canal = televisao.getCanal();
		televisao.setCanal(canal + 1);
		System.out.println(televisao.getCanal());
	
	}
	
	public void DiminuirCanal (Televisao televisao) {
		
		if(televisao.getCanal() == 1) {
			System.out.println("Imposs�vel ir para o canal 0.");
		} else {
	
		int canal = televisao.getCanal();
		televisao.setCanal(canal - 1);
		System.out.println(televisao.getCanal());
		
		}
	}
	
	
	public void SelecionarCanal (Televisao televisao, int canalDesejado) {
		
		
		televisao.setCanal(canalDesejado);
		System.out.println(televisao.getCanal());
	
	}
	
	
	public void ConsultaVolumeECanal (Televisao televisao) {
		
		System.out.println("O canal que est� no momento �: "+televisao.getCanal()+" E o volume �: "+televisao.getVolume());
	
	}
	

	
	
	
	
}
