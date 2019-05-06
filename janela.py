#importa a biblioteca Glu e Glut
"A biblioteca GLUT � respons�vel pela cria��o janelas e o tratamento de seus eventos de forma independente do sistema operacional utilizado."

"A biblioteca GLU � respons�vel pelo mapeamento entre coordenadas de tela e coordenadas do mundo, gera��o de mipmaps de texturas,"
'desenho de superf�cies quadricas, NURBS, tesselation de primitivas poligonais, interpreta��o dos c�digos de erros do OpenGL, diversas fun��es para facilitar'
'a cria��o e manipula��o de c�mera virtuais geralmente de forma mais amig�vel do que as apresentadas nas fun��es de base do OpenGL.'
'A biblioteca tamb�m prov� a renderiza��o autom�tica de objetos tridimensionais como esferas, cilindros e discos.'


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800,500 #tamanho da tela

def draw():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glutSwapBuffers()

glutInit() #inicia GLUT
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height) #seta o tamanho da janela
glutInitWindowPosition(200,200) #posi��o da janela
window = glutCreateWindow ("Janela OpenGL")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

