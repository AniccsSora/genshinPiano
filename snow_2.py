from pkey import Harp

def play():
    harp = Harp(bpm=92, basic_type=8, show_hit=False)
    # Press and release space
    # -- 1
    harp.hit2("3^", "1")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("4^")
    harp.hit("5")
    # -- 2
    harp.hit2("3^", "7,")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("2^")
    # -- 3
    harp.hit2("3^", "6,")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("4^")
    harp.hit("5")
    # -- 4
    harp.hit2("5^", "5,")
    harp.hit("5")

    harp.hit("4^")
    harp.hit("5")

    harp.hit("3^")
    harp.hit("5")

    harp.hit("2^")
    harp.hit("5")
    # -- 5
    harp.hit2("1^", "4,")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("5")

    harp.hit("2^")
    harp.hit("5")
    # -- 6
    harp.hit2("1^", "3,")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("5")

    harp.hit("5^")
    harp.hit("5")
    # -- 7
    harp.hit2("1^", "2,")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("2^")

    harp.hit("3^")
    harp.hit("2^", 32)  # 三連音 - 2
    harp.hit("3^", 32)  # 三連音 - 3
    harp.hit("2^", 16)

    harp.hit("1^")
    harp.hit("5")
    # -- 8
    harp.hit2("1^", "5,")
    harp.hit("5")

    harp.hit("1^")
    harp.hit("2^")

    harp.hit("3^")
    harp.hit("2^", 32)  # 三連音
    harp.hit("3^", 32)  # 三連音
    harp.hit("2^", 16)

    harp.hit("1^")
    harp.hit("2^")
    # -- 9
    harp.hit2("3^", "1,")
    harp.hit2("5", "5,")

    harp.hit2("3^", "3")
    harp.hit("5")

    harp.hit2("3^", "1,")
    harp.hit2("5", "5,")

    harp.hit2("4^", "2")
    harp.hit("5")
    # -- 10
    harp.hit2("3^", "7,")
    harp.hit2("5", "5,")

    harp.hit2("3^", "2")
    harp.hit("5")

    harp.hit2("3^", "7,")
    harp.hit2("5", "5,")

    harp.hit2("1^", "1")
    harp.hit("2^")
    # -- 11
    harp.hit2("3^", "6,")
    harp.hit2("5", "3,")

    harp.hit2("3^", "1")
    harp.hit("5")

    harp.hit2("3^", "6,")
    harp.hit2("5", "3,")

    harp.hit2("3^", "1")
    harp.hit("4^")
    # -- 12
    harp.hit2("5^", "5,")
    harp.hit2("5", "3,")

    harp.hit2("1^", "1")
    harp.hit("5")

    harp.hit2("5^", "5,")
    harp.hit("4^", 32)  # 三連音 - 2
    harp.hit("5^", 32)  # 三連音 - 3
    harp.hit("4^", 16)

    harp.hit2("3^", "1")
    harp.hit("2^")
    # -- 13
    harp.hit2("1^", "4,")
    harp.hit2("5", "1,")

    harp.hit2("1^", "6,")
    harp.hit("5")

    harp.hit2("1^", "4,")
    harp.hit2("5", "1,")

    harp.hit2("5^", "6,")
    harp.hit("5")
    # -- 14
    harp.hit2("1^", "3,")
    harp.hit2("1^", "1,")

    harp.hit2("5^", "5,")
    harp.hit("4^")

    harp.hit2("3^", "3,")
    harp.hit("2^", 32)  # 三連音 - 2
    harp.hit("3^", 32)  # 三連音 - 3
    harp.hit("2^", 16)

    harp.hit2("1^", "5,")
    harp.hit("5")
    # -- 15
    harp.hit2("1^", "2,")
    harp.hit2("5", "6,")

    harp.hit2("1^", "4,")
    harp.hit("2^")

    harp.hit2("3^", "2,")
    harp.hit("2^", 32)  # 三連音
    harp.hit("3^", 32)  # 三連音
    harp.hit("2^", 16)

    harp.hit2("1^", "4,")
    harp.hit("5")
    # -- 16
    harp.hit2("1^", "5,")
    harp.hit2("5", "4,")

    harp.hit2("1^", "5,")
    harp.hit2("5^", "4,")

    harp.hit2("4^", "5,")
    harp.hit("3^", 32)  # 三連音
    harp.hit("4^", 32)  # 三連音
    harp.hit("3^", 16)

    harp.hit2("2^", "7,", 4)
    # -- 17
    harp.hit2("3^", "1,")
    harp.hit2("5", "5,")

    harp.hit2("3^", "3,")
    harp.hit2("5", "5,")

    harp.hit2("3^", "1,")
    harp.hit2("5", "5,")

    harp.hit2("4^", "2,")
    harp.hit2("5", "5,")
    # -- 18
    harp.hit2("3^", "7,")
    harp.hit2("6", "6,")

    harp.hit2("3^", "2,")
    harp.hit2("6", "6,")

    harp.hit2("3^", "3,")
    harp.hit2("5", "7,")

    harp.hit2("1^", "5,")
    harp.hit2("2^", "7,")
    # -- 19
    harp.hit2("3^", "6,")
    harp.hit2("6", "3,")

    harp.hit2("3^", "1,")
    harp.hit2("6", "3,")

    harp.hit2("3^", "6,")
    harp.hit2("6", "3,")

    harp.hit2("4^", "1,")
    harp.hit2("6", "3,")
    # -- 20
    harp.hit2("5^", "5,")
    harp.hit2("1^", "3,")

    harp.hit2("1^", "7,")
    harp.hit("3,")

    harp.hit2("5^", "5,")
    harp.hit2("4", "3,", 32)
    harp.hit2("5", "3,", 32)
    harp.hit("4", 16)

    harp.hit2("3^", "1")
    harp.hit("2^")
    # -- 21
    harp.hit2("1^", "4,")
    harp.hit2("5^", "1,")

    harp.hit2("1^", "4,")
    harp.hit2("5", "1,")

    harp.hit2("1^", "5,")
    harp.hit2("5", "1,")

    harp.hit2("5^", "6,", 4)
    # -- 22
    harp.hit2("1^", "3,")
    harp.hit("1,")

    harp.hit2("5^", "5,")
    harp.hit2("4^", "1,")

    harp.hit2("3^", "3,")
    harp.hit("2^", 32)
    harp.hit("3^", 32)
    harp.hit("2^", 16)

    harp.hit2("1^", "5,")
    harp.hit2("5^", "1,")
    # -- 23
    harp.hit2("1^", "2,")
    harp.hit2("5^", "1,")

    harp.hit2("1^", "4,")
    harp.hit2("2^", "6,")

    harp.hit2("3^", "3")
    harp.hit("2^", 32)
    harp.hit("3^", 32)
    harp.hit("2^", 16)

    harp.hit("1^")
    harp.hit("5^")
    # -- 24
    harp.hit2("1^", "5,")
    harp.hit2("5^", "4,")

    harp.hit2("1^", "1")
    harp.hit("5^")

    harp.hit("4^")
    harp.hit("3^", 32)
    harp.hit("4^", 32)
    harp.hit("3^", 16)

    harp.hit("2^")
    harp.hit("1^")
    # -- 25
    harp.hit4("1^", "5,", "3^", "1,", 1)
    # -- end







