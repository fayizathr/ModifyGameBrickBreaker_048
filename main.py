


# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.speed = speed
        self.color = color

        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    # Used to render the object on the screen with curved edges effect simulation
    def display(self):
        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.strikerRect, border_radius=5)

    # Used to update the state of the object
    def update(self, xFac):
        self.posx += self.speed * xFac

        # Restricting the striker to be in between the edges
        if self.posx <= 0:
            self.posx = 0
        elif self.posx + self.width >= WIDTH:
            self.posx = WIDTH - self.width

    # Returns the rect of the object
    def getRect(self):
        return self.strikerRect


# Block Class
class Block:
    def __init__(self, posx, posy, width, height, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.color = color
        self.damage = 100

        if color == WHITE:
            self.health = 200
        else:
            self.health = 100

        self.blockRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    # Used to render the object on the screen
    def display(self):
        if self.health > 0:
            # Menggambar blok dengan efek garis tepi (border) agar ala neon arcade
            pygame.draw.rect(screen, self.color, self.blockRect, border_radius=3)
            pygame.draw.rect(screen, BLACK, self.blockRect, 2, border_radius=3)

    def hit(self):
        self.health -= self.damage

    def getRect(self):
        return self.blockRect

    def getHealth(self):
        return self.health


# Ball Class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, -1
        self.trail = []  # Menyimpan jejak bola

    def display(self):
        # Menggambar efek jejak (trail) di belakang bola
        for t in self.trail:
            pygame.draw.circle(screen, (50, 50, 80), (int(t[0]), int(t[1])), self.radius - 2)
        
        pygame.draw.circle(
            screen, self.color, (int(self.posx), int(self.posy)), self.radius)

    def update(self):
        # Simpan posisi untuk efek trail
        self.trail.append((self.posx, self.posy))
        if len(self.trail) > 5:
            self.trail.pop(0)

        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed

        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1

        if self.posy <= 0:
            self.yFac *= -1

        if self.posy >= HEIGHT:
            return True

        return False

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac, self.yFac = random.choice([-1, 1]), -1
        self.trail.clear()

    def hit(self):
        self.yFac *= -1

    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, 
                           self.radius * 2, self.radius * 2)


# Helper Functions
def collisionChecker(rect, ballRect):
    if pygame.Rect.colliderect(rect, ballRect):
        return True
    return False


def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
    listOfBlocks = []
    colorList = [NEON_BLUE, NEON_PURPLE, NEON_GREEN, NEON_YELLOW, NEON_RED]

    # Mengatur posisi blok agak ke bawah dari atas layar
    start_y = 50
    for i in range(15, WIDTH - blockWidth, blockWidth + horizontalGap):
        for j in range(start_y, start_y + (blockHeight + verticalGap) * 4, blockHeight + verticalGap):
            chosen_color = random.choice(colorList)
            listOfBlocks.append(
                Block(i, j, blockWidth, blockHeight, chosen_color))

    return listOfBlocks


def gameOverScreen(score):
    screen.fill(BLACK)
    
    overText = font_large.render("GAME OVER", True, NEON_RED)
    overRect = overText.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    
    scoreText = font.render(f"Skor Akhir: {score}", True, WHITE)
    scoreRect = scoreText.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

    restartText = font.render("Tekan [SPASI] untuk Main Lagi atau [ESC] untuk Keluar", True, NEON_BLUE)
    restartRect = restartText.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    screen.blit(overText, overRect)
    screen.blit(scoreText, scoreRect)
    screen.blit(restartText, restartRect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False


