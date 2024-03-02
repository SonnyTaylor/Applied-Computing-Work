# are python functions hoisted to the top of the call stack?


def testjoe():
    print("running joe test")
    joetest()


def joetest():
    print("joe")


testjoe()

# yes they are
