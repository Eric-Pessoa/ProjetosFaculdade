package br.com.example.atividadeaula3

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.text.DecimalFormat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnCalcular.setOnClickListener {

            if(camposSelecionados()) {
                val altura = txtAltura.text.toString().toDouble()
                val formula : Double
                if(radioMasc.isChecked){
                    val altura = txtAltura.text.toString().toDouble()
                    formula= (72.7 * altura) - 58
                }
                else {
                    val altura = txtAltura.text.toString().toDouble()
                    formula = (62.1 * altura) - 44.7
                }
                //Se eu quiser apenas mostrar o valor de uma variável pode se colocar apenas o cifrão e o nome da variável, se precisar entrar em alguma propriedade dentro da variável, aí sim precisará de chaves.
                val dec = DecimalFormat("#.0")
                val mensagem = "Peso ideal: ${dec.format(formula)} kg"
                Toast.makeText(this, mensagem, Toast.LENGTH_SHORT).show()



            }



        }



    }

    fun camposSelecionados() : Boolean {
        if(radioMasc.isChecked == false && radioFem.isChecked == false && txtAltura.text.trim().isEmpty()) {
            Toast.makeText(this, "Preencha todos os campos", Toast.LENGTH_LONG).show()
            return false
        }
        else if (radioMasc.isChecked == false && radioFem.isChecked == false) {
            Toast.makeText(this, "Selecione se você é homem ou mulher.", Toast.LENGTH_LONG).show()
            return false
        } else if (txtAltura.text.trim().isEmpty()) {
            Toast.makeText(this, "Preencha com sua altura.", Toast.LENGTH_LONG).show()
            return false
        }
        return true


    }
}