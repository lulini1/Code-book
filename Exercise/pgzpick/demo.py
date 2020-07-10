import pgzrun

alien = Actor("alien")
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 0

def draw():
    screen.clear()
    screen.fill((128,0,0))
    alien.draw()


def update():
    alien.left = alien.left + 2
    if alien.left > WIDTH:
        alien.left = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("呃")
        set_hurt()
    else:
        print("我闪")

def set_hurt():
    sounds.eep.play()
    alien.image = "alien_hurt"
    clock.schedule_unique(set_normal,1.0)

def set_normal():
    alien.image = "alien"

pgzrun.go()