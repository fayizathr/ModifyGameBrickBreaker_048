

# Helper Functions
def collisionChecker(rect, ballRect):
    if pygame.Rect.colliderect(rect, ballRect):
        return True
    return False





