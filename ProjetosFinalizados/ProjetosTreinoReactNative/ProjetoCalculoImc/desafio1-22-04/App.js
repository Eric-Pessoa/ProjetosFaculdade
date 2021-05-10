import { StatusBar } from 'react-native';
import React from 'react';
import { Alert,TextInput, Button, StyleSheet, Text, View } from 'react-native';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      txtPeso: "",
      txtAltura: "",
    };
  }


  botaoCalcular = () => {
    const {txtPeso, txtAltura} = this.state;
    const peso = parseFloat(txtPeso);
    const altura = parseFloat(txtAltura);
    if(Number.isNaN(peso) || Number.isNaN(altura)){
      Alert.alert("Erro", "Preencha os campos corretamente.");
      return;
      
    }
    const imc = peso / (altura * altura);
    let categoria = "";
    if(imc<18.5) {
      categoria = "Abaixo do peso";
    } else if(imc <25) {
      categoria = "Peso normal";
    } else if(imc<30) {
      categoria = "Acima do peso";
    }
    else {
      categoria = "Obesidade"
    }

    const mensagem = `IMC = ${imc.toFixed(1)}\n${categoria}`;
    Alert.alert("Índice de massa corporal: ", mensagem);


  }

  render() {
    return (
      <View style={styles.container}>
        <TextInput
          placeholder="Informe seu peso"
          keyboardType="numeric"
          onChangeText={peso => this.setState({ txtPeso: peso })}
          style={styles.inputStyle} />

        <TextInput
          placeholder="Informe seu peso"
          keyboardType="numeric"
          onChangeText={peso => this.setState({ txtAltura: altura })}
          style={styles.inputStyle} />


        <Button title="Calcular" 
          onPress={this.botaoCalcular}/>

        <StatusBar style="auto" />
      </View>

    );
  }


}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputStyle: {
    borderColor: 'gray',
    borderWidth: 1,
    height: 40,
    paddingHorizontal: 16,
    marginBottom: 20
  }
});
