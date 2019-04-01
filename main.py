import ezax.face_encoding_add
import ezax.camera_feed
import ezax.face_encoding_check
import ezax.draw
import ezax.db_handler
# import ezax.gamma_correction
import ezax.dbstring_to_numpy

import time

start = time.time()
# string = '[-0.14823183  0.0543281   0.04626148 -0.07088158  0.01434997 -0.03614035\n  0.02501003 -0.04428252  0.1978464  -0.07014141  0.27182871 -0.05656781\n -0.18675409 -0.04942062 -0.06066782  0.09509175 -0.16608019 -0.13457559\n -0.03028907 -0.11046835  0.04872097  0.03688549 -0.05619908  0.10276458\n -0.19191274 -0.33372721 -0.0648403  -0.13081816  0.03427883 -0.07740398\n  0.0260397   0.1555182  -0.19160312  0.0271626   0.01160917  0.0742503\n  0.07061476  0.04501667  0.1039135   0.05015493 -0.12352262 -0.04270197\n  0.05900547  0.28029686  0.14380345  0.07356497 -0.00247031 -0.03565745\n  0.00558345 -0.20539272  0.06080673  0.12473325  0.09908337  0.04946435\n  0.08398582 -0.17217997 -0.04260138  0.01889472 -0.18459164  0.09914459\n  0.00364266 -0.05240592 -0.05683896 -0.0476675   0.14997715  0.08466082\n -0.13284706 -0.07591237  0.19465831 -0.20592418 -0.02210309  0.10076956\n -0.03475214 -0.17771077 -0.23275368  0.05787557  0.41968584  0.17577252\n -0.16279951  0.04689381 -0.06216305 -0.06967267  0.06100602  0.0373832\n -0.11200614  0.01070121 -0.08293446  0.03885819  0.15785082  0.11005643\n -0.01592756  0.20632514 -0.07020885 -0.0063909   0.00920514  0.05122937\n -0.08554705 -0.00242762 -0.06317925 -0.04049781 -0.03278577 -0.07698727\n -0.04923742  0.08122961 -0.18903962  0.13741885  0.01167844 -0.05140121\n -0.03423346  0.1359048  -0.05960591 -0.03416018  0.11817911 -0.28569198\n  0.1130022   0.15904799  0.03624955  0.18197984  0.01895189  0.07341117\n  0.00976183 -0.08293025 -0.12857604 -0.09358872 -0.00093982 -0.08831275\n  0.03589448  0.01440365]'
unknown_image_path = "/Users/joshpersaud/PycharmProjects/EZAX/images/camera_feed0.jpg"

print('\x1b[1;31;0m' + "THE COMMAND 'new image' MUST BE RAN FIRST ON PROGRAM STARTUP" + '\x1b[0m')
user_input = (input('Enter Command:').lower())

while user_input is not 'exit':

    if user_input == 'new image':
        file_path = ezax.camera_feed.camera_feed()
        print("File path of the new image is stored in the variable: 'file_path'")
        user_input = (input('Enter Command:').lower())
    if user_input == 'file path':  # Get file path of image created from camera feed
        print(file_path)
        user_input = (input('Enter Command:').lower())
    if user_input == 'draw detection box':  # Draw detection square around faces
        print("Drawing in progress")
        ezax.draw.draw_on_image(file_path)
        user_input = (input('Enter Command:').lower())
    if user_input == 'create encoding':  # Creating encodings of a new user & add to database
        new_encoding = ezax.face_encoding_add.encode(file_path)
        user_id = int(input('A 9 digit user ID number is required: '))
        while (ezax.db_handler.check_user_id(user_id)) is 0 and user_id is not 'quit':
            result = ezax.db_handler.check_user_id(user_id)
            user_id = int(input("Enter new 9 digit user ID or enter 'quit' to cancel: "))
        if user_id is not 'quit':
            ezax.db_handler.write_encoding(user_id, f"{new_encoding}")
        user_input = (input('Enter Command:').lower())
    if user_input == 'exit':
        exit()
    else:
        print('\x1b[1;31;0m' + "Command doesn't exist, enter new command or enter 'exit' to quit" + '\x1b[0m')
        user_input = (input('Enter Command:').lower())


# ezax.face_encoding_check.check(new_encoding, unknown_image_path)

# get stored encodings
ezax.db_handler.get_encoding(1)

# adjust image gamma if too dark
# ezax.gamma_correction.adjust_gamma(unknown_image_path, 1)

# get number of encodings in database
print(ezax.db_handler.get_row_count())

# print("test string", string)

print(ezax.dbstring_to_numpy.convert())
print(ezax.db_handler.get_encoding(0))
end = time.time()
print(end - start)
