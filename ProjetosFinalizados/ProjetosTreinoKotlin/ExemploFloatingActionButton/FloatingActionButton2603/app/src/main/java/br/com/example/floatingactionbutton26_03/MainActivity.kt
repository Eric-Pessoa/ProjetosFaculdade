package br.com.example.floatingactionbutton26_03

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    //lista de tarefas
    var tarefas = ArrayList<String>()
    //adapter para o listview
    //nenhum objeto pode ter valor null, a não ser que vc declare explicitamente
    //o ? indica pro kotlin que o objeto pode ser null
    var adapter: ArrayAdapter<String>? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, tarefas)
        //associa o adapter do lstTarefas ao adapter que acabamos de criar
        lstTarefas.adapter = adapter

        fab.setOnClickListener {
            adicionarTarefa()

        }

        lstTarefas.setOnItemClickListener { parent, view, position, id ->
            var tarefa = parent.adapter.getItem(position).toString()
            atualizarTarefa(tarefa, position)

        }


    }

    fun atualizarTarefa(tarefa: String, posicao: Int){
        var builder = AlertDialog.Builder(this)
        builder.setTitle("Atualizar Tarefa")
        val entrada = EditText(this)
        //aqui com o buffertype editable estamos só falando que o texto que vem é editável
        entrada.setText(tarefa, TextView.BufferType.EDITABLE)
        builder.setView(entrada)
        builder.setPositiveButton("Ok"){ dialog, which ->
            //na lista eu quero atualizar, onde meu user selecionou, o novo texto.
            tarefas[posicao] = entrada.text.toString()
            adapter?.notifyDataSetChanged()
        }
        builder.setNegativeButton("Cancel", null)
        builder.setNeutralButton("Excluir"){ dialog, which ->
            tarefas.removeAt(posicao)
            adapter?.notifyDataSetChanged()

        }
        builder.create().show()
    }

    fun adicionarTarefa() {
        // cria um AlertDialog para o usuário inserir uma tarefa
        var builder = AlertDialog.Builder(this)
        builder.setTitle("Nova Tarefa")
        //Adiciona um EditText ao alertDialog
        val entrada = EditText(this)
        builder.setView(entrada)
        //define o tratamento para quando o botão ok for pressionado
        builder.setPositiveButton("Ok"){ dialog, which ->
            tarefas.add(entrada.text.toString())
            adapter?.notifyDataSetChanged()
        }
        builder.setNegativeButton("Cancel", null)
        builder.create().show()
    }
}