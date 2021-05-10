package br.com.example.checkpoint1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_tela_conta_telefonica_resultado.*


class tela_conta_telefonica_resultado : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_conta_telefonica_resultado)
        lbResultado.text = intent.getStringExtra("msg")
    }
}



