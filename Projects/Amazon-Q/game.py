import pygame
import sys
import random
import math
from collections import deque

# Initialize pygame
pygame.init()

# Game dimensions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
PLAY_AREA = 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 40)  # Background color

FLAG_COLORS = [
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 0, 255),   # Magenta
    (0, 255, 255),   # Cyan
    (255, 165, 0)    # Orange
]

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Caterpillar Flag Game")

# Background stars
stars = []
for _ in range(100):
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    size = random.randint(1, 3)
    brightness = random.randint(100, 255)
    speed = random.uniform(0.1, 0.5)
    stars.append({
        'x': x,
        'y': y,
        'size': size,
        'brightness': brightness,
        'speed': speed,
        'twinkle_speed': random.uniform(0.01, 0.05),
        'twinkle_factor': 0
    })

# Load sounds
try:
    pygame.mixer.init()
    collect_sound = pygame.mixer.Sound("collect.wav")
    game_over_sound = pygame.mixer.Sound("gameover.wav")
except:
    collect_sound = None
    game_over_sound = None

# Caterpillar properties
segment_radius = 20
caterpillar_speed = 5
segment_spacing = segment_radius * 1.5

# Flag properties
flag_width = 30
flag_height = 40
pole_width = 5
pole_height = 60
num_flags = 6

# Obstacle properties
num_obstacles = 3
obstacles = []

# Particle system
particles = []

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

# Draw background function
def draw_background():
    screen.fill(DARK_BLUE)
    
    # Update and draw stars
    for star in stars:
        # Update twinkle effect
        star['twinkle_factor'] += star['twinkle_speed']
        brightness_offset = int(math.sin(star['twinkle_factor']) * 50)
        brightness = max(100, min(255, star['brightness'] + brightness_offset))
        
        # Draw star
        pygame.draw.circle(screen, (brightness, brightness, brightness), 
                          (int(star['x']), int(star['y'])), star['size'])
        
        # Move star
        star['y'] += star['speed']
        if star['y'] > WINDOW_HEIGHT:
            star['y'] = 0
            star['x'] = random.randint(0, WINDOW_WIDTH)

