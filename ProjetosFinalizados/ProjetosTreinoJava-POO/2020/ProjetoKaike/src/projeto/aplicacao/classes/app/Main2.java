package projeto.aplicacao.classes.app;

public class Main2 {

	public static void main(String[] args) {
		
		
        double[] conjunto = {10.2, 5.1, 12.3, 6.4, 8.0, 4.2};
        
        receberConjunto(conjunto);
        double ResultadoMedia = calcularMedia(conjunto);
        System.out.print(ResultadoMedia);
        double ResultadoMaior = calcularMaior(conjunto);
        System.out.print(ResultadoMaior);
        double ResultadoMenor = calcularMenor(conjunto);
        System.out.print(ResultadoMenor);
		}
		
		



	public static void receberConjunto(double[] conjunto1) {
		
		System.out.print("Conjunto: ");
		for(int i = 0; i < conjunto1.length; i++) {
				System.out.print(conjunto1[i]);
			
		}
	}
	
	
	public static double calcularMedia(double[] conjunto1) {
		
		double media = 0;
		System.out.print("\nMédia: ");
	    for(int i = 0; i < conjunto1.length; i++){
	            media += conjunto1[i];
	    }

	    media = media / conjunto1.length;
		
		return media;
		
		
		
	}
	
	
	public static double calcularMaior(double[] conjunto1) {
		
		double NumeroMaior = 0;
		System.out.print("\nMaior valor: ");
		
	    for(int i = 0; i < conjunto1.length; i++){
	    	if(conjunto1[i] > NumeroMaior) {
	            NumeroMaior = conjunto1[i];
	    	}
	    }
		
		return NumeroMaior;
		
		
		
	}
	
public static double calcularMenor(double[] conjunto1) {
		
		double NumeroMenor = 0;
		System.out.print("\nMenor valor: ");
		
	    for(int i = 0; i < conjunto1.length; i++){
	    	if(i == 0) {
	           NumeroMenor = conjunto1[i];
	    	} else if(conjunto1[i] < NumeroMenor){
	    		NumeroMenor = conjunto1[i];
	    		
	    	}
	    }
		
		return NumeroMenor;
}
}		
