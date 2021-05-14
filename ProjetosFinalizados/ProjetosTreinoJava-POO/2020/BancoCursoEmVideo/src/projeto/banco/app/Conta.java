package projeto.banco.app;
//import java.util.Random;
import java.util.ArrayList;
import java.util.Scanner;


public class Conta {
	private int numConta;
	private String tipo;
	private String dono;
	private double saldo;
	private boolean status;
	
	
	public Conta() {
		
		numConta = 0;
		tipo = "";
		dono = "";
		saldo = 0;
		status = false;
		
		
		
	}

	public int getNumConta() {
		return numConta;
	}
	
	public void setNumConta(ArrayList<Integer> lista, Conta conta) {
		if(lista.contains(1) == false) {
			this.numConta = 1;
		
		} else {
			this.numConta = lista.size()+1;
			
		}
		
	}


	public String  getTipo() {
		return tipo;
	}
	
	public void setTipo(String tipoInformado) {
	    this.tipo = tipoInformado;
		
	}
	
	public String getDono() {
		return dono;
	}
	public void setDono(String dono) {
		this.dono = dono;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	public boolean getStatus() {
		return status;
	}
	public void setStatus(boolean status) {
		this.status = status;
	}

	
	
	
	public void abrirConta(Conta conta) {
		Scanner sc1 = new Scanner(System.in);
		conta.setStatus(true);
		System.out.println("Você quer abrir uma conta corrente ou poupança? cc para corrente, cp para poupança.");
		String resposta = sc1.next();
		sc1.close();
		conta.setTipo(resposta);

	
		if(conta.getTipo().equals("cc")) {
			conta.setSaldo(50);
			System.out.println("Obrigado por abrir sua conta conosco, depositamos 50 reais nela.");
		} else {
			conta.setSaldo(150);
			System.out.println("Obrigado por abrir sua conta conosco, depositamos 150 reais nela.");
		}
		
	}
	
	
	public void fecharConta(Conta conta) {
		if(conta.getSaldo() > 0) {
			System.out.println("Impossível fechar a conta com dinheiro ainda dentro dela.");
		} else {
			conta.setStatus(false);
			System.out.println("Conta fechada com sucesso.");
		}
		
		
	}
	
	public void depositar(Conta conta, double quantia) {
		if(conta.getStatus() == false) {
			System.out.println("A conta não foi aberta, impossível depositar.");
		} else {
			double ValorConta = conta.getSaldo();
			conta.setSaldo(ValorConta + quantia);
		}
		
		
	}
	
	public void sacar(Conta conta, double quantia) {
		if(conta.getStatus() == false) {
			System.out.println("A conta não foi aberta, impossível sacar.");
		} else if(conta.getSaldo() == 0 || conta.getSaldo() < quantia ) {
			System.out.println("Impossível realizar o saque.");
		} else {
			double SaldoAtual = conta.getSaldo();
			double SaldoResultante = SaldoAtual - quantia;
			conta.setSaldo(SaldoResultante);
			System.out.println("Sobrou "+ conta.getSaldo()+" reais");
		}
		
		
		
	}
	
	public void pagarMensalidade(Conta conta) {
		if(conta.getTipo().equals("cc")) {
		double SaldoAtual = conta.getSaldo();
		conta.setSaldo(SaldoAtual - 12);
		} else {
			double SaldoAtual = conta.getSaldo();
			conta.setSaldo(SaldoAtual - 20);
		}
		
	}
	
	

}
