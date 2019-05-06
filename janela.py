#importa a biblioteca Glu e Glut
"A biblioteca GLUT é responsável pela criação janelas e o tratamento de seus eventos de forma independente do sistema operacional utilizado."

"A biblioteca GLU é responsável pelo mapeamento entre coordenadas de tela e coordenadas do mundo, geração de mipmaps de texturas,"
'desenho de superfícies quadricas, NURBS, tesselation de primitivas poligonais, interpretação dos códigos de erros do OpenGL, diversas funções para facilitar'
'a criação e manipulação de câmera virtuais geralmente de forma mais amigável do que as apresentadas nas funções de base do OpenGL.'
'A biblioteca também provê a renderização automática de objetos tridimensionais como esferas, cilindros e discos.'


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
glutInitWindowPosition(200,200) #posição da janela
window = glutCreateWindow ("Janela OpenGL")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

