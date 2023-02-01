# MenuHub

A startup (Mundo dos Programas) está projetando um produto 
denominado MenuHub que permitirá a um restaurante a registrar seu menu de pratos. 
A pessoa responsável pelo restaurante deverá fornecer o seu e-mail, 
a sua senha e o nome do restaurante pelo qual ele é responsável. E para cada prato 
do restaurante, o nome do prato, a categoria (entrada, principal e sobremesa) 
e o preço.

## Nome(s) do(s) programador(es)

```bash
Marcos Keller da Fonseca
```

## Framework(s) Utilizado(s)

```python
Flask
```

## Modo de Execução

```python

1º - Realize o Clone do Projeto

-->git clone https://github.com/marcoskeller/menu_hub.git

2º - Crie e Ative o ambiente virtual com os comandos abaixo

-->python3 -m venv venv
--->venv/Scripts/activate

3º -  Realize a instalação das dependências necessárias do projeto com o comando abaixo

-->pip install -r requirements.txt

4º - Realize a criação e execução do ambiente de banco de dados do projeto com os comandos abaixo

-->flask db init
--->flask db migrate -m "First migration"
---->flask db upgrade

5º - Inicialize o Flask

-->flask run

6º - Abra seu navegador e cole o endereço abaixo

-->http://127.0.0.1:5000/login

```
