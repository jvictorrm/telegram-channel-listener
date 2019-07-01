# telegram-listener

### Como desenvolver ?

1.  Clone o repositório.
2.  Crie um virtualenv com Python 3.x.x.
3.  Ative o virtualenv.
4.  Instale as dependências.

```
git clone https://<usuario>@bitbucket.org/jvictorrm/telegram-listener.git telegram-listener
cd telegram-listener
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Como executar ?

```
python3 main.py
```

---

### Observações

> No arquivo `config.ini` há duas chaves que merecem destaque:

```ini
api_id = VALOR
api_hash = VALOR
```
> O valor destas chaves é adquirido através do cadastro feito no [site de autorização de uso da API do Telegram][auth-telegram].

[auth-telegram]: https://my.telegram.com/