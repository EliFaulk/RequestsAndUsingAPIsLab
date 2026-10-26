import sys
import os
import pygame


def main():
    response = requests.get("https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key=DEMO_KEY")

    # Load images.jpeg from the same directory as this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "image.jpeg")

    pygame.init()

    # Read the screen size BEFORE creating any window; afterwards Info()
    # reports the window's size instead of the monitor's
    info = pygame.display.Info()
    win_w, win_h = info.current_w // 2, info.current_h // 2

    try:
        # Create a temporary display so convert_alpha() works
        pygame.display.set_mode((1, 1))
        image = pygame.image.load(image_path).convert_alpha()
    except (pygame.error, FileNotFoundError) as e:
        print(f"Could not load {image_path}: {e}")
        pygame.quit()
        sys.exit(1)

    # Window is half the screen size; scale the image to fit it, keeping aspect ratio
    img_w, img_h = image.get_size()
    scale = min(win_w / img_w, win_h / img_h)
    image = pygame.transform.smoothscale(
        image, (int(img_w * scale), int(img_h * scale))
    )
    img_w, img_h = image.get_size()
    pos = ((win_w - img_w) // 2, (win_h - img_h) // 2)

    screen = pygame.display.set_mode((win_w, win_h))
    pygame.display.set_caption("images.jpeg")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((30, 30, 30))
        screen.blit(image, pos)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
