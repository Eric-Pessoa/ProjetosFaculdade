package br.com.example.checkpoint1

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }

    fun exibirmensagem(titulo: String,mensagem: String ){
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

    fun invocandoOAlert (view: View){
        val msg = "Eric Luiz Campos Pessoa\nGiovanna de Mello Leiva\nDaniel Sanchez Melero"
        exibirmensagem("Desenvolvido por", msg)

    }


    fun mudarTelaParaCalculadora (view: View) {
        var intentResultado = Intent(this, TelaCalculadora::class.java)
        startActivity(intentResultado)
    }

    fun mudarTelaParaContaTelefonica (view: View) {
        var intentResultado = Intent(this, tela_conta_telefonica::class.java)
        startActivity(intentResultado)
    }


}