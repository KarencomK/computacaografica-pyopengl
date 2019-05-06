from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicio():
    glClearColor(0.0, 0.5, 0.5, 0) #cor de fundo da janela

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(50, 1, 0.15, 50) #molda o circulo
    gluLookAt(5,5,5, 0,0,0,0, 5,0) #centraliza o circulo
    glEnable(GL_DEPTH_TEST)

angle = [0]
def translacao(sun_dist, radius, angle, r,g,b): #sun=tamanho da traslação radius=tamanho da forma 
      glLoadIdentity()
      glColor(r,g,b)
      glRotate(angle, 1,1,1) # rotação do circulo
      glTranslate(sun_dist,0,0)
      glutSolidSphere(radius, 50,50)
    

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #translação
    translacao(2, 0.5, angle[0], 0,5,1)
    angle[0] += 0.03 #velocidade da translação
    
   
    glutSwapBuffers()

glutInit( ) #inicia GLUT (janela)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600) #set o tamanho da janela
glutCreateWindow("TRANSLAÇÃO")
glutDisplayFunc(tela)
glutIdleFunc(tela)
inicio() #inica a função 
glutMainLoop()

      


