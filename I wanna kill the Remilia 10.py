import pygame
import time
import random

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
youlose = pygame.font.SysFont('Comic Sans MS', 30)
youwin = pygame.font.SysFont('Comic Sans MS', 30)
za_warudo = pygame.font.SysFont('Comic Sans MS', 30)

display_width = 1200
display_height = 800

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('I wanna kill the Remilia 10')

icon = pygame.image.load('Icon.jpg')
pygame.display.set_icon(icon)
bg = pygame.image.load('pixel-art.jpg')
sakuya_st = pygame.image.load('SakuyaStand.png')
sakuya_r1 = pygame.image.load('SR1.png')
sakuya_r2 = pygame.image.load('SR2.png')
sakuya_r3 = pygame.image.load('SR3.png')
sakuya_r4 = pygame.image.load('SR4.png')
sakuya_l1 = pygame.image.load('SR1R.png')
sakuya_l2 = pygame.image.load('SR2R.png')
sakuya_l3 = pygame.image.load('SR3R.png')
sakuya_l4 = pygame.image.load('SR4R.png')
sakuya_j1 = pygame.image.load('SJ1.png')
sakuya_j2 = pygame.image.load('SJ2.png')
sakuya_j3 = pygame.image.load('SJ3.png')
sakuya_j4 = pygame.image.load('SJ4.png')

remilia1 = pygame.image.load('311.png')
remilia2 = pygame.image.load('312.png')
remilia3 = pygame.image.load('313.png')
remilia4 = pygame.image.load('314.png')
remilia_h1 = pygame.image.load('323.png')
remilia_h2 = pygame.image.load('322.png')
remilia_h3 = pygame.image.load('321.png')

fire_1 = pygame.image.load('fire1.png')
fire_2 = pygame.image.load('fire2.png')
fire_3 = pygame.image.load('fire3.png')
fire_4 = pygame.image.load('fire4.png')

explode_1 = pygame.image.load('exp1.png')
explode_2 = pygame.image.load('exp2.png')
explode_3 = pygame.image.load('exp3.png')
explode_4 = pygame.image.load('exp4.png')
explode_5 = pygame.image.load('exp5.png')

clock = pygame.time.Clock()

