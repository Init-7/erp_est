#Guia de desarrollo con Frappe Framework

Guia de primeros pasos para el desarrollo de modulos de un ERP con el framework Frappe.

La siguiente guia esta elaborada para ser utilizada en un servidor con CentOS 7 Minimal.

Documentacion basada en http://frappe.github.io/frappe/user/tutorial/

##Instalacion

1. Asegurese de tener una conexion a internet estable, ya que al fallar la descarga puede fallar toda la instalacion

2. Como usuario normal con privilegios de administracion (no root) ejecute:

> wget https://raw.githubusercontent.com/frappe/bench/master/install_scripts/setup_frappe.sh

> sudo bash setup_frappe.sh

El script anterior crea:

* **bench-repo** : Directorio que almacena la herramienta *bench* para ser utilizada por el usuario que instalo la aplicacion. Esta herramienta permite desarrollar sitios y aplicaciones con Frappe y servir un sitio desarrollado con Frappe.

* **frappe-bench** : Directorio para la creacion de app de frappe con la aplicacion ERP Next y un sitio preinstalados y configurados.

* **frappe_passwords.txt** : Archivo con las claves Frappe, root de Mariadb y Administrator del sitio preconfigurado.


##Modo Desarrollador

Editar el archivo ./frappe_bench/sites/[site]/site_config.json y agregar:

>{

>"db_name": "....",

>"db_password": "....",

>"developer_mode": "1",

>"disable_website_cache":"1",

>"logging": "2"

>}


##Utilizando bench

>**bench new-app nombre_app**

Crea una nueva aplicacion


>**bench new-site nombre_del_sitio**

Crea un nuevo sitio


>**bench use nombre_del_sitio**

Utilizar el nuevo sitio creado


>**bench install-app nombre_de_la_app**

Instala la aplicacion creada en el sitio


>**bench start**

Inicia el servidor, usando el ambiente virtual de python ubicado en ./frappe-bench/env en la direccion http://localhost:8000/


>**bench mysql**

Permite acceder a mysql directamente sin el uso de credenciales. Se utilizara la base de datos del sitio que esta siendo utilizado.

##Modelos

Los modelos son creados y administrados a travez de una interfaz web en el menu de desarrollador.


##Vistas


##Controladores

##Secuencias perzonalizadas

Sirven para realizar operaciones dentro de las páginas, gatilladas por eventos de usuario.
La forma de crear estas operaciones es creando documentos en formato JS.

Los siguientes son enlaces que llevan a documentación acerca de creación de scripts.

https://frappe.github.io/frappe/user/tutorial/form-client-scripting.html
http://frappe.github.io/erpnext/user/manual/en/customize-erpnext/custom-scripts/

Para crear un nuevo script dirigirse a Configuración-> Personalizar-> Secuencia Personalizada

Estos scripts son guardados en ficheros .JSON.

##Doctypes

El modelo en Frappe es representado por Doctypes, estos documentos representan una nueva tabla en una base de datos.
Cada doctype está asociado a un módulo y puede ser clasificado como:

* Documento
* Configuración
* Sistema

###Creación de Doctypes

Para crear un nuevo doctype dirigirse a Configuración -> Personalizar -> Doctype

En este nuevo formulario se deben insertar los campos que tendrá este nuevo Doctype.

##Control de versiones e integración

Es necesario la creación de un repositorio para cada APP creada con "**bench new-app**" dentro de frappe-bench. Las aplicaciones deben ser comunes para todos los desarrolladores, con el miemo nombre y repositorio remoto, aunque se mantiene la recomendación de trabajar en ramas independientes.

### Versionado de una nueva aplicación

> cd ./apps/demoest

Primero es necesario moverse al directorio de la aplicación, en este ejemplo, se utiliza la aplicación demoest

> git init

###Instalar ERPNext en una aplicación.

Luego de tener instalado ErpNext localmente:

> bench --site [nombre de sitio] install-app erpnext

ERPnext exige que al instalarse en un sitio, este debe contar con una instalación fresca, en caso de que esto no se cumpla se puede reinstalar nuevamente el sitio:

> bench --site [nombre de sitio] reinstall


