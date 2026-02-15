import time
import os

NOTE_SET = {
    # 第 0 八度 (C0 到 B0) - 极低音区
    "C0": 16,  # 16.35 Hz
    "C#0": 17,  # 17.32 Hz
    "Db0": 17,  # 17.32 Hz
    "D0": 18,  # 18.35 Hz
    "D#0": 19,  # 19.45 Hz
    "Eb0": 19,  # 19.45 Hz
    "E0": 21,  # 20.60 Hz
    "F0": 22,  # 21.83 Hz
    "F#0": 23,  # 23.12 Hz
    "Gb0": 23,  # 23.12 Hz
    "G0": 24,  # 24.50 Hz
    "G#0": 26,  # 25.96 Hz
    "Ab0": 26,  # 25.96 Hz
    "A0": 28,  # 27.50 Hz
    "A#0": 29,  # 29.14 Hz
    "Bb0": 29,  # 29.14 Hz
    "B0": 31,  # 30.87 Hz
    # 第 1 八度 (C1 到 B1)
    "C1": 33,  # 32.70 Hz
    "C#1": 35,  # 34.65 Hz
    "Db1": 35,  # 34.65 Hz
    "D1": 37,  # 36.71 Hz
    "D#1": 39,  # 38.89 Hz
    "Eb1": 39,  # 38.89 Hz
    "E1": 41,  # 41.20 Hz
    "F1": 44,  # 43.65 Hz
    "F#1": 46,  # 46.25 Hz
    "Gb1": 46,  # 46.25 Hz
    "G1": 49,  # 49.00 Hz
    "G#1": 52,  # 51.91 Hz
    "Ab1": 52,  # 51.91 Hz
    "A1": 55,  # 55.00 Hz
    "A#1": 58,  # 58.27 Hz
    "Bb1": 58,  # 58.27 Hz
    "B1": 62,  # 61.74 Hz
    # 第 2 八度 (C2 到 B2)
    "C2": 65,  # 65.41 Hz
    "C#2": 69,  # 69.30 Hz
    "Db2": 69,  # 69.30 Hz
    "D2": 73,  # 73.42 Hz
    "D#2": 78,  # 77.78 Hz
    "Eb2": 78,  # 77.78 Hz
    "E2": 82,  # 82.41 Hz
    "F2": 87,  # 87.31 Hz
    "F#2": 93,  # 92.50 Hz
    "Gb2": 93,  # 92.50 Hz
    "G2": 98,  # 98.00 Hz
    "G#2": 104,  # 103.83 Hz
    "Ab2": 104,  # 103.83 Hz
    "A2": 110,  # 110.00 Hz
    "A#2": 117,  # 116.54 Hz
    "Bb2": 117,  # 116.54 Hz
    "B2": 123,  # 123.47 Hz
    # 第 3 八度 (C3 到 B3) - 低音区
    "C3": 131,  # 130.81 Hz
    "C#3": 139,  # 138.59 Hz
    "Db3": 139,  # 138.59 Hz
    "D3": 147,  # 146.83 Hz
    "D#3": 156,  # 155.56 Hz
    "Eb3": 156,  # 155.56 Hz
    "E3": 165,  # 164.81 Hz
    "F3": 175,  # 174.61 Hz
    "F#3": 185,  # 185.00 Hz
    "Gb3": 185,  # 185.00 Hz
    "G3": 196,  # 196.00 Hz
    "G#3": 208,  # 207.65 Hz
    "Ab3": 208,  # 207.65 Hz
    "A3": 220,  # 220.00 Hz
    "A#3": 233,  # 233.08 Hz
    "Bb3": 233,  # 233.08 Hz
    "B3": 247,  # 246.94 Hz
    # 第 4 八度 (C4 到 B4) - 中音区（中央C所在八度）
    "C4": 262,  # 261.63 Hz - 中央C
    "C#4": 277,  # 277.18 Hz
    "Db4": 277,  # 277.18 Hz
    "D4": 294,  # 293.66 Hz
    "D#4": 311,  # 311.13 Hz
    "Eb4": 311,  # 311.13 Hz
    "E4": 330,  # 329.63 Hz
    "F4": 349,  # 349.23 Hz
    "F#4": 370,  # 369.99 Hz
    "Gb4": 370,  # 369.99 Hz
    "G4": 392,  # 392.00 Hz
    "G#4": 415,  # 415.30 Hz
    "Ab4": 415,  # 415.30 Hz
    "A4": 440,  # 440.00 Hz - 标准音
    "A#4": 466,  # 466.16 Hz
    "Bb4": 466,  # 466.16 Hz
    "B4": 494,  # 493.88 Hz
    # 第 5 八度 (C5 到 B5) - 高音区
    "C5": 523,  # 523.25 Hz
    "C#5": 554,  # 554.37 Hz
    "Db5": 554,  # 554.37 Hz
    "D5": 587,  # 587.33 Hz
    "D#5": 622,  # 622.25 Hz
    "Eb5": 622,  # 622.25 Hz
    "E5": 659,  # 659.25 Hz
    "F5": 698,  # 698.46 Hz
    "F#5": 740,  # 739.99 Hz
    "Gb5": 740,  # 739.99 Hz
    "G5": 784,  # 783.99 Hz
    "G#5": 831,  # 830.61 Hz
    "Ab5": 831,  # 830.61 Hz
    "A5": 880,  # 880.00 Hz
    "A#5": 932,  # 932.33 Hz
    "Bb5": 932,  # 932.33 Hz
    "B5": 988,  # 987.77 Hz
    # 第 6 八度 (C6 到 B6) - 极高音区
    "C6": 1047,  # 1046.50 Hz
    "C#6": 1109,  # 1108.73 Hz
    "Db6": 1109,  # 1108.73 Hz
    "D6": 1175,  # 1174.66 Hz
    "D#6": 1245,  # 1244.51 Hz
    "Eb6": 1245,  # 1244.51 Hz
    "E6": 1319,  # 1318.51 Hz
    "F6": 1397,  # 1396.91 Hz
    "F#6": 1480,  # 1479.98 Hz
    "Gb6": 1480,  # 1479.98 Hz
    "G6": 1568,  # 1567.98 Hz
    "G#6": 1661,  # 1661.22 Hz
    "Ab6": 1661,  # 1661.22 Hz
    "A6": 1760,  # 1760.00 Hz
    "A#6": 1865,  # 1864.66 Hz
    "Bb6": 1865,  # 1864.66 Hz
    "B6": 1976,  # 1975.53 Hz
    # 第 7 八度 (C7 到 B7) - 超高音区
    "C7": 2093,  # 2093.00 Hz
    "C#7": 2217,  # 2217.46 Hz
    "Db7": 2217,  # 2217.46 Hz
    "D7": 2349,  # 2349.32 Hz
    "D#7": 2489,  # 2489.02 Hz
    "Eb7": 2489,  # 2489.02 Hz
    "E7": 2637,  # 2637.02 Hz
    "F7": 2794,  # 2793.83 Hz
    "F#7": 2960,  # 2959.96 Hz
    "Gb7": 2960,  # 2959.96 Hz
    "G7": 3136,  # 3135.96 Hz
    "G#7": 3322,  # 3322.44 Hz
    "Ab7": 3322,  # 3322.44 Hz
    "A7": 3520,  # 3520.00 Hz
    "A#7": 3729,  # 3729.31 Hz
    "Bb7": 3729,  # 3729.31 Hz
    "B7": 3951,  # 3951.07 Hz
    # 第 8 八度 (C8 到 B8) - 极限音区
    "C8": 4186,  # 4186.01 Hz
    "C#8": 4435,  # 4434.92 Hz
    "Db8": 4435,  # 4434.92 Hz
    "D8": 4699,  # 4698.63 Hz
    "D#8": 4978,  # 4978.03 Hz
    "Eb8": 4978,  # 4978.03 Hz
    "E8": 5274,  # 5274.04 Hz
    "F8": 5588,  # 5587.65 Hz
    "F#8": 5920,  # 5919.91 Hz
    "Gb8": 5920,  # 5919.91 Hz
    "G8": 6272,  # 6271.93 Hz
    "G#8": 6645,  # 6644.88 Hz
    "Ab8": 6645,  # 6644.88 Hz
    "A8": 7040,  # 7040.00 Hz
    "A#8": 7459,  # 7458.62 Hz
    "Bb8": 7459,  # 7458.62 Hz
    "B8": 7902,  # 7902.13 Hz
}


