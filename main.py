"""
    Case-study #5 Tessellation
    Developers:
    Panukova E.(90%), Kuznetsova K.(20%)

"""
import local as lc
from turtle import *

def menu():

    print(lc.MENU)
    print(lc.T, lc.WHITE)
    print(lc.T, lc.DARKRED)
    print(lc.T, lc.RED)
    print(lc.T, lc.ORANGE)
    print(lc.T, lc.YELLOW)
    print(lc.T, lc.GREEN)
    print(lc.T, lc.SKY_BLUE1)
    print(lc.T, lc.SKY_BLUE)
    print(lc.T, lc.BLUE)
    print(lc.T, lc.DARKBLUE)
    print(lc.T, lc.ROSY)
    print(lc.T, lc.PURPLE)
    print(lc.T, lc.BLACK)

menu()


def get_color_choice():                                         # A function to select the colors of the canvas.
    fir_color = str(input(lc.MEN_2)).lower()

    while True:
        if fir_color == lc.RED or fir_color == lc.ORANGE or fir_color == lc.YELLOW or fir_color == lc.GREEN \
            or fir_color == lc.SKY_BLUE1 or fir_color == lc.SKY_BLUE or fir_color == lc.BLUE \
            or fir_color == lc.PURPLE or fir_color == lc.BLACK or fir_color == lc.WHITE or fir_color == lc.DARKRED\
                or fir_color == lc.DARKBLUE or fir_color == lc.ROSY:

            color = fir_color
            if color == lc.WHITE:
                return '#FFFFFF'
            elif color == lc.RED:
                return '#FF0000'
            elif color == lc.DARKRED:
                return '#8B0000'
            elif color == lc.ORANGE:
                return '#FF8C00'
            elif color == lc.YELLOW:
                return '#FFFF00'
            elif color == lc.GREEN:
                return '#008000'
            elif color == lc.SKY_BLUE1:
                return '#00FFFF'
            elif color == lc.SKY_BLUE:
                return '#00BFFF'
            elif color == lc.BLUE:
                return '#0000CD'
            elif color == lc.DARKBLUE:
                return '#191970'
            elif color == lc.ROSY:
                return '#FF1493'
            elif color == lc.PURPLE:
                return '#800080'
            elif color == lc.BLACK:
                return '#000000'
        else:
            print(fir_color, lc.COLOR)
            fir_color = str(input(lc.ERROR)).lower()
            continue


def get_num_hexagons():                                         # Function for determining the size of the canvas.
    n = int(input(lc.COUNT))
    while True:
        try:
            if n >= 4 and n <= 20 and type(n) == int:
                return n
            else:
                print(lc.ERROR2)
                n = int(input())
        except ValueError:
            print(lc.ERROR1)
            n = input()
            continue


def draw_hexagons(n = 0):                                       # Function of the main polygon.
    left(30)
    begin_fill()
    speed(100)
    down()
    while n != 600:
        fd(lines_)
        left(60)
        n += 120
    up()
    fd(lines_)
    left(30)
    end_fill()


def func_part(color_3):                                         # Draws a single polygon of the specified color .
    color(color_3)
    draw_hexagons(size_of_pict)
    up()
    fd(lines_for * 2)
    down()


setpos = (500, 500)


def main(color_1, color_2):                                     # Main function.

    get_color_choice()                                          # Calling the function to select a color .
    size_of_pict = get_num_hexagons()
    lines_ = ((500 / 2 / size_of_pict) ** 2 / 6) * 2             # Length of the polygon's side.
    lines_for = ((lines_ ** 2 - (lines_ / 2) ** 2) ** 1 / 2)    # Offset depending on the parity line.

    on_line = 1
    to_line = 1
    x = 500
    y = -500

    bel = ''

    for n in range(size_of_pict):
        up()
        goto(x, y)
        down()

        if on_line % 2 == 0:                                    # If the polygon line is odd.
            for i in range(size_of_pict):
                if to_line % 2 != 0:
                    bel = color_1
                elif to_line % 2 == 0:
                    bel = color_2
                color_3 = bel
                func_part(color_3)
                to_line += 1
            up()
            x = x + lines_for
            y = y - (3 / 2) * lines_
            goto(x, y)
            down()
            on_line += 1

        else:

            for i in range(size_of_pict):
                if to_line % 2 != 0:
                    bel = color_2
                elif to_line % 2 == 0:
                    bel = color_1
                color_3 = bel
                func_part(color_3)
                to_line += 1
            up()
            x = x - lines_for
            y = y - (3 / 2) * lines_
            on_line += 1
            to_line += 1
            goto(x, y)
            down()


color_1 = get_color_choice()
color_2 = get_color_choice()


main(color_1, color_2)
