from cv2 import *
import face_recognition
import PIL.Image
import PIL.ImageDraw
import os


def draw_on_image(file_path):

    absFilePath = os.path.abspath(__file__)
    #print(absFilePath)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    #print(fileDir)
    parentDir = os.path.dirname(fileDir)
    #print(parentDir)


    drawnCounter = 0;
    while os.path.isfile(f"{parentDir}/images/drawn/camera_feed_drawn{drawnCounter}.png"):
        drawnCounter += 1

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(file_path)

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image,number_of_times_to_upsample=2)

    number_of_faces = len(face_locations)
    print("{} detected face(s) are in photograph.".format(number_of_faces))

    # Load the image into a Python Image Library object so that we can draw on top of it and display it
    pil_image = PIL.Image.fromarray(image)

    for face_location in face_locations:

        # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # Let's draw a box around the face
        draw = PIL.ImageDraw.Draw(pil_image)
        draw.rectangle([left, top, right, bottom], outline="green", width=3)

    # Display the image on screen
    pil_image.show()
    pil_image.save(f"{parentDir}/images/drawn/camera_feed_drawn{drawnCounter}.png")  # save image