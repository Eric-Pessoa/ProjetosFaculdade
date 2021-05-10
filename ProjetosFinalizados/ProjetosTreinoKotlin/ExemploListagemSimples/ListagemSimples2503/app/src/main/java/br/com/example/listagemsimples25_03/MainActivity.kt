package br.com.example.listagemsimples25_03

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {


    //array de strings, e entre parênteses define os elementos dessa lista.
    //o array começa da posição 0.
    val estados = arrayOf<String>(
        "Acre - AC",
        "Alagoas - AL",
        "Amapá - AM",
        "Bahia - BA",
        "Ceará - CE",
        "Distrito Federal - DF",
        "Espírito Santo - ES",
        "Goiás - GO",
        "Maranhão - MA",
        "Mato Grosso - MT",
        "Mato Grosso do Sul - MS",
        "Minas Gerais - MG",
        "Pará - PA",
        "Paraíba - PB",
        "Paraná - PA",
        "Pernambuco - PE",
        "Piauí - PI",
        "Rio de Janeiro - RJ",
        "Rio Grande do Norte - RN",
        "Rio Grande do Sul - RS",
        "Rondônia - RO",
        "Roraima - RR",
        "Santa Catarina - SC",
        "São Paulo - SP",
        "Sergipe - SE",
        "Tocantins - TO"
    )


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, estados)
        lstEstados.adapter =  adapter

        //o array começa no 0
        //parent é o adapter que a gente criou
        //view é a propria view
        //position é a posição em que o elemento foi clicado
        //e id é o id do item que foi clicado.
        lstEstados.setOnItemClickListener { parent, view, position, id ->

            //Exibe o nome do estado clicado, baseando-se na posição do array
            //que é a mesma posição do item criado na lista
            Toast.makeText(this, estados[position], Toast.LENGTH_LONG).show()




        }











    }
}