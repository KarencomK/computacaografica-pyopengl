from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
angle=[0]
def inicio():
    glClearColor(1.0, 0.5, 0.0, 0.0) #cor de fundo da janela

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(50, 1, 0.15, 50) #molda o circulo
    gluLookAt(5,5,5, 0,0,0,0, 5,0) #centraliza o circulo
    glEnable(GL_DEPTH_TEST)



#angle = [0]
def escala(sun_dist, radius, angle, r,g,b): #sun=tamanho da traslação radius=tamanho da forma 
      glLoadIdentity()
      glColor(r,g,b)
      glRotate(angle, 0,0,0) 
      glTranslate(sun_dist,2,3) #escala : 2 circulo  3 angulo do circulo quando aproxima
      glutSolidSphere(radius, 50,50)
    

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    escala(2, 0.5, angle[0], 1.0, 0.25, 0)
    angle[0] += 0.03 

   
    glutSwapBuffers()

glutInit( ) #inicia GLUT (janela)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 800) #set o tamanho da janela
glutCreateWindow("ESCALA")
glutDisplayFunc(tela)
glutIdleFunc(tela)
inicio() #inica a função 
glutMainLoop()

      


