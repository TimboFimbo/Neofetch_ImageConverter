#!/usr/bin/python3

from html.parser import HTMLParser   

class Colors():
    cur_color = ""
    color_list = []

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.colors = Colors

    # TODO Check if user wishes to merge colors down to 6 (neofetch default maximum)
    def add_color(self, parsed_color):
        self.colors.color_list.append(parsed_color)
        self.colors.cur_color = parsed_color
        print("${c" + str((len(self.colors.color_list))) + "}", end='')

    # TODO Try to extract colors from image (convert 24-bit/RGB to 8-bit/256-color)
    def check_color(self, parsed_color):
        if parsed_color == self.colors.cur_color:
            return
        elif len(self.colors.color_list) == 0:
            self.add_color(parsed_color)
            return       
        elif parsed_color not in self.colors.color_list:
            self.add_color(parsed_color)
            # print("'" + str(self.colors.color_list) + "'", end='') # Just for Testing
            return
        else:
            print("${c" + str(self.colors.color_list.index(parsed_color) + 1) + "}", end='')
            self.colors.cur_color = parsed_color

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