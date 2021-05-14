import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestaListagem {

	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub

		Connection con = DriverManager.getConnection("jdbc:oracle:thin:@oracle.fiap.com.br:1521:ORCL", "RM86405", "070302");
		
		//System.out.println("Conexão aberta.");
		
		//String sql = "SELECT ID, NOME, DESCRICAO FROM PRODUTO.";
		
		Statement statement = con.createStatement();
		
		statement.execute("SELECT ID, NOME, DESCRICAO FROM PRODUTO");
		
		ResultSet rs = statement.getResultSet();
		
		while (rs.next()) {
			// Se tem registros, executa o que tá aqui, se não, pula pro debaixo
			int id = rs.getInt("ID");
			String nome = rs.getString("NOME");
			String descricao = rs.getString("DESCRICAO");
			System.out.println("ID: " + id);
			System.out.println("NOME: " + nome);
			System.out.println("DESCRICAO: "+ descricao);
	
			}
		
		rs.close();
		statement.close();
		con.close();
		
			
		}
		
	}

