package br.com.example.atividadeaula2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        //var btnCalcular = findViewById<Button>(R.id.idButton)
        idButton.setOnClickListener { _:View ->

            if (idCampo1.text.trim().isEmpty() || idCampo2.text.trim().isEmpty()){
                Toast.makeText(this, "Preencha os 2 campos, por favor.", Toast.LENGTH_LONG).show()
            } else{

                var valor1 = idCampo1.text.toString().toDouble()
                var valor2 = idCampo1.text.toString().toDouble()

                var resultadoConta : Double = valor1 + valor2

                var intentResultado = Intent(this, MainActivity2::class.java)
                intentResultado.putExtra("msg", resultadoConta)
                startActivity(intentResultado)










        }
    }
} }