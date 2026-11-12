


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


