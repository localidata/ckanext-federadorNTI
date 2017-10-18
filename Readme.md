![Logo Localidata](https://github.com/localidata/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoLocalidata.png)
![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


ckanext-malaga
==============

En Localidata hemos modificado la extensión original del [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) para la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

Esta extensión actualmente sólo tiene la funcionalidad de Federación. 

Ha sido desarrollada para versiones 2.5 de CKAN, proximamente realizaremos la migración a versiones superiores.

#### Descarga y configuración de la extensión

- activamos entorno: source /usr/lib/ckan/default/bin/activate
- accedemos al directorio de CKAN: cd /usr/lib/ckan/default/src
- descargamos la extensión: git clone https://github.com/localidata/ckanext-malaga
- accedemos al directorio donde se ha descargado: cd ckanext-malaga
- instalamos la extensión: python setup.py develop
- añadimos la extension 'malaga' dentro de la sección ckan.plugins en el archivo de configuración de CKAN ( /etc/ckan/default/production.ini). 
        
        ckan.plugins = .... malaga
- creamos el directorio donde dejar el fichero para federar: mkdir /usr/lib/ckan/default/src/ckan/ckan/public/recursos/
- cambiamos el usuario del directorio: sudo chown www-data -R /usr/lib/ckan/default/src/ckan/ckan/public/recursos/
- cambiamos los permisos del mismo: sudo chmod u+rwx -R /usr/lib/ckan/default/src/ckan/ckan/public/recursos/

Añadimos estas lineas de configuración en el archivo de configuración de CKAN:

- ckan_mlg.federador_file = /usr/lib/ckan/default/src/ckan/ckan/public/recursos/federador.rdf
- ckan_mlg.federador_template = /usr/lib/ckan/default/src/ckanext-malaga/ckanext/malaga/theme/local/plantillafederacion.rdf
- ckan_mlg.federador_process = generador
- ckan_mlg.federador_spatialURI = http://spatialURI.com
- ckan_mlg.federador_publisherURI = http://publisherURI.com
- ckan_mlg.federador_startDate = 2017-02-27T09:26:44
- ckan_mlg.federador_licenseURI = http://licenseURI.com

#### Explicación de los parámetros y uso

Esta extensión funciona de la siguiente manera:
	
	a) Se le invoca a través de la URL del portal más el valor del parámetro ckan_mlg.federador_process
	b) Una vez llamada ejecuta la plantilla definida en ckan_mlg.federador_template. Esta plantilla itera por todos los Conjuntos de Datos y Recursos formando un RDF tal y como está especificado en dicha plantilla
	c) El valor de algunos campos de este RDF se especifican con parametros definidos en el fichero de configuración. Estos valores dependen de cada organismo. 
	d) Una vez acabado el rdf final se guarda en la ruta especificada en ckan_mlg.federador_file.
	e) Para que otro portal (como datos.gob.es) nos federe leyendo este RDF debemos proporcionarle esta url: http://urlDeNuestroPortal/recursos/federador.rdf

A continuación explicamos todos los parámetros que se utilizan en esta extensión:

- ckan_mlg.federador_file: fichero final que va contener toda la información para la federación. Se genera cada vez que se finaliza el proceso de federación. La ruta completa debe existir y tener permisos.
- ckan_mlg.federador_template: ruta donde se encuentra la plantilla rdf para generar el RDF que se federará.
- ckan_mlg.federador_process: Url que utilizamos comenzar la generación del fichero. Si escribimos 'generador', la url será: http://datosabiertos.localidata.com/generador
- ckan_mlg.federador_spatialURI: URI espacial que más se aproxima a nuestro municipio o residencia. Ejemplo: http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Madrid
- ckan_mlg.federador_publisherURI: URI de nuestro organismo. Ejemplo: http://datos.gob.es/recurso/sector-publico/org/Organismo/L01281230
- ckan_mlg.federador_startDate: Fecha de alta en datos.gob.es. El formato debe ser YYYY-MM-DDTHH:MI:SS Ejemplo: 2017-02-27T09:26:44
- ckan_mlg.federador_licenseURI: URL donde se encuentra la página con la licencia de nuestros datos. Ejemplo: http://datosabiertos.localidata.com/pages/aviso-legal

#### Cómo securizar la url del ckan_mlg.federador_process

Es importante no dejar expuesta la URL que lanza la generación del RDF. En caso de tener muchos datos, puede tardar varios minutos en generarse y si se lanzan muchas peticiones podría ser problemático.

Proximamente ampliaremos esta información.

### Desinstalación de ckanext-malaga

* dentro del directorio 'ckanext-malaga', lanzamos el comando: pip uninstall ckanext-malaga
* borramos la extension 'malaga' dentro de la sección ckan.plugins en el archivo de configuración de CKAN


## Licencia:

![Logo Localidata](https://github.com/localidata/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoLocalidata.png)

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo o mencionanos a modo de reconocimiento. Gracias! 

![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos Abiertos Málaga. Gracias! 



