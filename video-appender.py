# Video Appender
# Created by Liam Moore
# March 1st, 2020

import subprocess
import os

# find current working directory
cwd = os.getcwd()

# take initial input
print(".--------------------------------------------------.")
print("|--------------- Video Appender v1.0 --------------|")
print("| MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS  |")
print("| THE VIDEOS YOU WISH TO USE IN YOUR FINAL PRODUCT |")
print("'--------------------------------------------------'")
video = input("Enter filenames for 2 videos (or type quit): ")

while video != "quit":
    # divide video 1 and 2
    two_videos = video.split(" ")
    video1 = two_videos[0]
    video2 = two_videos[1]
    
    # locate files
    video1_input_path = cwd + '/' + video1
    video2_input_path = cwd + '/' + video2

    # check if file exists
    if ((not os.path.exists(video1)) or (not os.path.exists(video2))):
        print("One of the files specified does not exist. Please try again.")
    else:
        # convert video file name into segment file name
        video1_list = video1.split(".")
        video2_list = video2.split(".")
        video_name = video1_list[0] + "-" + video2_list[0]

        # check if segments path exists, make the directory if not
        if not os.path.exists(cwd + '/Results'):
            print("No results folder found, creating one now...")
            os.mkdir(cwd + "/Results")
            print("Folder created.")
        else:
            print("Results folder found.")

        # write files to temp txt file
        file1 = open("temp.txt","w")
        file1.write("file " + video1 + "\nfile " + video2)
        file1.close()

        # output segment
        video_output_path = cwd + '/Results/' + video1 + "-" + video2
        print("Working...")
        subprocess.call(['ffmpeg', '-loglevel', 'quiet', '-f', 'concat', '-safe', '0', '-i', 'temp.txt', '-c', 'copy', video_output_path])
        os.remove("temp.txt")

        # completion message
        print(video1 + " and " + video2 + " were concatinated successfully.")

    # take input to continue loop
    video = input("Enter filenames for 2 videos (or type quit): ")

print("Exiting...")