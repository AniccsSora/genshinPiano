from pynput.keyboard import Key, Controller
from Interval_mapping import mapping
import time

class Harp:
    def __init__(self, bpm, show_hit=False, basic_type=4):
        self.bpm = bpm  # 每分鐘 4分音符的出現次數
        self.basic_type = basic_type  # 預設幾分音符
        self.keyboard = Controller()
        self.mapping = mapping  # 速記符號對 應到 實際鍵盤
        self.show_hit = show_hit

    def _press(self, key, note_type):
        if key == "0":  # 休止符
            self._note_time(note_type)
            return
        else:
            self.keyboard.press(key)
            self._note_time(note_type)
            self.keyboard.release(key)

    def _press2(self, key1, key2, note_type):
        self.keyboard.press(key1)
        self.keyboard.press(key2)
        self._note_time(note_type)
        self.keyboard.release(key1)
        self.keyboard.release(key2)

    def _press4(self, key1, key2, key3, key4, note_type):
        self.keyboard.press(key1)
        self.keyboard.press(key2)
        self.keyboard.press(key3)
        self.keyboard.press(key4)
        self._note_time(note_type)
        self.keyboard.release(key1)
        self.keyboard.release(key2)
        self.keyboard.release(key3)
        self.keyboard.release(key4)

    def hit(self, interval, note_type=None):
        """
        :param interval: 音程，速記表達。
        :param note_type: 幾分音符
        :return:
        """
        if note_type is None:
            note_type = self.basic_type

        actual_key = self.mapping(interval)

        if self.show_hit:
            print(f"{interval}, {note_type}分音符.")
        # 實際按下鍵盤

        self._press(actual_key, note_type)

    def hit2(self, interval1, interval2, note_type=None):
        """
        :param interval: 音程，速記表達。
        :param note_type: 幾分音符
        :return:
        """
        if note_type is None:
            note_type = self.basic_type

        actual_key1 = self.mapping(interval1)
        actual_key2 = self.mapping(interval2)

        if self.show_hit:
            print(f"{actual_key1}{actual_key2}, {note_type}分音符.")
        # 實際按下鍵盤

        self._press2(actual_key1, actual_key2, note_type)

    def hit4(self, interval1, interval2, interval3, interval4, note_type=None):
        """
        :param interval: 音程，速記表達。
        :param note_type: 幾分音符
        :return:
        """
        if note_type is None:
            note_type = self.basic_type

        actual_key1 = self.mapping(interval1)
        actual_key2 = self.mapping(interval2)
        actual_key3 = self.mapping(interval3)
        actual_key4 = self.mapping(interval4)

        if self.show_hit:
            print(f"{actual_key1}{actual_key2}{actual_key3}{actual_key4}, {note_type}分音符.")
        # 實際按下鍵盤

        self._press4(actual_key1, actual_key2, actual_key3, actual_key4, note_type)


    def _note_time(self, t):
        """
        :param t: 幾 "分" 音符。
        :return:  幫音符睡覺
        !NOTE:
        BPM:120, 一個四分音符佔據 0.5 秒
        """
        time.sleep(60 / self.bpm * (4 / t))