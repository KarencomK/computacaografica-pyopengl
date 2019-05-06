from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


def inicio():
    glClearColor( 0.258824,0.435294 , 0.258824, 0)
    glClearDepth(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
obj_rot = 0.2

obj_rot_speed = 1.0


def tela():
    global obj_rot
    global obj_rot_speed
   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glRotatef(obj_rot,0.0,0.0,0.1) #gira a estrela
    glTranslatef(0.5, 0.0, 0.0) #posiÁ„o da estrela na janela
    
     #desenha estrela
  
    glBegin(GL_TRIANGLES)
     
    glColor3f(0.137255, 0.556863, 0.137255)


    glVertex3f(-0.60, 0.77, 0)
    glVertex3f(-0.42, 0.77, 0)
    glVertex3f(-0.58, 0.68, 0);

    #2 triangulo

     
    glColor3f( 0.196078,0.8,  0.196078)
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
    #glPopAttrib()
 
    obj_rot += obj_rot_speed #faz a estrela "mexer"
  
    glFlush()
    time.sleep(2/100.0)#controla a velocidade da rota√ß√£o da estrela

if __name__ == '__main__': #executa o c√≥digo
    glutInit()
    glutCreateWindow("ROTACIONAR")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutDisplayFunc(tela)
    glutIdleFunc(tela)
    inicio()
    glutMainLoop()
    
