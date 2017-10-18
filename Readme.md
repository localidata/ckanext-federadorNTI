![Logo Localidata](https://github.com/localidata/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoLocalidata.png)
![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)
ckanext-malaga
==============

En Localidata hemos modificado la extensión original del [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) para la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

Esta extensión actualmente sólo tiene la funcionalidad de Federación. 

Ha sido desarrollada para versiones 2.5 de CKAN, proximamente realizaremos la migración a versiones superiores.

###Instalación de ckanext-malaga

####Descarga de la extensión

* activamos entorno: source /usr/lib/ckan/default/bin/activate
* accedemos al directorio de CKAN: cd /usr/lib/ckan/default/src
* descargamos la extensión: git clone https://github.com/localidata/ckanext-malaga
* accedemos al directorio donde se ha descargado: cd ckanext-malaga
* instalamos la extensión: python setup.py develop
* añadimos la extension 'malaga' dentro de la sección ckan.plugins en el archivo de configuración de CKAN ( /etc/ckan/default/production.ini). 
        
        ckan.plugins = .... malaga
* creamos el directorio donde dejar el fichero para federar: mkdir /usr/lib/ckan/default/src/ckan/ckan/public/recursos/
* cambiamos el usuario del directorio: sudo chown www-data -R /usr/lib/ckan/default/src/ckan/ckan/public/recursos/
* cambiamos los permisos del mismo: sudo chmod u+rwx -R /usr/lib/ckan/default/src/ckan/ckan/public/recursos/

Añadimos estas lineas de configuración en el archivo de configuración de CKAN:

ckan_mlg.federador_file = /usr/lib/ckan/default/src/ckan/ckan/public/recursos/federador.rdf
ckan_mlg.federador_template = /usr/lib/ckan/default/src/ckanext-malaga/ckanext/malaga/theme/local/plantillafederacion.rdf
ckan_mlg.federador_process = generador
ckan_mlg.federador_spatialURI = http://spatialURI.com
ckan_mlg.federador_publisherURI = http://publisherURI.com
ckan_mlg.federador_startDate = 2017-02-27T09:26:44
ckan_mlg.federador_licenseURI = http://licenseURI.com


###Desinstalación de ckanext-malaga

* dentro del directorio 'ckanext-malaga', lanzamos el comando: pip uninstall ckanext-malaga
* borramos la extension 'malaga' dentro de la sección ckan.plugins en el archivo de configuración de CKAN


##Licencia:

Localidata: El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo o mencionanos en el cabecero o pie de página a modo de reconocimiento a Localidata. Gracias! 

![Logo Localidata](https://github.com/localidata/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoLocalidata.png)

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos Abiertos Málaga. Gracias! 

![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

