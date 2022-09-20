# Proyecto-Cripto

Una pagina web donde podrás realizar un simulacro de la compra y venta de criptomonedas.



## Para usar la app 

1. Clonar el repositorio
# con https
```
git clone https://
```
2. Crear un entorno virtual
```
En el terminal colocar:

python -m venv env
```
# windows
```
.\env\Scripts\activate
```
# linux / MacOs
```
source ./env/bin/activate
```
3. Instala las dependencias
```
pip install -r requirements.txt
```
4. Configurar las variables de entorno
```
copiar el archivo .env_template dentro de la raiz del programa

asignarles el valor

FLASK_APP=main
FLASK_ENV=development
FLASK_SECRET_KEY=b52eb9cea1044ad0a79b67e7e4f1e4c9
COINAPI_TOKEN = <tu token de coinapi.io>
```
5. Arrancar la App Web
```
flask run
```
