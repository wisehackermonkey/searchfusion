from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in

rg = Ripgrepy('print', '/home/o/github/searchfusion')
b = rg.with_filename().line_number().json().run().as_dict
b