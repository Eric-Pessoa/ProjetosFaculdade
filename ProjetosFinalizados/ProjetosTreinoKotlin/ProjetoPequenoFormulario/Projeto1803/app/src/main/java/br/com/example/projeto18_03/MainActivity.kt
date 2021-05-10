package br.com.example.projeto18_03

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Cria um array de itens para o spinner
        val itensSpinner = arrayOf<String>("Selecione", "Residencial", "Comercial", "Celular", "Outro")
        //Cria um adapter para poder mostrar os itens do spinner na tela
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, itensSpinner)
        //Fala para o adapter definir o spinner como caindo e abrindo a lista.
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        //No componente da tela temos a propriedade adapter, e vamos atribuir pra ele o adapter que acabamos de criar
        spinnerTipoTelefone.adapter = adapter

        //Cria um listener pro botão
        //Esse listener checa se os campos estão válidos, chamando a outra função criada.
        btnMsg.setOnClickListener {
            if (camposValidos()) {
                //msg que vai ser mandada pro alert
                // O pipeline define o espaçamento da tabulação
                var msg = """Nome: ${txtNome.text}
                    |Telefone: ${txtPhone.text}
                    |Tipo Telefone:  ${spinnerTipoTelefone.selectedItem}
                    |Email: ${txtEmail.text}
                    |Preferências de contato:
                    """.trimMargin("|")
                    //O TrimMargin tira tudo que tá a esquerda, inclusive o pipeline, e define uma margem.

                if (cbTelefone.isChecked) {
                    //Se estiver checado, entra no if, pega o valor atual da mensagem e concatena com a String a ser
                    //passada
                    msg += "\n - Telefone"
                }
                if (cbEmail.isChecked){
                    msg += "\n - Email"
                }

                //Chama o alert e passa os parâmetros recém criados.
                alert("Boas vindas", msg)
            }


        }

    }

    //Essa função retorna um boolean indicando se os campos estão válidos ou não
    //A função selectedItemPosition pega uma posição do array spinnerTipoTelefone e faz uma verificação com ela.
    fun camposValidos() : Boolean {
        if (txtNome.text.trim().isEmpty() || txtPhone.text.trim().isEmpty()
            || spinnerTipoTelefone.selectedItemPosition == 0
            || txtEmail.text.trim().isEmpty()) {
            Toast.makeText(this,"Preencha todos os campos.", Toast.LENGTH_LONG).show()
            return false
        }
        return true

        //Se entrou no if a função retorna falso, se não, retorna que tá tudo bem.



    }


    fun alert(titulo: String, mensagem: String) {
        //Constroi um alertDialog. joga na val builder, e passa o contexto sendo essa activity
        val builder = AlertDialog.Builder(this)
        //Passa os parâmetros do builder
        builder
            .setTitle(titulo)
            .setMessage(mensagem)
            .setPositiveButton("Ok", null)
        //Por fim, mostra o builder
        builder.create().show()


    }





}