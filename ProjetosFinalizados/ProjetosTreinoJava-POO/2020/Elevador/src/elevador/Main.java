package elevador;

import elevador.aplica.Elevador;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Elevador c1 = new Elevador(4,3);
		c1.entra(26);
		c1.sai(30);
		//c1.subir(3);
		c1.descer(1);

	}

}
