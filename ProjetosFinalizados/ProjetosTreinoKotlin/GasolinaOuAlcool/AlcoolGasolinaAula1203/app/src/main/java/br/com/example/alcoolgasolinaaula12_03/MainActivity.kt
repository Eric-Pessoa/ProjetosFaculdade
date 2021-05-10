package br.com.example.alcoolgasolinaaula12_03

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Conseguimos tirar tudo que teve o findviewbyid pois usamos a extensão que permite utilizar já diretamente
        //cada view que temos na nossa activity main do xml.
        //essa extensao traz automaticamente toda view que temos lá como um objeto acessível por meio do id aqui.


        //Método que procura uma view pelo id, nesse caso é do tipo button, e retorna ela num objeto.
        //desse jeito conseguimos manipular a view pelo objeto.
        //o nome da variável não precisa ser o mesmo nome do id.
        var btnCalcular = findViewById<Button>(R.id.btnCalcular)
        //função que implementa o evento de clique em um botão
        btnCalcular.setOnClickListener { _ : View? ->
            //aqui estamos apenas resgatando o objeto e setando ele numa variável

            //var txtAlcool = findViewById<EditText>(R.id.txtPrecoAlcool)

            //é aqul que, de fato, estamos resgatando o valor desse objeto e jogando esse valor em outra variável.
            var precoAlcool = txtPrecoAlcool.text.toString().toDouble()
            //var txtGasolina = findViewById<EditText>(R.id.txtPrecoGasolina)
            //declaração implícita do tipo da variável (só coloca var)
            var precoGasolina = txtPrecoGasolina.text.toString().toDouble()
            //declaração explícita da variável (coloca o tipo da variável)
            var resultado : Double = precoAlcool / precoGasolina
            var mensagem = ""
            if(resultado > 0.7){
                mensagem = "Gasolina"
            } else if(resultado < 0.7) {
                mensagem = "Álcool"
            } else {
                mensagem = "Tanto faz"
            }

            //Se eu quisesse mostrar o resultado em um toast, seria assim.
            //Toast.makeText(this, mensagem, Toast.LENGTH_LONG).show()

            //para mostrar em outra tela, é assim

            //instância do objeto intent, apontando para a activity alvo
            var intentResultado = Intent(this, MainActivity2::class.java)
            //armazenamento por conjuntos de chave-valor
            //note que essa chave tem a label de "Msg", e o valor da mensagem que definimos lá em cima.
            intentResultado.putExtra("msg", mensagem)
            //disparo da intent para carregar a nova tela
            startActivity(intentResultado)

        }




















    }
}