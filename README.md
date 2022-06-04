<h1 align="center">
    <img alt="Event QR Code" title="Event QR Code" src="setup/static/images/qr-code.png" width="100px" />
</h1>

<h4 align="center">
    Event QR Code
</h4>

## 💻 Projeto
**Projeto para gerar QR Code e registrar participação em eventos. Ideal para usar com celular e ler QR Code. Salva informações dos eventos em que o partcipante esteve presente.**


### Run
```sh
# clonar repositório
git clone https://github.com/andre23arruda/event-qr-code

# Entrar na pasta
cd event-qr-code

# Renomear env_example.py para env.py
cp setup/env_example.py setup/env.py

# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
. activate.sh
# ou . venv/Scripts/activate
# ou . venv/bin/activate
# ou source venv/Scripts/activate

# Instalar os pacotes necessários
pip install -r requirements.txt

# Executar as migrações
python manage.py migrate

# Criar superusuário (poderá fazer login e entrar no admin)
. create_su.sh
# username -> teste
# password -> teste1234

# Carregar fixtures (exemplo para colocar no banco de dados)
python manage.py loaddata events participants

# Gerar qr codes
python generate_codes.py

# Start
. run.sh
```

## Agora leia um dos QR Codes gerados e teste a aplicação

## Acesse __/admin__ para cadastrar __Eventos__ e __Participantes__

## Explore ou altere do jeito que achar melhor!!
