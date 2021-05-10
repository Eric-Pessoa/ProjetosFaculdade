import React from 'react';
import { Alert, Button, Image, StatusBar, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

      //Variáveis
      valorInserido: "0",

      //Titulo
      titulo: "Conta corrente",
      backColor: "blue",
      fontSizeTitulo: 32,

      //Texto 1 (saldo)
      txt1: "Saldo",
      txt1margin: 20,

      //Texto 2 (valor)
      valor: "10",
      fonttxt2: 20,
      cor: "green",

      //Botão 1
      txtBtn1: "Crédito",
      func: this.cliqueBotaoCredito,

      //Botão 2
      txtBtn2: "Débito",
      func2: this.cliqueBotaoDebito,

      //Text input
      editable1: false,
      borderWidth1: 0.0,
      borderColor: "grey",
      cor2: 'black',


      /////////






    }
  }

  cliqueBotaoCredito = _ => {
    this.setState({ titulo: "Operação de crédito" });
    this.setState({ backColor: "grey" })
    this.setState({ fontSizeTitulo: 20 })

    this.setState({ txt1: "Valor" })

    this.setState({ fonttxt2: 0 })

    this.setState({ txtBtn1: "Voltar ao menu" })
    this.setState({ txtBtn2: "Depositar" })

    this.setState({ editable1: true })
    this.setState({ borderWidth1: 1 })
    this.setState({ borderColor: "grey" })
    this.setState({cor2:'white'})
    this.setState({ func: this.cancelar })
    this.setState({ func2: this.salvar })




  }

  cliqueBotaoDebito = _ => {
    this.setState({ titulo: "Operação de débito" });
    this.setState({ backColor: "grey" })
    this.setState({ fontSizeTitulo: 20 })

    this.setState({ txt1: "Valor" })

    this.setState({ fonttxt2: 0 })

    this.setState({ txtBtn1: "Voltar ao menu" })
    this.setState({ txtBtn2: "Sacar" })

    this.setState({ editable1: true })
    this.setState({ borderWidth1: 1 })
    this.setState({ borderColor: "grey" })
    this.setState({cor2:'white'})
    this.setState({ func: this.cancelar })
    this.setState({ func2: this.salvar })




  }

  cancelar = _ => {

    this.setState({ valorInserido: "0" })

    this.setState({ valor: this.state.valor })
    this.setState({ fonttxt2: 20 })
    if(this.state.valor < 0){
    this.setState({ cor: "red" })
    } else {
    this.setState({cor: "green"})
    }   
    this.setState({ txt1: "Saldo", })
    this.setState({ txt1margin: 20, })

    this.setState({ txtBtn1: "Crédito", })
    this.setState({ txtBtn2: "Débito", })

    this.setState({ titulo: "Conta corrente", })
    this.setState({ backColor: "blue", })
    this.setState({ fontSizeTitulo: 32, })

    this.setState({ editable1: false, })
    this.setState({ borderWidth1: 0.0, })
    this.setState({ borderColor: "black" })
    this.setState({cor2:'black'})


    this.setState({ func: this.cliqueBotaoCredito })
    this.setState({ func2: this.cliqueBotaoDebito })


  }




  salvar = _ => {
    if (this.state.titulo == "Operação de crédito") {
      var { valor } = this.state;
      var { valorInserido } = this.state
      var valorMuda = parseFloat(valor);
      var valorInseridoMuda = parseFloat(valorInserido)
      var resultado = valorMuda + valorInseridoMuda
      this.setState({ valor: resultado })
      Alert.alert("Depósito concluído", "Já pode voltar ao menu")
      

    } else {
      var { valor } = this.state;
      var { valorInserido } = this.state
      var valorMuda = parseFloat(valor);
      var valorInseridoMuda = parseFloat(valorInserido)
      var resultado = valorMuda - valorInseridoMuda
      this.setState({valor: resultado})
      Alert.alert("Saque concluído", "Já pode voltar ao menu")



    }

  }


  render() {
    return (
      <View style={styles.container}>
        <Text style={{ backgroundColor: this.state.backColor, fontSize: this.state.fontSizeTitulo, textAlign: "center", marginBottom: 30, }}>
          {this.state.titulo}
        </Text>

        <Text style={{ alignSelf: "center", marginBottom: this.state.txt1margin, fontSize: 20 }}>
          {this.state.txt1}
        </Text>

        <Text style={{ color: this.state.cor, fontSize: this.state.fonttxt2, alignSelf: "center" }}>
          R${this.state.valor}
        </Text>

        <TextInput
          keyboardType='numeric'
          editable={this.state.editable1}
          style={{ borderWidth: this.state.borderWidth1, marginBottom: 20, color: this.state.cor2, borderColor: this.state.borderColor, textAlign: "center" }}
          onChangeText={valor => this.setState({ valorInserido: valor })}>
        </TextInput>

        <TouchableOpacity>
          <Button
            color='red'
            title={this.state.txtBtn1}
            onPress={this.state.func}
          ></Button>
        </TouchableOpacity>

        <View style={styles.view}></View>

        <TouchableOpacity>
          <Button
            color='red'
            title={this.state.txtBtn2}
            onPress={this.state.func2}
          ></Button>
        </TouchableOpacity>

        <View style={styles.view}></View>

        <StatusBar style="light" />
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    //alignItems: 'center',
    justifyContent: 'flex-start',
    backgroundColor: 'black'
  },

  view: {
    marginBottom: 20,


  },

});
