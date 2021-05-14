package elevador.aplica;

public class Elevador {
	private int qntdAndares;
	public int getQntdAndares() {
		return qntdAndares;
	}
	public void setQntdAndares(int qntdAndares) {
		this.qntdAndares = qntdAndares;
	}
	public int getAndarAtual() {
		return andarAtual;
	}
	public void setAndarAtual(int andarAtual) {
		this.andarAtual = andarAtual;
	}
	public int getQntdAtualPessoas() {
		return qntdAtualPessoas;
	}
	public void setQntdAtualPessoas(int qntdAtualPessoas) {
		this.qntdAtualPessoas = qntdAtualPessoas;
	}
	public int getCapacidadeMaxima() {
		return capacidadeMaxima;
	}
	public void setCapacidadeMaxima(int capacidadeMaxima) {
		this.capacidadeMaxima = capacidadeMaxima;
	}
	private int andarAtual;
	private int qntdAtualPessoas;
	private int capacidadeMaxima;
	
	
	public Elevador(int qntdAtualPessoas, int andarAtual) {
		this.qntdAtualPessoas = qntdAtualPessoas;
		 capacidadeMaxima = 30;
		 qntdAndares = 3;	
		
	}
	
	public void entra(int qntdPessoasEntrando) {
		System.out.println("Tem " +qntdAtualPessoas+ " No elevador agora");
		qntdAtualPessoas = qntdAtualPessoas + qntdPessoasEntrando;
		if(qntdAtualPessoas> capacidadeMaxima) {
			System.out.println("Não dá, o elevador vai cair e tu vai morrer");
		} else {
			
			System.out.println("beleza, agora tem " + qntdAtualPessoas + " pessoas nesse elevador");
		}
			
			
			
		}
	
	
	public int sai(int TirarPessoas) {
		qntdAtualPessoas = qntdAtualPessoas - TirarPessoas;
		if(qntdAtualPessoas < 0) {
		System.out.println("Não dá pra ficar um número negativo de pessoas no elevador");
		} else {
			System.out.println("Sairam " + TirarPessoas + " pessoas");
			
		}
		return qntdAtualPessoas;
		
	}
	
	public boolean subir(int pedidosubir) {
		pedidosubir = pedidosubir + andarAtual;
		if(pedidosubir > qntdAndares) {
			System.out.println("Não dá pra subir esse tanto, loki");
			return false;
		} else {
			System.out.println("podepa, parei no " +pedidosubir+ " andar");
			return true;
		}
		
	}
	
	
	public boolean descer (int pedidodescer) {
		andarAtual = andarAtual- pedidodescer;
		if(andarAtual <= 0) {
			System.out.println("oxe");
			return false;
		} else {
			System.out.println("podepa, parei no "+ andarAtual + " andar");
			return true;
		}
		
	}
	
	
	
}
	
	
	

    