bg_music = pygame.mixer.music.load('audio.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.1)

miku_width = 200
miku_height = 200
miku_x = display_width/2 + miku_width/2
miku_y = 100
miku_speed = 5
boss_hp = 10
remilia_hit = False
remilia_count = 0
hit_duration = 0
prepare = 0
suprise_count = 0

make_jump = False
jump_counter = 20

bullet_x = 100
bullet_y = 100
bullet_widht = 10
bullet_height = 9
bullet_speed_y = 5
bullet_speed_x = 5*(2*random.random() - 1)

damage_done = False
count = 0
#bullets = []
damage_index = 0

user_width = 40
user_height = 60
user_x = 100
user_y = display_height - user_height - 50
speed = 8
hp = 10
sakuya_count = 0
time_freeze = False
reload = True
time_count = 0

time_list = []
health_bar = []
#swords = []

left_status = False
right_status = False

class remilia:
    
    def __init__(self, x, y, width, height, hp, speed, remilia_hit, hit_duration, remilia_count, prepare, suprise_count, rate):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.speed = speed
        self.count = remilia_count
        self.hit = remilia_hit
        self.duration = hit_duration
        self.prepare = prepare
        self.suprise = suprise_count
        self.rate = rate
        self.bullets = []
        self.swords = []
        
    def draw_remilia(self):
        if self.hit:
            self.duration = 0
            self.hit = False
        
        if (self.duration < 10) and (self.count < 300):
            if self.count <= 5:
                display.blit(remilia_h1, (self.x, self.y))
            if (self.count > 5) and (self.count <= 10):
                display.blit(remilia_h2, (self.x, self.y))
            if (self.count > 10) and (self.count <= 15):
                display.blit(remilia_h3, (self.x, self.y))
            if (self.count > 15) and (self.count <= 20):
                display.blit(remilia_h2, (self.x, self.y))
            if self.count > 20:
                display.blit(remilia_h1, (self.x, self.y))
                self.count = 0
                self.duration += 1
            self.count += 1
        else:
            if self.count <= 5:
                display.blit(remilia1, (self.x, self.y))
            if (self.count > 5) and (self.count <= 10):
                display.blit(remilia2, (self.x, self.y))
            if (self.count > 10) and (self.count <= 15):
                display.blit(remilia3, (self.x, self.y))
            if (self.count > 15) and (self.count <= 20):
                display.blit(remilia4, (self.x, self.y))
            if (self.count > 20) and (self.count <= 25):
                display.blit(remilia3, (self.x, self.y))
            if (self.count > 25) and (self.count <= 30):
                display.blit(remilia2, (self.x, self.y))
            if (self.count > 30):
                display.blit(remilia1, (self.x, self.y))
                self.count = 0
            self.count += 1
    
    def flow(self, display_width):
        self.x += self.speed
        if self.x < 20:
            self.speed = (-1)*self.speed
        if self.x > (display_width - 200):
            self.speed = (-1)*self.speed
            
    
    def suprise_att(self,display_width, display_height):
        global suprise_x, suprise_y, suprise_radius
        if (self.prepare == 0):
            suprise_x = (display_width - 200)*random.random() + 100
            suprise_y = display_height - user_height 
            suprise_radius = 40
        if self.prepare < 5:
            if self.suprise <= 5:
                display.blit(fire_1, (suprise_x - suprise_radius, suprise_y))
            if (self.suprise > 5) and (self.suprise <= 10):
                display.blit(fire_2, (suprise_x - suprise_radius, suprise_y))
            if (self.suprise > 10) and (self.suprise <= 15):
                display.blit(fire_3, (suprise_x - suprise_radius, suprise_y))
            if (self.suprise > 15) and (self.suprise <= 20):
                display.blit(fire_4, (suprise_x - suprise_radius, suprise_y))
            if self.suprise > 20:
                self.suprise = 1
                self.prepare += 1
        
        if (self.prepare >= 5) and (self.prepare <=10):
            if self.suprise <= 5:
                display.blit(explode_1, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 5) and (self.suprise <= 10):
                display.blit(explode_2, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 10) and (self.suprise <= 15):
                display.blit(explode_3, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 15) and (self.suprise <= 20):
                display.blit(explode_4, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 20) and (self.suprise <= 25):
                display.blit(explode_3, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 25) and (self.suprise <= 30):
                display.blit(explode_2, (suprise_x - suprise_radius, display_height -  400))
            if (self.suprise > 30):
                display.blit(explode_1, (suprise_x - suprise_radius, display_height -  400))
                self.suprise = 1
                self.prepare += 1
            if ((suprise_x + suprise_radius - user.x ) > 0) and ((suprise_x - suprise_radius - user.x) < 0 ):
                user.hp -= 1
        
        if (self.prepare >= 10) and (self.suprise >= 20):
            self.suprise = 1
            self.prepare = 0
        if user.freeze and user.reload:
            self.suprise += 0.2
        else:
            self.suprise += 1
    
    def health(self):
        global health_bar
        
        if self.hit:
            self.hp -= 1
            self.count = 0
             
        health_bar.append(myfont.render( f'Remilia {miku.hp} / 10 ', False, (255, 27, 192)))
        display.blit(health_bar[0], (display_width - 200, 20))
        health_bar.pop(0)
        
    def frequency(self):
        if user.freeze and user.reload:
            self.rate = 2 * self.hp * 5
        else:
            self.rate = 2*self.hp
    
    def drawBullets(self):
        for bullet in self.bullets:
            bullet.draw(display)
        for sword in self.swords:
            sword.draw(display)
    
    def gift_and_damage(self,count,user):
        
        if (count%(self.rate + 1)) == 0:
            self.bullets.append(potroni(int(self.x + self.width//2), int(self.y + self.height//2) , 25 - self.hp, (0,0,255), round(20*random.random() - 10)))
        
        if (count%300 == 0) and (len(self.swords) == 0 ):
            sword_y = round( display_height - user.height*2.5*random.random() - 50)
            sword_x = round((display_width - 100)*random.random() + 100)
            self.swords.append(attacking(sword_x, sword_y, 20, (255, 0, 0)))

class sakuya:
    
    def __init__(self, x, y, width, height, hp, speed, sakuya_count, time_freeze, reload, time_count, left_status, right_status, jump, damage_done):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.speed = speed
        self.count = sakuya_count
        self.freeze = time_freeze
        self.reload = reload
        self.time = time_count
        self.left = left_status
        self.right = right_status
        self.jump = jump
        self.damage = damage_done
    
    def draw_sakuya(self):
        if self.left:
            if self.count <= 5:
                display.blit(sakuya_l1, (self.x, self.y))
            if (self.count > 5) and (self.count <= 10):
                display.blit(sakuya_l2, (self.x, self.y))
            if (self.count > 10) and (self.count <= 15):
                display.blit(sakuya_l3, (self.x, self.y))
            if (self.count > 15) and (self.count <= 20):
                display.blit(sakuya_l4, (self.x, self.y))
            if (self.count > 20) and (self.count <= 25):
                display.blit(sakuya_l3, (self.x, self.y))
            if (self.count > 25) and (self.count <= 30):
                display.blit(sakuya_l2, (self.x, self.y))
            if (self.count > 30):
                display.blit(sakuya_l1, (self.x, self.y))
                self.count = 0
            self.count += 1
    
        elif self.right:
            if self.count <= 5:
                display.blit(sakuya_r1, (self.x, self.y))
            if (self.count > 5) and (self.count <= 10):
                display.blit(sakuya_r2, (self.x, self.y))
            if (self.count > 10) and (self.count <= 15):
                display.blit(sakuya_r3, (self.x, self.y))
            if (self.count > 15) and (self.count <= 20):
                display.blit(sakuya_r4, (self.x, self.y))
            if (self.count > 20) and (self.count <= 25):
                display.blit(sakuya_r3, (self.x, self.y))
            if (self.count > 25) and (self.count <= 30):
                display.blit(sakuya_r2, (self.x, self.y))
            if (self.count > 30):
                display.blit(sakuya_r1, (self.x, self.y))
                self.count = 0
            self.count += 1
    
        elif self.jump:
            if self.count <= 5:
                display.blit(sakuya_j1, (self.x, self.y))
            if (self.count > 6) and (self.count <= 12):
                display.blit(sakuya_j1, (self.x, self.y))
            if (self.count > 12) and (self.count <= 18):
                display.blit(sakuya_r3, (self.x, self.y))
            if (self.count > 18) and (self.count <= 24):
                display.blit(sakuya_j4, (self.x, self.y))
            if (self.count > 24) and (self.count <= 30):
                display.blit(sakuya_j3, (self.x, self.y))
            if (self.count > 30) and (self.count <= 36):
                display.blit(sakuya_j2, (self.x, self.y))
            if (self.count > 36):
                display.blit(sakuya_j1, (self.x, self.y))
                self.count = 0
            self.count += 1    
       
        else: 
            display.blit(sakuya_st, (self.x, self.y))
    
    def right_move(self, display_width):
        if self.x < display_width - 50:
            user.x += self.speed

    def left_move(self, display_width):
        if self.x > 50:
            self.x -= self.speed

    def jump_move(self):
        global jump_counter
        if jump_counter >= -20:
            self.y -= jump_counter
            jump_counter -= 1
        else:
            jump_counter = 20
            self.jump = False
    
    def health(self):
        global health_bar
        if self.damage:
            self.hp -= 1
            OF = pygame.mixer.Sound('classic_hurt.wav')
            OF.play()
            self.damage = False
        
        health_bar.append(myfont.render( f'You {self.hp} / 10 ', False, (206, 182, 27)))
        display.blit(health_bar[0], (20, 20))
        health_bar.pop(0)
        
    def EverythingWillFreeze(self, miku):

        for bullet in miku.bullets:
            if abs(bullet.velx) > 2:
                bullet.velx = bullet.velx // 5
            bullet.vely = 2     
        if self.time == 0:
            miku.speed = miku.speed // 5
    
    def Unfreeze(self,miku):
        
        for bullet in miku.bullets:
            bullet.velx = bullet.velx * 10
            bullet.vely = 10       
        miku.speed = miku.speed * 5
        self.reload = False
        self.time = 0
    
    def attacked_and_attack(self,miku):
        for sword in miku.swords:
            if ((sword.x + sword.radius//2 - self.x) > 0) and ((sword.x - sword.radius//2 - self.x) < self.width) and ((sword.y + sword.radius//2 - self.y) > 0) and ((sword.y - sword.radius//2  - self.y) < self.height):
                miku.hit = True
                miku.swords.pop(miku.swords.index(sword))
        
        for bullet in miku.bullets:
            if ((bullet.x - self.x) > 0) and ((bullet.x - self.x) < self.width) and ((bullet.y - self.y) > 0) and ((bullet.y - self.y) < self.height):
                self.damage = True
                miku.bullets.pop(miku.bullets.index(bullet))
            
class attacking():
    
    def __init__(self, x ,y , radius, color ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        

class potroni():
    
    def __init__(self, x ,y , radius, color, facing ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velx = facing
        self.vely = 10
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


user = sakuya(user_x, user_y, user_width, user_height, hp, speed, sakuya_count, time_freeze, reload, time_count, left_status, right_status, make_jump, damage_done)
miku = remilia(miku_x, miku_y, miku_width, miku_height, boss_hp, miku_speed, remilia_hit, hit_duration, remilia_count, prepare, suprise_count, 5*(boss_hp))
def run_game():
    global user, make_jump, count , bullet_x, bullet_y, damage_done, left_status , sword_x, sword_y, right_status, time_freeze , rate
    
    game = True
    
    while game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        
        if user.hp <= 0:
            you_lose()
            
        if miku.hp <= 0:
            you_win()
        
        if keys[pygame.K_SPACE]:
            user.freeze = True
        
        for bullet in miku.bullets:
            
            if (bullet.x < 30) or (bullet.x > (display_width-30)):
                bullet.velx = -1*bullet.velx
            if bullet.y < 1000:
                bullet.y += bullet.vely
                bullet.x += bullet.velx
            else:
                miku.bullets.pop(miku.bullets.index(bullet))
        
        user.attacked_and_attack(miku)
    
        miku.gift_and_damage(count,user)        
        
        if  keys[pygame.K_LEFT]:
            user.left = True
            user.left_move(display_width)
        else: user.left = False
        
        if keys[pygame.K_RIGHT]:
            user.right = True
            user.right_move(display_width)
        else: user.right = False
        
        if  keys[pygame.K_UP]:
            user.jump = True
            
        if user.jump:
            user.jump_move()
                
        miku.flow(display_width)
        
        display.blit(bg, (-500,-290))
        
        if miku.hp <= 9:
            miku.suprise_att(display_width, display_height)
        
        miku.frequency()
        time_control()
        user.draw_sakuya()
        count+=1
        miku.drawBullets()
        miku.health()
        user.health()
        miku.draw_remilia()
        pygame.display.update()
        clock.tick(60)

def you_win():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        display.blit(youwin.render(' How dare you?!! You lose anyway!! ', False, (206, 182, 27)), (miku.x + 20, miku.y))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(15)

def you_lose():
    pygame.mixer.music.stop()
    KONO_DIO_DA = pygame.mixer.Sound('dio.wav')
    KONO_DIO_DA.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        display.blit(youlose.render(' You lose! HAHAHAHA ', False, (206, 182, 27)), (miku.x + 20, miku.y))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(15)

   
def time_control():
    global bullets
    if user.reload and user.freeze:
        user.EverythingWillFreeze(miku)
        time_list.append(za_warudo.render( f'{300 - user.time} / 300 ', False, (206, 182, 27)))
        display.blit(time_list[0], (display_width//2 - 200, 20))
        time_list.pop(0)
            
    if (user.time > 300) and user.reload:
        user.Unfreeze(miku)
    if user.reload == False:
        time_list.append(za_warudo.render( f'{user.time} / 500  ', False, (255, 145, 35)))
        display.blit(time_list[0], (display_width//2 - 200, 20))
        time_list.pop(0)
    if user.time == 500:
        user.reload = True
        user.time = 0
        user.freeze = False
    user.time += 1
    if user.freeze == False:
        user.time = 0
        time_list.append(za_warudo.render( 'READY ', False, (44, 255, 235)))
        display.blit(time_list[0], (display_width//2 - 200, 20))
        time_list.pop(0)       
            

run_game()

def main():
    pass

if __name__ == main:
    main()