#!/usr/bin/python3

from html.parser import HTMLParser   
import hex_to_256

class Colors():
    cur_color = ""
    color_list = []

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.colors = Colors
        # self.color_chart = {
        #     "000000" : 16,
        #     "808080" : 8,
        #     "800000" : 88,
        #     "ff0000" : 9,
        #     "008000" : 28,
        #     "00ff00" : 10,
        #     "808000" : 208,
        #     "ffff00" : 11,
        #     "000080" : 21,
        #     "0000ff" : 12,
        #     "800080" : 127,
        #     "ff00ff" : 13,
        #     "008080" : 33,
        #     "00ffff" : 14,
        #     "c0c0c0" : 246,
        #     "ffffff" : 15
        # }

    def print_final_colors(self):
        # print("'" + str(self.colors.color_list) + "'", end='') # Just for Testing
        print("\nascii_colors=(", end='')
        first = True

        for color in self.colors.color_list:
            if first:
                first = False
                # print(str(self.color_chart[color]), end='')
                print(str(color), end='')
            else:
                # print(" " + str(self.color_chart[color]), end='')
                print(" " + color, end='')

        print(")")


    # TODO Check if user wishes to merge colors down to 6 (neofetch default maximum)
    def add_color(self, hex_color):
        self.colors.color_list.append(hex_color)
        self.colors.cur_color = hex_color
        print("${c" + str((len(self.colors.color_list))) + "}", end='')

    def check_color(self, hex_color):
        color256, rgb = hex_to_256.rgb2short(hex_color)
        if color256 == self.colors.cur_color:
            return
        elif len(self.colors.color_list) == 0:
            self.add_color(color256)
            return       
        elif color256 not in self.colors.color_list:
            self.add_color(color256)
            return
        else:
            print("${c" + str(self.colors.color_list.index(color256) + 1) + "}", end='')
            self.colors.cur_color = color256

    def handle_starttag(self, tag, attrs):
        startTagText = self.get_starttag_text()
        if "#" in startTagText:
            textSplit = startTagText.split("#")
            if textSplit[1][0] != ";":
                color = textSplit[1][0:6]
                self.check_color(color)

    def handle_data(self, data):
        print(data, end='')

# TODO Needs to prompt for output files
input_file = input("Enter path to HTML input_file: ")
f = open(input_file, "r")
lines = f.readlines()

parser = MyHTMLParser()

for line in lines:
    parser.feed(line)

parser.print_final_colors()