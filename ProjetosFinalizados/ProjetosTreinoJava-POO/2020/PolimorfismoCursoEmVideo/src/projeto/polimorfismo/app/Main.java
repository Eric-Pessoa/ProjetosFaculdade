package projeto.polimorfismo.app;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		//Exemplo claro a� de sobrecarga, podemos ver que tem o mesmo nome de m�todo, por�m com assinaturas diferentes, ent�o s�o 2 m�todos usados para diferentes coisas.
		
		Teclado t1 = new Teclado(); 
		t1.tocarNota(1);
		t1.tocarNota("d�");

	}

}
