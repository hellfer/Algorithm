wavelength = int(input())

if 620 <= wavelength <= 780:
    color = "Red"
elif 590 <= wavelength < 620:
    color = "Orange"
elif 570 <= wavelength < 590:
    color = "Yellow"
elif 495 <= wavelength < 570:
    color = "Green"
elif 450 <= wavelength < 495:
    color = "Blue"
elif 425 <= wavelength < 450:
    color = "Indigo"
elif 380 <= wavelength < 425:
    color = "Violet"

print(color)
