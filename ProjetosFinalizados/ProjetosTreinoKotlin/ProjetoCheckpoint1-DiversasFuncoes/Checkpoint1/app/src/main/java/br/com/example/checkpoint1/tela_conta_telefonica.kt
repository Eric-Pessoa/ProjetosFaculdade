package br.com.example.checkpoint1

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_tela_conta_telefonica.*
import java.text.DecimalFormat

class tela_conta_telefonica : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_conta_telefonica)

        btnCalcular.setOnClickListener {
            val dec = DecimalFormat("#.00")
            if (camposValidos()) {
                var txtAssinatura = txtAssinatura.text.toString().toDouble()
                var txtChLocal = txtChLocal.text.toString().toDouble() * 0.04
                var txtChCelular = txtChCelular.text.toString().toDouble() * 0.20
                var resultado: Double = txtAssinatura + txtChLocal + txtChCelular
                resultado = dec.format(resultado).toDouble()


                var mensagem = """Assinatura     : R$ ${txtAssinatura.toString()}
                 |Chamada Local  : R$ ${txtChLocal.toString()}
                 |Chamada Celular: R$ ${txtChCelular.toString()}
                 
                 |Valor Total    : R$ ${resultado.toString()}
                """.trimMargin("|")
                var intentResultado = Intent(this, tela_conta_telefonica_resultado::class.java)
                intentResultado.putExtra("msg", mensagem)
                startActivity(intentResultado)
            }
        }
    }

    fun camposValidos() : Boolean {
        if (txtAssinatura.text.trim().isEmpty() || txtChLocal.text.trim().isEmpty()
                || txtChCelular.text.trim().isEmpty()) {
            Toast.makeText(this, "Preencha todos os campos.", Toast.LENGTH_LONG).show()
            return false
        }
        return true
    }

}


