def bRest(note):
    """
    判断是否为休止符
    """
    if not note:
        return False
    # 检查是否只包含数字和小数点
    for char in note:
        if char not in "0123456789.":
            return False
    # 检查小数点个数
    if note.count(".") > 1:
        return False
    # 如果是整数（没有小数点）
    if "." not in note:
        return note.isdigit()  # 确保全是数字
    # 处理小数情况
    parts = note.split(".")
    # 应该正好有两部分（小数点前和后）
    if len(parts) != 2:
        return False
    # 小数点前后都应该是数字 且不允许为空
    if not parts[0] or not parts[1]:
        return False
    # 检查两部分是否都是数字
    if not parts[0].isdigit() or not parts[1].isdigit():
        return False
    return True


def bValidNote(note):
    """
    验证音符格式
    """
    # 空字符串
    if not note:
        return False
    if bRest(note):
        return True
    # 检查第一个字符是否是字母 A-G
    if note[0] not in "ABCDEFG":
        return False
    # 处理可能的升号
    index = 1
    if len(note) > 1 and note[1] == "#":
        index = 2
    # 剩余部分应该全是数字
    if index >= len(note):
        return False
    # 检查剩余部分是否都是数字
    for char in note[index:]:
        if not char.isdigit():
            return False
    # 验证数字范围
    num = int(note[index:])
    if num < 0 or num > 8:
        return False
    return True


def toFloat(num_str):
    """
    将数字字符串转换为无前导0的形式
    num_str：一定符合整数或小数的字符串，可能有前导0
    return：无前导0的整数或小数字符串
    """
    if not num_str:
        return num_str
    try:
        # 先转换为数字，再转回字符串
        if "." in num_str:
            # 小数
            num = float(num_str)
            # 获取小数位数
            decimal_places = len(num_str.split(".")[1])
            # 使用原小数位数格式化
            result = format(num, f".{decimal_places}f")
            # 去掉可能的小数点后多余的0（可选）
            # result = result.rstrip('0').rstrip('.') if '.' in result else result
        else:
            # 整数
            num = int(num_str)
            result = str(num)
        return result
    except ValueError:
        return num_str  # 转换失败返回原字符串


def play(note):
    if bRest(note):
        time.sleep(float(note))
    else:  # 非休止
        pitch = NOTE_SET[note]
        result = os.system(f"beep -f {pitch}")
        if result != 0:
            print("beep失败! 你的电脑可能没有安装beep")
            exit()
        else:
            print(note)


if __name__ == "__main__":
    originNotes = input("请输入乐谱")
    # originNotes应该是这样的 "C3 0.3 C4 0.3 C#3 0.6 Cb3"
    notes = originNotes.split()
    for note in notes:
        if not bValidNote(note):
            print(f"无效的音符: {note}")
            exit()
        else:
            if not bRest(note):
                print(f"正在弹奏: {note}")
            play(note)
