
def mapping(interval_abbr):
    if interval_abbr == "1^":
        return "q"
    elif interval_abbr == "2^":
        return "w"
    elif interval_abbr == "3^":
        return "e"
    elif interval_abbr == "4^":
        return "r"
    elif interval_abbr == "5^":
        return "t"
    elif interval_abbr == "6^":
        return "y"
    elif interval_abbr == "7^":
        return "u"
    # 基音
    elif interval_abbr == "1":
        return "a"
    elif interval_abbr == "2":
        return "s"
    elif interval_abbr == "3":
        return "d"
    elif interval_abbr == "4":
        return "f"
    elif interval_abbr == "5":
        return "g"
    elif interval_abbr == "6":
        return "h"
    elif interval_abbr == "7":
        return "j"
    # 高音
    elif interval_abbr == "1,":
        return "z"
    elif interval_abbr == "2,":
        return "x"
    elif interval_abbr == "3,":
        return "c"
    elif interval_abbr == "4,":
        return "v"
    elif interval_abbr == "5,":
        return "b"
    elif interval_abbr == "6,":
        return "n"
    elif interval_abbr == "7,":
        return "m"
    elif interval_abbr == "0":
        return "0"  # 休止符
    else:
        raise ValueError(f"Wrong mapping :\'{interval_abbr}\'")
