package projeto.aplicacao.classes.app;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		
	    Scanner sca1 = new Scanner(System.in);
	    
	    System.out.println("Digite que tipo de opera��o voc� quer realizar: ");
	    String operacao = sca1.next();
	    
	    System.out.println("Digite o primeiro n�mero dessa opera��o:");
	    double Num1 = sca1.nextDouble();
	    
	    System.out.println("Digite o segundo n�mero dessa opera��o:");
	    double Num2 = sca1.nextDouble();
	   
	    
	    switch(operacao) {
	    case "soma":
	    	double Num3 = Num1 + Num2;
	    	System.out.println("O resultado da soma �:");
	    	System.out.println(Num3);
	        
	    	
	    case "divisao":
	    	

	    }
	    
	    
	    
	    

		
		
	}

}
