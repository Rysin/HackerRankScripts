from matplotlib import pyplot as plt
import numpy as np
from random import choice


def angleTranslate(dest_ang):
    if dest_ang > -90:  # 179 to -179
        dest_yaw = dest_ang - 90
    else:
        dest_yaw = dest_ang + 270

    return dest_yaw


def angleTranslate_180(angle):
    return angle + 180


def angleTranslate360(angle):
    if angle < 0:
        angle = 360 + angle
    return angle


if __name__ == '__main__':
    angles = np.arange(-180, 180, 1)
    angles_translated = list(map(angleTranslate, angles))
    angles_translated_180 = list(map(angleTranslate_180, angles))
    angles_translated_full = list(map(angleTranslate360, angles_translated))

    plt.xkcd()
    # plt_style = choice(list(plt.style.available))
    # plt.style.use(plt_style)
    plt.tight_layout()
    plt.plot(angles, angles_translated_full, label='360_Converted', marker='*')
    plt.plot(angles, angles_translated_180, label='180_Converted')
    plt.xlabel("In game angles")
    plt.ylabel("Converted Angles")
    plt.title("Angle Relationship")
    # plt.subtitle(plt_style)
    # plt.plot(angles, angles_translated, label="-90 Converted", marker='+')
    plt.legend()
    plt.grid()
    plt.show()
