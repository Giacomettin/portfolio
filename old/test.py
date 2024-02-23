import requests

def download_html(url, save_path):
    try:
        # Envia uma solicitação GET para obter o conteúdo da página
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        # Salva o conteúdo HTML no arquivo especificado
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"HTML baixado com sucesso e salvo em: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a página: {e}")

# Exemplo de uso
if __name__ == "__main__":
    url = "https://www.rammaheshwari.com/#projects"
    save_path = "pagina_exemplo2.html"
    download_html(url, save_path)