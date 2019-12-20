import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)

    def update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):

        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
