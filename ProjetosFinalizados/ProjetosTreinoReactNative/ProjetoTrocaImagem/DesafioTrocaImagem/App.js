import React from 'react';
import { Button, Image, StatusBar, StyleSheet, Text, View } from 'react-native';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      imagem: "https://picsum.photos/200",
    }
  }

  cliqueBotao1 = _ => {
    const imagem = "https://picsum.photos/200"
    this.setState({ imagem });

  }

  cliqueBotao2 = _ => {
    const imagem2 = "https://picsum.photos/201"
    this.setState({ imagem: imagem2 });

  }

  cliqueBotao3 = _ => {
    const imagem3 = "https://picsum.photos/202"
    this.setState({ imagem: imagem3 });
  }

  render() {
    return (
      <View style={styles.container}>
        <Image
          resizeMode="contain"
          style={styles.img}
          source={{ uri: this.state.imagem }}
        ></Image>

        <Button
          color='red'
          title={"Imagem 1"}
          onPress={this.cliqueBotao1}
        ></Button>

        <View style={styles.view}></View>

        <Button
          color='red'
          title={"Imagem 2"}
          onPress={this.cliqueBotao2}
        ></Button>

        <View style={styles.view}></View>

        <Button
          color='red'
          title={"Imagem 3"}
          onPress={this.cliqueBotao3}
        ></Button>





        <StatusBar style="light" />
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  img: {

    width: 300,
    height: 200,
    margin: 20,


  },
  view: {
    marginBottom: 20,


  }


});
