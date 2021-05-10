package br.com.example.atividadeaula1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }


    fun mudancaImgGeral(view: View){

        //o when é tipo switch, voce coloca um valor, e abre as chaves pra testar
        when (view.id){

            //Por exemplo, se o id da view for igual ao id do button1, ele vai realizar uma ação, e sair do when
            R.id.button1 -> imagem.setImageResource(R.drawable.flor1)

            R.id.button2 -> imagem.setImageResource(R.drawable.flor2)

            R.id.button3 -> imagem.setImageResource(R.drawable.flor3)

            //caso default
            else -> imagem.setImageResource(R.drawable.flor1)






        }

    }



    //Setando uma função pra cada button, método burro

    fun mudancaImg(view: View) {
        imagem.setImageResource(R.drawable.flor1)

    }

    fun mudancaImg2(view: View) {
        imagem.setImageResource(R.drawable.flor2)

    }

    fun mudancaImg3(view: View) {
        imagem.setImageResource(R.drawable.flor3)

    }


}