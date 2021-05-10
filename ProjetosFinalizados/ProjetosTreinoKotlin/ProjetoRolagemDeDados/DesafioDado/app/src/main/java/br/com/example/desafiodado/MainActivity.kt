package br.com.example.desafiodado

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.lang.Math.*
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Diferentes formas de pegar um random
        //vai até o 6, não conta o 7, no primeiro caso, começa no 1
        val random = Random.nextInt(1, 7)
        val randomDouble = Math.random()
        val randomInteger1 = (1..6).shuffled().first()
        val randomInteger2 = (1..6).shuffled().first()


        btnJogar.setOnClickListener {

            val random = Random.nextInt(1, 7)
            val random2 = Random.nextInt(1, 7)
            val valorDado1 = idImagemDado(random)
            val valorDado2 = idImagemDado(random2)
            image1.setImageResource(valorDado1)
            image2.setImageResource(valorDado2)

            if(random > random2) {
                Toast.makeText(this, "Jogador 1 venceu", Toast.LENGTH_SHORT).show()
            } else if (random == random2) {
                Toast.makeText(this, "Empate", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Jogador 2 venceu", Toast.LENGTH_SHORT).show()

            }


        }
    }


    fun idImagemDado(valor: Int) : Int {
        return when(valor){

            1 -> R.drawable.face1
            2 -> R.drawable.face2
            3 -> R.drawable.face3
            4 -> R.drawable.face4
            5 -> R.drawable.face5
            6 -> R.drawable.face6
            else -> R.drawable.face1
        }
    }



}