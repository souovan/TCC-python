Aplicação feita no framework Python Flask com base na documentação do meu [TCC](https://github.com/souovan/TCC)

# Para executar a aplicação Flask

Com o banco de dados já em execução:

```sh
git clone https://github.com/souovan/TCC-python.git && \
##### Corrigir
cd TCC-python/python-flask/src/ && \

python3 -m venv venv && \
source venv/bin/activate && \

pip install -r requirements.txt && \

flask run
```

# Para executar em container com Podman

```bash
podman pull docker.io/souovan/apptccpython && \
podman run -it -d --name apptccpython -p 5000:5000 docker.io/souovan/apptccpython && \
podman exec -it apptccpython bash && \
```

```bash
# Quando dentro do container executar
cd TCC-python\python-flask\src && \
source venv/bin/activate && \
flask run -h 0.0.0.0 -p 5000
```

# Para executar em container com Docker

```bash
sudo docker pull docker.io/souovan/apptccpython && \
sudo docker run -it -d --name apptccpython -p 5000:5000 docker.io/souovan/apptccpython && \ 
sudo docker exec -it apptccpython bash && \
```
```bash
# Quando dentro do container executar
cd TCC-python\python-flask\src && \
source venv/bin/activate && \
flask run -h 0.0.0.0 -p 5000
```

## Para uso em containers

```bash
# configurar conexões com banco de dados 
cd TCC-python/python-flask/src/
# editar a linha "app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/postgres'" do arquivo app.py com a conexão desejada (neste caso, se usar em conjunto com o postgresql também como container editar para:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@<IP_da_maquina_executando_postgresql_container>:<porta>/postgres'
```

## Para atualizar o app

```bash
# Dentro do container executar
cd TCC-python && \
git pull
```
