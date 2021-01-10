CONFIGURAR EL ENTORNO
	Para instalar las dependencias del proyecto y poder ejecutarlo debes ejecutar lo siguiente en una terminal correctamente configurada con conda:

		-Si tienes windows ejecuta:
			conda env create -f windows-environment.yml
		-En otro caso (no aseguramos que funcione en otros sistemas operativos):
			conda env create -f cross-plataforms-environment.yml

	En ambos casos se creara un nuevo conda enviroment donde podras ejecutar correctamente el proyecto.


EJECUTAR:
	Puedes ejecutar el proyecto con el siguiente comando:
		python src/optimitation_problem.py
