package projeto.emoji.app;

public class Main {

	public static void main(String[] args) {
		
		Lutador lutadores[] = new Lutador[6];
		lutadores[0] = new Lutador("Eric", "Brasileiro", 19, 1.75, 68.0, 4, 0, 1);
		lutadores[0].status();
		lutadores[1] = new Lutador("José", "Brasileiro", 20, 1.80, 70.0, 1, 1, 1);
		lutadores[2] = new Lutador("João", "Brasileiro", 20, 1.78, 85.0, 1, 1, 1);
		lutadores[3] = new Lutador("Jiloba", "Brasileiro", 23, 1.75, 89.0, 1, 1, 1);
		
		Luta luta1 = new Luta();
		luta1.marcarLuta(lutadores[0], lutadores[1]);
		System.out.println(lutadores[0].getVitorias());
		System.out.println(lutadores[0].getDerrotas());
		System.out.println(lutadores[0].getEmpates());
		luta1.lutar(lutadores[0],lutadores[1]);
		System.out.println(lutadores[0].getVitorias());
		System.out.println(lutadores[0].getDerrotas());
		System.out.println(lutadores[0].getEmpates());

	}

}
