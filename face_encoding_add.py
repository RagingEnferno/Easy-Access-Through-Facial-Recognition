import face_recognition
import PIL.Image
import PIL.ImageDraw


def encode(file_name):
    # Load the known images
    image_of_person = face_recognition.load_image_file(file_name)
    print("Images loaded")

    # Get the face encoding of each person. This can fail if no one is found in the photo.
    person_face_encoding = face_recognition.face_encodings(image_of_person)[0]
    print("Encodings created")
    # Create a list of all known face encodings
    known_face_encoding = person_face_encoding

    print("Encodings placed in known faces array")
    #print(f"Encoding info: {known_face_encoding}")
    print(type(known_face_encoding))
    return known_face_encoding
