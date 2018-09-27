![Logo Localidata](https://raw.githubusercontent.com/localidata/ckanext-federadorNTI/master/ckanext/malaga/public/images/logoLocalidata.png)


ckanext-federadorNTI
============== 

En Localidata hemos modificado la extensión original del [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) para la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

Esta extensión actualmente sólo tiene la funcionalidad de Federación. 

Ha sido desarrollada para la version 2.7 de CKAN, proximamente realizaremos la migración a versiones superiores.

#### Descarga y configuración de la extensión

- activamos entorno: source /usr/lib/ckan/default/bin/activate
- accedemos al directorio de CKAN: cd /usr/lib/ckan/default/src
- descargamos la extensión: git clone https://github.com/localidata/ckanext-federadorNTI.git
- accedemos al directorio donde se ha descargado: cd ckanext-federadorNTI
- instalamos la extensión: python setup.py develop

		En este punto a veces aparece este error:  [Errno 13] Permission denied: '/usr/lib/ckan/default/lib/python2.7/site-packages/test-easy-install-1482.write-test'
		Esto ocurre porque se ha instalado CKAN como administrador, y hay que cambiar el propietario de este directorio '/usr/lib/ckan/default/lib/python2.7/site-packages'		
		Lo arreglamos con el comando 'sudo chown -R $USER /usr/lib/ckan/default/lib/python2.7/site-packages'

- añadimos la extension 'federadorNTI' dentro de la sección ckan.plugins en el archivo de configuración de CKAN ( /etc/ckan/default/production.ini). 
        
        ckan.plugins = .... federadorNTI

Añadimos estas lineas de configuración en el archivo de configuración de CKAN:

- ckan_mlg.federador_spatialURI = http://spatialURI.com
- ckan_mlg.federador_publisherURI = http://publisherURI.com
- ckan_mlg.federador_startDate = 2017-02-27T09:26:44
- ckan_mlg.federador_licenseURI = http://licenseURI.com

Para generar el RDF que va a ser consumido por datos.gob.es tenemos que utilizar la siguiente URL:

http://nuestroCKAN/plantillafederacion.rdf

Esta plantilla se encuentra situada en la ruta: /usr/lib/ckan/default/src/ckanext-federadorNTI/ckanext/malaga/theme/templates

Podemos renombrarla y cambiar su contenido según nos convenga.

#### Explicación de los parámetros

A continuación explicamos todos los parámetros que se utilizan en esta extensión:

- ckan_mlg.federador_spatialURI: URI espacial que más se aproxima a nuestro municipio o residencia. Ejemplo: http://datos.gob.es/recurso/sector-publico/territorio/Provincia/Madrid
- ckan_mlg.federador_publisherURI: URI de nuestro organismo. Ejemplo: http://datos.gob.es/recurso/sector-publico/org/Organismo/L01281230
- ckan_mlg.federador_startDate: Fecha de alta en datos.gob.es. El formato debe ser YYYY-MM-DDTHH:MI:SS Ejemplo: 2017-02-27T09:26:44
- ckan_mlg.federador_licenseURI: URL donde se encuentra la página con la licencia de nuestros datos. Ejemplo: http://datosabiertos.localidata.com/pages/aviso-legal

#### ¿Debo securizar la url?

Sí, deberías. Lo mejor es que esa url sólo pueda ser invocada desde dentro del propio servidor.

Un buen truco es tener un script parecido a este:
		
		$(curl http://localhost/plantillafederacion.rdf -o /usr/lib/ckan/default/src/ckanext-federadorNTI/ckanext/malaga/public/federacion.rdf)

Con este script descargamos el contenido que se genera al ejecutar la plantilla en una ruta física dentro del propio plugin.

Se puede acceder al RDF generado con esta URL: http://nuestroCKAN/federacion.rdf
		
### Actualización de ckanext-federadorNTI

* activamos entorno: source /usr/lib/ckan/default/bin/activate
* cd /usr/lib/ckan/default/src/ckanext-federadorNTI
* python setup.py develop --uninstall
* descargamos la extensión actualizada: git pull
* instalamos la extensión de nuevo: python setup.py develop


### Desinstalación de ckanext-federadorNTI

* activamos entorno: source /usr/lib/ckan/default/bin/activate
* cd /usr/lib/ckan/default/src/ckanext-federadorNTI
* python setup.py develop --uninstall
* borramos la extension 'federadorNTI' dentro de la sección ckan.plugins en el archivo de configuración de CKAN


## Licencia:

![Logo Localidata](https://raw.githubusercontent.com/localidata/ckanext-federadorNTI/master/ckanext/malaga/public/images/logoLocalidata.png)

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo o mencionanos a modo de reconocimiento. Gracias! 

![Logo datos abiertos Málaga](https://raw.githubusercontent.com/damalaga/ckanext-malaga/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos Abiertos Málaga. Gracias! 



