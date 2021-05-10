package br.com.example.intercionalizacao

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnMensagem.setOnClickListener {
            val mensagem = "${getString(R.string.ola_msg)}"
            val nome = txtNome.text.toString()
            Toast.makeText(this, "${mensagem} ${nome}",Toast.LENGTH_LONG).show()


        }
    }
}