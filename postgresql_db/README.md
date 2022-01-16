# Configurando o banco de dados Postgres

> ```
> postgres user: postgres
> postgres password: password
> pgadmin user: van@van.com
> pgadmin password: password
> ```

```bash
git clone https://github.com/souovan/tcc-python.git && \
cd tcc-python/postgresql_db/ && \
psql -U postgres -f python_flask_fastapi_db.sql
```

# Para executar em container com Podman

```bash
# Execute os comandos para rodar o container e configura-lo
sudo podman pull docker.io/souovan/postgresqltccpython && \
podman run -it -d --name postgresqltccpython -p 8080:80 -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres docker.io/souovan/postgresqltccpython && \
podman exec -it postgresqltccpython /etc/init.d/apache2 start
```

```bash
# Execute para importar as tabelas do banco
git clone https://github.com/souovan/tcc-python.git && \
cd tcc-python/postgresql_db/ && \
psql -U postgres -f python_flask_fastapi_db.sql
```