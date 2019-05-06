from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


def inicio():
    glClearColor(0.737255,0.560784 ,0.560784, 0)
    glClearDepth(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
obj_rot = 0.0
obj_rot_speed = 1.0


def tela():
    global obj_rot
    global obj_rot_speed
   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

   
    glRotate(obj_rot, 2.0, 1.0, 2.0) #gira a estrela
    glTranslatef(-0.1, -0.5, 0.1) #posição da estrela na janela

     #desenha estrela
  
    glBegin(GL_TRIANGLES)
     
    glColor3f(1.00, 0.11, 0.68)


    glVertex3f(-0.60, 0.77, 0)
    glVertex3f(-0.42, 0.77, 0)
    glVertex3f(-0.58, 0.68, 0);

    #2 triangulo

    
    glVertex3f(-0.64, 1, 0);
    glVertex3f(-0.68, 0.77, 0);
    glVertex3f(-0.60, 0.77, 0);

    # 3 triangulo
    
    glVertex3f(-0.68, 0.77, 0);
    glVertex3f(-0.7, 0.68, 0);
    glVertex3f(-0.86, 0.77, 0);

    #4 triangulo
    
    glVertex3f(-0.64, 0.63, 0);
    glVertex3f(-0.7, 0.68, 0);
    glVertex3f(-0.82, 0.43, 0);

    #5 triangulo
    
    glVertex3f(-0.64, 0.63, 0);
    glVertex3f(-0.58, 0.68, 0);
    glVertex3f(-0.51, 0.43, 0);

    glEnd()
    
 
    obj_rot += obj_rot_speed #faz a estrela "mexer"
  
    glFlush()
    time.sleep(1/40.0)#controla a velocidade da rotação da estrela

if __name__ == '__main__': #executa o código
    glutInit()
    glutCreateWindow("ROTAÇÃO")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutDisplayFunc(tela)
    glutIdleFunc(tela)
    inicio()
    glutMainLoop()
    
