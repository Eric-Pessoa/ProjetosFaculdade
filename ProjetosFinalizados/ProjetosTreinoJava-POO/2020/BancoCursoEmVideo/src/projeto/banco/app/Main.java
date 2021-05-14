package projeto.banco.app;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {

		ArrayList<Integer> lista = new ArrayList<Integer>();
		Conta c1 = new Conta();
		c1.abrirConta(c1);
		System.out.println(c1.getSaldo());
		c1.setNumConta(lista, c1);
		System.out.println(c1.getNumConta());
		Conta c2 = new Conta();
		c2.setNumConta(lista, c2);
		System.out.println(c2.getNumConta());
	}	

}
