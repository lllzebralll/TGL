from numpy import array
from set import char, debug

#array([["\033[30m\033[40m#","\033[31m\033[40m#","\033[30m\033[41m#","\033[31m\033[41m#"],
#       ["\033[32m\033[40m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[30m\033[42m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[32m\033[42m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"]],
#      [["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"]],
#      [["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"]],
#      [["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"],
#       ["\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#","\033[3m\033[4m#"]])
def color(R, G, B):
    ar = array([[["\033[30m\033[40m\033[1m{}\033[0m".format(char),"\033[31m\033[40m\033[1m{}\033[0m".format(char),"\033[31m\033[41m\033[1m{}\033[0m".format(char)],
                 ["\033[32m\033[40m\033[1m{}\033[0m".format(char),"\033[30m\033[43m\033[1m{}\033[0m".format(char),"\033[31m\033[43m\033[1m{}\033[0m".format(char)],
                 ["\033[32m\033[42m\033[1m{}\033[0m".format(char),"\033[32m\033[43m\033[1m{}\033[0m".format(char),"\033[33m\033[43m\033[1m{}\033[0m".format(char)]],
                [["\033[34m\033[40m\033[1m{}\033[0m".format(char),"\033[30m\033[45m\033[1m{}\033[0m".format(char),"\033[31m\033[45m\033[1m{}\033[0m".format(char)],
                 ["\033[30m\033[46m\033[1m{}\033[0m".format(char),"\033[37m\033[40m\033[1m{}\033[0m".format(char),"\033[37m\033[41m\033[1m{}\033[0m".format(char)],
                 ["\033[32m\033[46m\033[1m{}\033[0m".format(char),"\033[37m\033[42m\033[1m{}\033[0m".format(char),"\033[33m\033[47m\033[1m{}\033[0m".format(char)]],
                [["\033[34m\033[44m\033[1m{}\033[0m".format(char),"\033[35m\033[44m\033[1m{}\033[0m".format(char),"\033[35m\033[45m\033[1m{}\033[0m".format(char)],
                 ["\033[36m\033[44m\033[1m{}\033[0m".format(char),"\033[37m\033[44m\033[1m{}\033[0m".format(char),"\033[35m\033[47m\033[1m{}\033[0m".format(char)],
                 ["\033[36m\033[46m\033[1m{}\033[0m".format(char),"\033[36m\033[47m\033[1m{}\033[0m".format(char),"\033[37m\033[47m\033[1m{}\033[0m".format(char)]]], str)

    color = ar[B, G, R]

    return color

    if debug == True:
        print(ar[B, G, R])