# Draw a flag function
def draw_flag(x, y, color):
    # Draw pole
    pygame.draw.rect(screen, BROWN, (x, y, pole_width, pole_height))
    # Draw triangular flag
    pygame.draw.polygon(screen, color, [(x + pole_width, y), (x + pole_width + flag_width, y + flag_height//2), (x + pole_width, y + flag_height)])

# Create particle effect
def create_particles(x, y, color, count=20):
    for _ in range(count):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 5)
        size = random.randint(2, 6)
        lifetime = random.randint(20, 40)
        particles.append({
            'x': x,
            'y': y,
            'dx': math.cos(angle) * speed,
            'dy': math.sin(angle) * speed,
            'size': size,
            'color': color,
            'lifetime': lifetime
        })

# Update particles
def update_particles():
    global particles
    for particle in particles[:]:
        particle['x'] += particle['dx']
        particle['y'] += particle['dy']
        particle['lifetime'] -= 1
        if particle['lifetime'] <= 0:
            particles.remove(particle)

# Draw particles
def draw_particles():
    for particle in particles:
        pygame.draw.circle(screen, particle['color'], (int(particle['x']), int(particle['y'])), particle['size'])

# Initialize game function
def init_game():
    # Caterpillar initial position
    head_x = WINDOW_WIDTH // 2
    head_y = WINDOW_HEIGHT // 2
    
    # Initialize caterpillar segments (head is the first element)
    segments = deque([(head_x, head_y)])
    
    # Generate random flag positions
    flags = []
    for i in range(num_flags):
        x = random.randint(pole_width + 20, WINDOW_WIDTH - flag_width - 20)
        y = random.randint(pole_height + 20, WINDOW_HEIGHT - pole_height - 20)
        flags.append({
            'x': x,
            'y': y,
            'color': FLAG_COLORS[i],
            'captured': False
        })
    
    # Generate obstacles
    obstacles.clear()
    for _ in range(num_obstacles):
        size = random.randint(30, 80)
        x = random.randint(size, WINDOW_WIDTH - size)
        y = random.randint(size, WINDOW_HEIGHT - size)
        obstacles.append({
            'x': x,
            'y': y,
            'size': size
        })
    
    # Clear particles
    particles.clear()
    
    return segments, flags, 0, PLAYING  # segments, flags, score, game_state

# Draw button
def draw_button(text, x, y, width, height, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    return False

# Game state
font = pygame.font.SysFont(None, 36)
segments, flags, score, game_state = init_game()
high_score = 0
trail = []

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_state != MENU:
                segments, flags, score, game_state = init_game()
            elif event.key == pygame.K_ESCAPE:
                if game_state == PLAYING:
                    game_state = MENU
                elif game_state == MENU:
                    game_state = PLAYING
    
    # Draw dynamic background
    draw_background()
    
    # Menu state
    if game_state == MENU:
        title = font.render("CATERPILLAR FLAG GAME", True, WHITE)
        screen.blit(title, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//4))
        
        if draw_button("START GAME", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2, 200, 50, GREEN, (100, 255, 100)):
            segments, flags, score, game_state = init_game()
        
        if draw_button("QUIT", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 70, 200, 50, RED, (255, 100, 100)):
            running = False
        
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_text, (WINDOW_WIDTH//2 - 80, WINDOW_HEIGHT//2 + 150))
    
    # Playing state
    elif game_state == PLAYING:
        # Get head position
        head_x, head_y = segments[0]
        
        # Handle key presses for movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -caterpillar_speed
        if keys[pygame.K_RIGHT]:
            dx = caterpillar_speed
        if keys[pygame.K_UP]:
            dy = -caterpillar_speed
        if keys[pygame.K_DOWN]:
            dy = caterpillar_speed
        
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071  # 1/sqrt(2)
            dy *= 0.7071
        
        head_x += dx
        head_y += dy
        
        # Keep the head within the play area
        head_x = max(segment_radius, min(head_x, WINDOW_WIDTH - segment_radius))
        head_y = max(segment_radius, min(head_y, WINDOW_HEIGHT - segment_radius))
        
        # Check collision with obstacles
        for obstacle in obstacles:
            distance = math.sqrt((head_x - obstacle['x'])**2 + (head_y - obstacle['y'])**2)
            if distance < segment_radius + obstacle['size']:
                # Push the head away from the obstacle
                angle = math.atan2(head_y - obstacle['y'], head_x - obstacle['x'])
                push_distance = segment_radius + obstacle['size'] - distance
                head_x += math.cos(angle) * push_distance
                head_y += math.sin(angle) * push_distance
        
        # Add to trail
        if len(trail) == 0 or math.sqrt((trail[-1][0] - head_x)**2 + (trail[-1][1] - head_y)**2) > 5:
            trail.append((head_x, head_y))
            if len(trail) > 100:  # Limit trail length
                trail.pop(0)
        
        # Update head position
        segments.appendleft((head_x, head_y))
        
        # Remove tail if no new segment needed
        if len(segments) > score // 50 + 1:
            segments.pop()
        
        # Check for flag captures
        for flag in flags:
            if not flag['captured']:
                # Simple collision detection (if head is near flag pole)
                if abs(head_x - flag['x']) < segment_radius + pole_width and \
                   abs(head_y - flag['y'] + pole_height//2) < segment_radius + pole_height//2:
                    flag['captured'] = True
                    score += 50
                    create_particles(flag['x'], flag['y'], flag['color'])
                    if collect_sound:
                        collect_sound.play()
        
        # Check if all flags are captured
        if all(flag['captured'] for flag in flags):
            game_state = GAME_OVER
            if score > high_score:
                high_score = score
            if game_over_sound:
                game_over_sound.play()
        
        # Draw the trail
        if len(trail) > 1:
            pygame.draw.lines(screen, (50, 50, 50), False, trail, 3)
        
        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.circle(screen, BLUE, (obstacle['x'], obstacle['y']), obstacle['size'])
        
        # Draw the flags
        for flag in flags:
            if not flag['captured']:
                draw_flag(flag['x'], flag['y'], flag['color'])
        
        # Update and draw particles
        update_particles()
        draw_particles()
        
        # Draw the caterpillar
        for i, (x, y) in enumerate(segments):
            color = RED if i == 0 else GREEN
            pygame.draw.circle(screen, color, (int(x), int(y)), segment_radius)
            # Draw eyes on head
            if i == 0:
                eye_offset = 8
                pygame.draw.circle(screen, WHITE, (int(x - eye_offset), int(y - eye_offset)), 5)
                pygame.draw.circle(screen, WHITE, (int(x + eye_offset), int(y - eye_offset)), 5)
                pygame.draw.circle(screen, BLACK, (int(x - eye_offset), int(y - eye_offset)), 2)
                pygame.draw.circle(screen, BLACK, (int(x + eye_offset), int(y - eye_offset)), 2)
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Draw instructions
        instructions = font.render("ESC: Menu | R: Restart", True, WHITE)
        screen.blit(instructions, (WINDOW_WIDTH - 250, 10))
    
    # Game over state
    elif game_state == GAME_OVER:
        # Draw the caterpillar
        for i, (x, y) in enumerate(segments):
            color = RED if i == 0 else GREEN
            pygame.draw.circle(screen, color, (int(x), int(y)), segment_radius)
        
        # Update and draw particles
        update_particles()
        draw_particles()
        
        # Draw game over message
        game_over_text = font.render("Game Over! All flags captured!", True, WHITE)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press 'R' to restart or ESC for menu", True, WHITE)
        
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - 180, WINDOW_HEIGHT//2 - 40))
        screen.blit(score_text, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2))
        screen.blit(restart_text, (WINDOW_WIDTH//2 - 180, WINDOW_HEIGHT//2 + 40))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()