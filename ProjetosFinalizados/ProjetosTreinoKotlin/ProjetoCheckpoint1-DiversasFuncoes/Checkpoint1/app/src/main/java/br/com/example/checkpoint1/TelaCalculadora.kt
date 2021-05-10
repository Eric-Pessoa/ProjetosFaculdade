package br.com.example.checkpoint1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_tela_calculadora.*
import java.text.DecimalFormat

class TelaCalculadora : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_calculadora)


        btnCalcular.setOnClickListener {
            if(camposValidos()){
                val valor1 = txtVal1.text.toString().toDouble()
                val valor2 = txtVal2.text.toString().toDouble()

                val resultado: Double = if (rbSoma.isChecked) {
                    valor1 + valor2
                } else if (rbSubtracao.isChecked) {
                    valor1 - valor2
                } else if (rbMultiplicacao.isChecked) {
                    valor1 * valor2
                } else {
                    valor1 / valor2
                }

                val dec = DecimalFormat("#.0")
                val mensagem = "Resultado: ${dec.format(resultado)}"
                Toast.makeText(this, mensagem, Toast.LENGTH_LONG).show()
            }

        }
    }

    private fun camposValidos(): Boolean {
        if (txtVal1.text.trim().isEmpty() || txtVal2.text.trim().isEmpty()) {
            Toast.makeText(this, "Preencha todos os campos.", Toast.LENGTH_LONG).show()
            return false
        }
        return true
    }
}









