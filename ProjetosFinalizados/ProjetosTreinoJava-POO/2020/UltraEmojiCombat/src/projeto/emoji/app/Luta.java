package projeto.emoji.app;
import java.util.Random;

public class Luta {
	private Lutador desafiante;
	private Lutador desafiado;
	private int rounds;
	private boolean aprovado;
	
	
	
	
	public Lutador getDesafiante() {
		return desafiante;
	}

	private void setDesafiante(Lutador desafiante) {
		this.desafiante = desafiante;
	}

	public Lutador getDesafiado() {
		return desafiado;
	}

	private void setDesafiado(Lutador desafiado) {
		this.desafiado = desafiado;
	}

	public int getRounds() {
		return rounds;
	}

	private void setRounds(int rounds) {
		this.rounds = rounds;
	}

	public boolean isAprovado() {
		return aprovado;
	}

	private void setAprovado(boolean aprovado) {
		this.aprovado = aprovado;
	}

	
	
	public void marcarLuta(Lutador desafiante, Lutador desafiado) {
		if(desafiante.getCategoria() == desafiado.getCategoria() && desafiante != desafiado) {
			this.setAprovado(true);
			this.setDesafiante(desafiante);
			this.setDesafiado(desafiado);
		} else {
			System.out.println("Impossível marcar essa luta.");
		}
		
	}
	
	public void lutar(Lutador desafiante, Lutador desafiado) {
		if(this.isAprovado()) {
			desafiante.apresentar();
			desafiado.apresentar();
			Random gerador = new Random();
			int rounds = 3;
			int contadorDesafiante = 0;
			int contadorDesafiado = 0;
			int contadorEmpate = 0;
			for(int i = 0; i < rounds; i++) {
				int quemGanhou = gerador.nextInt(3);
				System.out.println(quemGanhou);
				if(quemGanhou == 1) {
					contadorDesafiante += 1;
					System.out.println("Desse round o vencedor foi: " + desafiante.getNome());
				} else if(quemGanhou == 2) {
					contadorDesafiado +=1;
					System.out.println("Desse round o vencedor foi: " + desafiado.getNome());
				} else {
					contadorEmpate += 1;
					System.out.println("Esse round deu EMPATE!");
				}
				
			}if(contadorDesafiante > contadorDesafiado) {
				desafiante.ganharLuta();
				desafiado.perderLuta();
				System.out.println("O GRANDE VENCEDOR FOI O "+ desafiante.getNome()+ " PARABÉNS AO VENCEDOR!");
			} else if(contadorDesafiante < contadorDesafiado) {
				desafiado.ganharLuta();
				desafiante.perderLuta();
				System.out.println("O GRANDE VENCEDOR FOI O "+ desafiado.getNome()+ " PARABÉNS AO VENCEDOR!");
			} else if(contadorEmpate >= 1 || contadorEmpate == 1 && contadorDesafiante == 1 && contadorDesafiado == 1) {
				desafiado.empatarLuta();
				desafiante.empatarLuta();
				System.out.println("SENHORAS E SENHORES, EU ME CAGUEI.");
			}
			
		
			
		} else {
			System.out.println("Luta não pode acontecer.");
		}
		
	}
}
