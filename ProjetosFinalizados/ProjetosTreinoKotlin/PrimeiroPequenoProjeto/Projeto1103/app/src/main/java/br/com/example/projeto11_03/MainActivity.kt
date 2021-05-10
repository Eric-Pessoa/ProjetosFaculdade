package br.com.example.projeto11_03

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    //definindo a criação de um toast

    fun cliqueBotao (view: View){
        //verifica no edittext com o id txtNome, se o atributo text dele está vazio, sem nada escrito.
        //O trim() retira os espaçamentos antes e depois do texto, fazendo com que os espaços não contém como sendo   algo escrito.
        if (txtNome.text.trim().isEmpty()){
            Toast.makeText(this, "Informe um nome",Toast.LENGTH_LONG).show()
        } else{
            val msg = "Olá ${txtNome.text}"
            Toast.makeText(this, msg, Toast.LENGTH_LONG).show()

        }

    }

    //Se eu quisesse criar uma função só pra mandar os parâmetros pro alert, seria dessa forma
    fun InvocandoOAlert (view: View){
        val msg2 = "Olá ${txtNome.text}"
        exibirmensagem("Olá!", msg2)

    }


        //Definindo a criação de um alert

    fun exibirmensagem(titulo: String,mensagem: String   ){
        //instancia um builder com o método alertdialog, e o contexto sendo essa main activity.
        val builder = AlertDialog.Builder(this)
        //definindo os atributos do builder, definindo titulo, mensagem, etc
        builder
            .setTitle(titulo)
            .setMessage(mensagem)
                //define o texto do botão e se ele vai acionar alguma outra coisa.
            .setPositiveButton("Ok", null)
        //constroi a caixa de diálogo e mostra na tela
        builder.create().show()

    }
}