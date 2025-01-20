from textblob import TextBlob

class AnalisadorSentimentos:
    def __init__(self, texto):
        self.texto = texto
        self.blob = TextBlob(texto)

    def analisar_sentimento(self):
        """Analisa o sentimento do texto"""
        # O TextBlob retorna um valor de polaridade -1 (negativo) e 1 (positivo)
        polaridade = self.blob.sentiment.polarity

        if polaridade > 0:
            return "Positivo"
        elif polaridade < 0:
            return "Negativo"
        else:
            return "Neutro"
        
def main():
    texto = input("Digite o texto para análise de sentimento: ")
    analisador = AnalisadorSentimentos(texto)

    print("Analisando o sentimento do texto...")
    sentimento = analisador.analisar_sentimento()
    print(f"O sentimento do texto é: {sentimento}")

if __name__ == "__main__":
    main()