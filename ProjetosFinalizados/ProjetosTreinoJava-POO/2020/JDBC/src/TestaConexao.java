import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestaConexao {

	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub
		
		String url = "jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL"; // JDBC:oracle:thin:@host:porta: nome do servi�o 
		String usuario = "RM86405";
		String senha = "070302";

		Connection con = DriverManager.getConnection(url, usuario, senha);
		
		System.out.println("Conex�o aberta");
		
		//usa a conex�o
		
		con.close();
		
	}

}
