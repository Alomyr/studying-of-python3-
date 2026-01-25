import requests


def verifcar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            return True, "Site esta acessivel!"
        else:
            return False, f"Site Retornou o statos {resposta.status_code}"
    except requests.exceptions.RequestException as errors:
        return False, str(errors)


url = "https://pudim.com.br/"
esta_online, messagem = verifcar_site(url)
print(f"O site {url} | Online: {esta_online} | Mensagem: {messagem}")
