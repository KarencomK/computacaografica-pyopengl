from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicio():
    glClearColor(0.1, 0.0, 0.1, 0) #cor de fundo da janela

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(40, 1, 0.5, 50) 
    gluLookAt(5,5,5, 0,0,0,0, 5,0) #molda a forma do circulo
    glEnable(GL_DEPTH_TEST)
    
def tela():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glColor(1.0, 0.0, 1.0, 0.0) #cor do circulo
    glutSolidSphere(2,30,30)   #tamanho do circulo
    glutSwapBuffers()

glutInit( ) #inicia GLUT
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500) #set o tamanho da janela
glutCreateWindow("CIRCULO")
glutDisplayFunc(tela)
glutIdleFunc(tela)
inicio() #inica a função 
glutMainLoop()

      


