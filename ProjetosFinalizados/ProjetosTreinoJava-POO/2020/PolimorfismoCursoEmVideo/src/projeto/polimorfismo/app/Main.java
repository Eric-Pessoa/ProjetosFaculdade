package projeto.polimorfismo.app;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		//Exemplo claro aí de sobrecarga, podemos ver que tem o mesmo nome de método, porém com assinaturas diferentes, então são 2 métodos usados para diferentes coisas.
		
		Teclado t1 = new Teclado(); 
		t1.tocarNota(1);
		t1.tocarNota("dó");

	}

}
