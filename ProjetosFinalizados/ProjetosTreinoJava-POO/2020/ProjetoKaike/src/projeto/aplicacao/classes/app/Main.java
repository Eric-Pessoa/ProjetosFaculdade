package projeto.aplicacao.classes.app;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		
	    Scanner sca1 = new Scanner(System.in);
	    
	    System.out.println("Digite que tipo de operação você quer realizar: ");
	    String operacao = sca1.next();
	    
	    System.out.println("Digite o primeiro número dessa operação:");
	    double Num1 = sca1.nextDouble();
	    
	    System.out.println("Digite o segundo número dessa operação:");
	    double Num2 = sca1.nextDouble();
	   
	    
	    switch(operacao) {
	    case "soma":
	    	double Num3 = Num1 + Num2;
	    	System.out.println("O resultado da soma é:");
	    	System.out.println(Num3);
	        
	    	
	    case "divisao":
	    	

	    }
	    
	    
	    
	    

		
		
	}

}
