import ezax.face_encoding_add
import ezax.camera_feed
import ezax.face_encoding_check
import ezax.draw
import time

file_path = "/Users/joshpersaud/PycharmProjects/EZAX/images/test_face.jpg"
start = time.time()
#Creating encodings of a new user to add to database
##print (file_path)
ezax.draw.draw_on_image(file_path)
known_face_encoding_test = ezax.face_encoding_add.encode(file_path)

#ezax.face_encoding_check.check(known_face_encoding_test)


end = time.time()
print(end - start)