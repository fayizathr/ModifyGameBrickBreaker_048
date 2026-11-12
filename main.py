

# Game Manager
def main():
    running = True
    lives = 3
    score = 0

    striker = Striker(WIDTH // 2 - 50, HEIGHT - 40, 100, 15, 8, NEON_BLUE)
    strikerXFac = 0

    ball = Ball(WIDTH // 2, HEIGHT // 2, 8, 5, WHITE)

    blockWidth, blockHeight = 50, 18
    horizontalGap, verticalGap = 12, 12

    listOfBlocks = populateBlocks(
        blockWidth, blockHeight, horizontalGap, verticalGap)

    # Game loop
    while running:
        screen.fill(BLACK)

        # Render UI Skor & Nyawa di atas
        scoreSurf = font.render(f"SCORE: {score}", True, WHITE)
        livesSurf = font.render(f"LIVES: {lives}", True, NEON_RED)
        screen.blit(scoreSurf, (20, 15))
        screen.blit(livesSurf, (WIDTH - 100, 15))

        # Garis pembatas bawah UI atas
        pygame.draw.line(screen, GRAY, (0, 40), (WIDTH, 40), 1)

        # If all the blocks are destroyed, repopulate them
        if not listOfBlocks:
            listOfBlocks = populateBlocks(
                blockWidth, blockHeight, horizontalGap, verticalGap)
            ball.speed += 0.5  # Tambah tingkat kesulitan (kecepatan bola bertambah)

        # All the lives are over
        if lives <= 0:
            shouldRestart = gameOverScreen(score)
            if shouldRestart:
                lives = 3
                score = 0
                ball.speed = 5
                listOfBlocks = populateBlocks(
                    blockWidth, blockHeight, horizontalGap, verticalGap)
                ball.reset()
            else:
                running = False
                break

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT:
                    strikerXFac = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    strikerXFac = 0

        # Collision check with Striker
        if collisionChecker(striker.getRect(), ball.getRect()):
            ball.hit()
            # Efek pantulan dinamis berdasarkan titik benturan dengan striker
            offset = ball.posx - (striker.posx + striker.width / 2)
            ball.xFac = offset / (striker.width / 2)

        # Collision check with Blocks
        for block in listOfBlocks:
            if collisionChecker(block.getRect(), ball.getRect()):
                ball.hit()
                block.hit()

                if block.getHealth() <= 0:
                    listOfBlocks.remove(block)
                    score += 10

        # Update
        striker.update(strikerXFac)
        lifeLost = ball.update()

        if lifeLost:
            lives -= 1
            ball.reset()

        # Display Entities
        striker.display()
        ball.display()

        for block in listOfBlocks:
            block.display()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()