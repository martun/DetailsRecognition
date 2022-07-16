import HandDetails


def parse_hand_details(path_to_png_file):
    details = HandDetails(path_to_png_file)
    # Print something here to make sure it works.


if __name__ == '__main__':
    path_to_file = "C:/Users/martun/Downloads/game_283.png"
    parse_hand_details(path_to_file)
