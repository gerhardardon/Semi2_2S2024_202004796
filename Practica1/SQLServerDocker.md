## Pasos para instalar sql server desde docker 
Descargar la imagen de docker 
```
sudo docker pull mcr.microsoft.com/mssql/server
```
Imiciar el contenedor aceptando todos sus permisos y seteando la nueva contraseña, Ojo la contraseña debe tener 8 caracteres, mayusculas y caracteres especiales o no correra el contenedor 
```
sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword123' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server
```
Luego verificar con
```
sudo docker ps 
```
