import face_recognition


def check(known_face_encodings, unknown_image_path):
    # Load the image we want to check
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    # Get face encodings for any people in the picture
    face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=2)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image, known_face_locations=face_locations)

    # There might be more than one person in the photo, so we need to loop over each face we found
    for unknown_face_encoding in unknown_face_encodings:

        # Test if this unknown face encoding matches any of the three people we know
        results = face_recognition.compare_faces([known_face_encodings], unknown_face_encoding, tolerance=0.6)

        name = "Unknown"

        print(f"Match: {results}")