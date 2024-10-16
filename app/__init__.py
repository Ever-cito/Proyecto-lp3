from flask import Flask

app = Flask(__name__)
    
# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod #ciudad
from app.rutas.referenciales.paises.pais_routes import paimod #pais
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod  #nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupmod  #ocupacion
from app.rutas.referenciales.estado_civil.estado_civil_routes import estacivmod  #estado civil
from app.rutas.referenciales.sexo.sexo_routes import sexmod  #sexo
from app.rutas.referenciales.estado_cita.estado_cita_routes import estacitmod  #estado de la cita
from app.rutas.referenciales.diagnostico.diagnostico_routes import diagmod  # diagnostico
from app.rutas.referenciales.turno.turno_routes import turmod # turno
from app.rutas.referenciales.tratamiento.tratamiento_routes import traumod # tratamiento




# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad') #ciudad
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises') #paises
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')  #nacionalidad
app.register_blueprint(ocupmod, url_prefix=f'{modulo0}/ocupacion')  #ocupacion
app.register_blueprint(estacivmod, url_prefix=f'{modulo0}/estadocivil')  #estado civil
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')  #sexo
app.register_blueprint(estacitmod, url_prefix=f'{modulo0}/estadocita')  #estado de la cita
app.register_blueprint(diagmod, url_prefix=f'{modulo0}/diagnostico')  # diagnostico
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')  # turno
app.register_blueprint(traumod, url_prefix=f'{modulo0}/tratamiento')  # tratamiento


#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
#pais
from app.rutas.referenciales.paises.pais_api import paisapi

#nacionalidad
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi
#nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_api import ocupapi
#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_api import estacivapi
#sexo
from app.rutas.referenciales.sexo.sexo_api import sexapi
#estado de la cita
from app.rutas.referenciales.estado_cita.estado_cita_api import estacitapi

# diagnostico
from app.rutas.referenciales.diagnostico.diagnostico_api import diagapi  
# turno
from app.rutas.referenciales.turno.turno_api import turnoapi 
# tratamiento
from app.rutas.referenciales.tratamiento.tratamiento_api import trauapi 




# APIS v1
#Ciudad
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

#Pais
version1 = '/api/v1'
app.register_blueprint(paisapi, url_prefix=version1)




#nacionalidad
version1 = '/api/v1'
app.register_blueprint(nacioapi, url_prefix=version1)

#ocupacion
version1 = '/api/v1'
app.register_blueprint(ocupapi, url_prefix=version1)


#Estado civil
version1 = '/api/v1'
app.register_blueprint(estacivapi, url_prefix=version1)

#sexo
version1 = '/api/v1'
app.register_blueprint(sexapi, url_prefix=version1)

#Estado de la cita
version1 = '/api/v1'
app.register_blueprint(estacitapi, url_prefix=version1)


# Diagnóstico
version1 = '/api/v1'
app.register_blueprint(diagapi, url_prefix=version1)  # diagnóstico


# Turno
version1 = '/api/v1'
app.register_blueprint(turnoapi, url_prefix=version1) 



# Turno
version1 = '/api/v1'
app.register_blueprint(trauapi, url_prefix=version1) 








