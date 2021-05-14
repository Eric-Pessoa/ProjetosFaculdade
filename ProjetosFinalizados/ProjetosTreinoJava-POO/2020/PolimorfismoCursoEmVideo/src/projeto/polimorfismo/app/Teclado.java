package projeto.polimorfismo.app;

public class Teclado {
	
	//Exemplo de um polimorfismo de sobrecarga
	
	public void tocarNota(String nota) {
		if(nota == "dó") {
			System.out.println("DÓ");
		} else {
			System.out.println("AAAAAAAAAAAAA");
		}
	
	}
	
	public void tocarNota(int escala) {
		if(escala == 1) {
			System.out.println("Escala grave");
		} else {
			System.out.println("Escala aguda");
		}

}
}