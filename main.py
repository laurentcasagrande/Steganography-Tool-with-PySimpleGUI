import PySimpleGUI as sg
import os.path
import io
from PIL import Image
from steg import encode, decode

global OriginalFilename 
OriginalFilename = ""
global DecodeFilename 
DecodeFilename = ""

def resize_image(image_path, max_width, max_height):
    img = Image.open(image_path)
    img.thumbnail((max_width, max_height))
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    return bio.getvalue()

tab1_left = [
[
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER1-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST1-"
        )
    ],
    [sg.Image(key="-IMAGE1-", size=(300,  200))],
]
tab2_left = [
[
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER2-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST2-"
        )
    ],
    [sg.Image(key="-IMAGE2-", size=(300,  200))],
]

tab1_right = [
    [sg.Multiline(size=(40, 17), key='-PLAINTEXT-')],
    [sg.Button('ENCODE', size=(10,  2))],
    [sg.Multiline(size=(40, 2), key='-FilepathNew-')],
    [sg.Image(key="-IMAGE-3", size=(300,  200))],
]
tab2_right = [
    [sg.Button('DECODE', size=(10,  2))],
    [sg.Multiline(size=(40, 30), key='-RESULTTEXT-')],
]

tab1_layout = [
    [
        sg.Column(tab1_left),
        sg.VSeperator(),
        sg.Column(tab1_right),
    ]

]

tab2_layout = [
    [
        sg.Column(tab2_left),
        sg.VSeperator(),
        sg.Column(tab2_right),
    ]

]

layout = [
    [
        sg.TabGroup([
            [sg.Tab('encode', tab1_layout)],
            [sg.Tab('decode', tab2_layout)]
        ])
    ]
]

window = sg.Window("Steganographie", layout)

# Event loop to handle window interactions
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-FOLDER1-":
        folder = values["-FOLDER1-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png"))
        ]
        window["-FILE LIST1-"].update(fnames)

    elif event == "-FILE LIST1-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER1-"], values["-FILE LIST1-"][0])
            OriginalFilename = filename
            resized_image = resize_image(filename, 300, 200)
            window["-IMAGE1-"].update(data=resized_image)

        except:
            pass

    elif event == "ENCODE":
        input_text = values['-PLAINTEXT-']
        imgPath = OriginalFilename
        result_file_path = encode(imgPath, input_text)
        window["-IMAGE-3"].update(data=resized_image)
        window["-FilepathNew-"].update(result_file_path)

    if event == "-FOLDER2-":
        folder = values["-FOLDER2-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png"))
        ]
        window["-FILE LIST2-"].update(fnames)

    elif event == "-FILE LIST2-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER2-"], values["-FILE LIST2-"][0])
            DecodeFilename = filename
            resized_image = resize_image(filename, 300, 200)
            window["-IMAGE2-"].update(data=resized_image)

        except:
            pass

    elif event == "DECODE":
        imgPath = DecodeFilename
        result_message = decode(imgPath)
        window["-RESULTTEXT-"].update(result_message)


window.close()
