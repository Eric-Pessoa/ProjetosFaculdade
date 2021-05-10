package br.com.example.alcoolgasolinaaula12_03

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main2.*

class MainActivity2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        //recupera o resultado da chave que definimos no intent do MainActivity e jogamos no atributo texto
        //da view lbResultado.
        //é getStringExtra porque o tipo de dado que eu quero resgatar é string, e o label da chave é msg.
        lbResultado.text = intent.getStringExtra("msg")
















    }
}