import pgzrun
import random

WIDTH = 1280
HEIGHT = 620
TITLE = "Combat Pilot Game"

#estados
game_state = "menu"
sound_enabled = True

#musica
try:
    music.play('bg_music') 
    music.set_volume(0.5)
except:
    print("Aviso: Música não encontrada na pasta 'music'")

#classe do jogador 
class Player(Actor):
    def __init__(self):
        super().__init__('plane1') 
        self.x = 200
        self.y = 300
        self.images = ['plane1', 'plane2']
        self.current_image = 0
        self.anim_timer = 0
        
    def update(self):
        if keyboard.up and self.y > 50:
            self.y -= 5
        if keyboard.down and self.y < HEIGHT - 50:
            self.y += 5
            
        #animação do jogador
        self.anim_timer += 1
        if self.anim_timer > 10:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.anim_timer = 0

    def reset_position(self):
        self.x = 200
        self.y = 300

#classe do inimigo 
class Enemy(Actor):
    def __init__(self):
        super().__init__('bomb1')
        self.x = WIDTH
        self.y = random.randint(50, HEIGHT - 50)
        self.speed = 5 # Velocidade base

        self.images = ['bomb1', 'bomb2'] 
        self.current_image = 0
        self.anim_timer = 0

    def update(self):
        self.x -= self.speed
        if self.x < -50:
            self.x = WIDTH + random.randint(50, 200)
            self.y = random.randint(50, HEIGHT - 50)
            
        self.anim_timer += 1
        if self.anim_timer > 15: 
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.anim_timer = 0
            
    def reset_position(self):
        self.x = WIDTH + random.randint(0, 300) #para as bombas não nascerem juntas
        self.y = random.randint(50, HEIGHT - 50)

#classe missil 
class Missile(Actor):
    def __init__(self):
        super().__init__('missile')
        self.x = -100
        self.active = False
        self.speed = 10

    def fire(self, px, py):
        if not self.active:
            if sound_enabled:
                try:
                    sounds.shoot.play()
                except: pass
            self.active = True
            self.x = px + 20
            self.y = py + 10

    def update(self):
        if self.active:
            self.x += self.speed
            if self.x > WIDTH:
                self.active = False
                
    def reset_position(self):
        self.active = False
        self.x = -100

#criando objetos
start_button = Actor('start_btn', center=(WIDTH/2, HEIGHT/2 - 50))
exit_button = Actor('exit_btn', center=(WIDTH/2, HEIGHT/2 + 50))
sound_button = Actor('sound_on', pos=(50, 50))

player = Player()
missile = Missile()

#quantidade de bombas
enemies = [] 
for i in range(2):
    enemies.append(Enemy())

bg_x = 0

#reset
def reset_game():
    player.reset_position()
    missile.reset_position()

    for enemy in enemies:
        enemy.reset_position()

def draw():
    screen.clear()
    screen.blit("city", (bg_x, 0))
    screen.blit("city", (bg_x + WIDTH, 0))
    
    if game_state == "menu":
        start_button.draw()
        exit_button.draw()
        sound_button.draw()
        screen.draw.text("PILOT COMBAT", center=(WIDTH/2, 150), fontsize=60, color="white")
        
    elif game_state == "playing":
        player.draw()
        
        for enemy in enemies:
            enemy.draw()
            
        if missile.active:
            missile.draw()
        screen.draw.text("PRESS SPACE TO SHOOT", (WIDTH/2 - 100, HEIGHT - 40), color="white")

def update():
    global bg_x, game_state
    
    #ilusão de infinito
    bg_x -= 1
    if bg_x <= -WIDTH:
        bg_x = 0
        
    if game_state == "playing":
        player.update()
        missile.update()
        
        for enemy in enemies:
            enemy.update()
            
            #colisão missil bomba especifica
            if missile.active and missile.colliderect(enemy):
                if sound_enabled:
                    try:
                        sounds.explosion.play()
                    except: pass
                
                #reseta so a bomba especifica
                enemy.x = WIDTH + random.randint(50, 200)
                enemy.y = random.randint(50, HEIGHT - 50)
                missile.active = False
            
            #game over
            if player.colliderect(enemy):
                print("GAME OVER - Retornando ao Menu")
                reset_game() 
                game_state = "menu"

        if keyboard.space:
            missile.fire(player.x, player.y)

def on_mouse_down(pos):
    global game_state, sound_enabled
    
    if game_state == "menu":
        if start_button.collidepoint(pos):
            reset_game()
            game_state = "playing"
            
        if exit_button.collidepoint(pos):
            quit()
            
        if sound_button.collidepoint(pos):
            sound_enabled = not sound_enabled
            if sound_enabled:
                sound_button.image = 'sound_on'
                try: music.unpause()
                except: pass
            else:
                sound_button.image = 'sound_off'
                try: music.pause()
                except: pass

pgzrun.go()