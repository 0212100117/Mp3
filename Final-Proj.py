# HOW TO IMPORT PACKAGES: go to File -> Settings -> Project -> Project Interpreter
# Then Click the "+" for adding Packages.
# Then Search for the Packages and Click the "Install Package" in the Bottom Left.
# Wait for the Confirmation of Installation before exiting the window.
# Ignore this if you have this Program Project Folder.
# No Need to Import re and os as they are Built-In Packages.

# Importing necessary packages
import tkinter
#  imports the "namespace" Tkinter in your namespace
#  and "renames" it locally to 'tk' to save you typing

from tkinter import *
# imports every exposed object in Tkinter into your current namespace

from tkinter import messagebox, filedialog
# imports messagebox and filedialog methods
# to allows you to display messagebox and browse files with filedialog.

from pytube import YouTube
# Used for downloading YouTube Videos by using links

from moviepy.audio.io.AudioFileClip import AudioFileClip
# Used for converting the downloaded mp4 files into mp3 files.

import requests
# Used for downloading files outside YouTube as well as Documents.

import re
import os
import sys


# Defining CreateWidgets() function
# to create necessary tkinter widgets.
def Widgets():
    # Defining the Configuration for the File Format Label Box
    link_format = Label(root,
                        text="  File Format: ",
                        bg="#1E90FF",
                        fg="#ffffff",
                        bd=1,
                        relief="solid", )

    # Defining the position of the File Format Label Box
    link_format.grid(row=1,
                     column=0,
                     pady=5,
                     padx=5)

    # Defining the Configuration of the Entry Text Box for the
    # File Format
    # 'textvariable=file_format' acts as the variable of the
    # text inputted in the Entry.
    root.formatText = Entry(root,
                            width=40,
                            textvariable=file_format,
                            bd=2)

    # Defining the position of the File Format Entry Box.
    root.formatText.grid(row=1,
                         column=1,
                         pady=5,
                         padx=5, )

    # Defining the Configuration of the File Link Label Box.
    link_label = Label(root,
                       text="     File link:     ",
                       bg="#1E90FF",
                       fg="#ffffff",
                       bd=1,
                       relief="solid")

    # Defining the position of the File Link Label Box
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    # Defining the Configuration the Entry text Box
    # for the File Link
    # 'textvariable=file_link' acts as the variable of the
    # text inputted in the Entry for the YouTube Link.
    root.linkText = Entry(root,
                          width=55,
                          textvariable=file_link,
                          fg="#000000",
                          bd=2)

    # Defining the position of the File Link Entry Box
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    # Defining the Configuration of Destination Label Box.
    destination_label = Label(root,
                              text="  Destination: ",
                              bg="#1E90FF",
                              fg="#ffffff",
                              bd=1,
                              relief="solid")

    # Defining the position of the Destination Label Box
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    # Defining the Configuration of the Entry text Box
    # for the Destination.
    # 'textvariable=download_path' acts as the variable of the
    # text inputted in the Entry for the Destination of the
    # to be downloaded files.
    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_path,
                                 fg="#000000",
                                 bd=2)

    # Defining the position of the Destination Entry Box
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    # Defining the Configuration of the Browse Button.
    # 'command=Browse' acts as the On Click reaction for
    # Browse Button.
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      fg="#ffffff",
                      bg="#1E90FF")

    # Defining the position of the Browse Button.
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    # Defining the Configuration of the Download Button.
    # 'command=Browse' acts as the On Click reaction for
    # Download Button.
    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        fg="#ffffff",
                        bg="#1E90FF")

    # Defining the position of the Download Button.
    Download_B.grid(row=4,
                    column=1,
                    pady=3,
                    padx=3)

    # Defining the Configuration of the Instructions Button.
    # 'command=Instruction' acts as the On Click reaction for
    # Instructions Button.
    info_B = Button(root,
                    text="Instructions",
                    command=Instruction,
                    width=10,
                    fg="#ffffff",
                    bg="#1E90FF")

    # Defining the position of the Instructions Button.
    info_B.grid(row=1,
                column=2,
                pady=1,
                padx=1)


# Defining Browse() to select a
# destination folder to save the video.
def Browse():
    # Presenting the user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory in the directory
    # textbox
    download_path.set(download_directory)


# Defining Instruction() for the preview
# on how to use the Application
def Instruction():
    # Displaying the Instructions
    # on a pop up message.
    messagebox.showinfo("THIS IS HOW YOU USE IT",
                        '''1st  Step: Input the File format you want for you want for 
                  your Download.(mp4/mp3/document)\n
2nd Step: Input the File Link you want to 
                  Download.\n
3rd Step: Input or Browse the Destination for your 
                 Downloaded File.\n
4th Step: Click Download and wait for the message for the 
                completion of Download.\n
REMINDERS: Don't SAVE a mp3 file to a Destination 
                      containing mp4 files, as it will override the 
                      mp4 files format and converting them all 
                      into mp3 files.
                      
                     Only Supported Document Formats are only: 
                     docx, doc, pdf, ppt, and xls\n''')


# Defining Download() for the Downloading
# Process of the Files.
def Download():

    # The Process if the Input File Format is "mp3".
    if file_format.get() == "mp3":

        # The Process if the Input Link ends with "mp4".
        if file_link.get().endswith("mp4"):

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # create request object
            request = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_folder, file_name)

            # download started
            with open(path, 'wb') as f:
                for chunk in request.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

            # Start of Converting the Downloaded mp4 file into mp3 file
            for file in os.listdir(download_folder):
                if re.search('mp4', file):
                    mp4_format = os.path.join(download_folder, file)
                    mp3_format = os.path.join(download_folder, os.path.splitext(file)[0] + '.mp3')
                    new_file_format = AudioFileClip(mp4_format)
                    new_file_format.write_audiofile(mp3_format)
                    os.remove(mp4_format)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_folder)

        # The Process if the Input Link ends with "mp3".
        elif file_link.get().endswith("mp3"):

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # create response object
            r = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_folder, file_name)

            # Download started
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=5291456):
                    if chunk:
                        f.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_folder)

        # The Process if the Input Link is a YouTube Link.
        else:
            # Using Try and Except Codes to verify the
            # given YouTube Link is a Legitimate YouTube Link
            try:

                # Getting the Input from the YouTube Video
                # Entry Box and referencing it to another
                # Variable
                Youtube_link = file_link.get()

                # Creating object of YouTube()
                # Verifying if the Variable is actually
                # a YouTube Video Link.
                yt_link = YouTube(Youtube_link)

            # If the given Link is not a Youtube Link
            # a Warning Message will be given to the User.
            except:

                messagebox.showwarning("INVALID lINK INPUT",
                                       '''ONLY USE "mp3", "mp4", "YouTube Links" or "document" AS LINK INPUTS!!\n''')

                # Ending the Process of the Program.
                return sys

            # If the given Link is A YouTube Link,
            # The process will be continued.

            # Getting all the available streams of the
            # YouTube Video and selecting the one with
            # the Lowest Resolution.
            # This is to make sure that the size of the
            # Downloaded File will be in the minimum size
            # thus, shortening the time for the conversion
            videoStream = yt_link.streams.get_lowest_resolution()

            # select the optimal location for
            # saving the file.
            download_folder = download_path.get()

            # Downloading the video to the destination
            # directory.
            videoStream.download(download_folder)

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Start of Converting the Downloaded mp4 file into mp3 file
            for file in os.listdir(download_folder):
                if re.search('mp4', file):
                    mp4_format = os.path.join(download_folder, file)
                    mp3_format = os.path.join(download_folder, os.path.splitext(file)[0] + '.mp3')
                    new_file_format = AudioFileClip(mp4_format)
                    new_file_format.write_audiofile(mp3_format)
                    os.remove(mp4_format)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_folder)

            # MP3 Download Process Finished

    # The Process if the Input is "mp4".
    elif file_format.get() == "mp4":

        # The Process if the Input Link ends with "mp4".
        if file_link.get().endswith("mp4"):

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # create response object
            r = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_folder, file_name)

            # download started
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_folder)

        # The Process if the Input Link is a YouTube Link.
        else:

            # Using Try and Except Codes to verify the
            # given YouTube Link is a Legitimate YouTube Link
            try:

                # Getting the Input from the YouTube Video
                # Entry Box and referencing it to another
                # Variable
                Youtube_link = file_link.get()

                # Creating object of YouTube()
                # Verifying if the Variable is actually
                # a YouTube Video Link.
                yt_link = YouTube(Youtube_link)

            # If the given Link is not a Youtube Link
            # a Warning Message will be given to the User.
            except:

                messagebox.showwarning("INVALID LINK INPUT",
                                       '''ONLY USE "mp3", "mp4", "YouTube Links", or "document" AS LINK INPUTS!!\n''')

                # Ending the Process of the Program.
                return sys

            # If the given Link is A YouTube Link,
            # The process will be continued.

            # Getting all the available streams of the
            # YouTube Video and selecting the one with
            # the Highest Resolution.
            videoStream = yt_link.streams.get_highest_resolution()

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # select the optimal location for
            # saving the file.
            download_folder = download_path.get()

            # Downloading the video to destination
            # directory
            videoStream.download(download_folder)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_folder)

    # The Process if the Input is "document".
    elif file_format.get() == "document":

        # The Process if the Input Link ends with "pdf".
        if file_link.get().endswith("pdf"):

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # create response object
            r = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_Folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_Folder, file_name)

            # download started
            with open(path, "wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):

                    # writing one chunk at a time to pdf file
                    if chunk:
                        pdf.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_Folder)

        # The Process if the Input Link ends with "ppt".
        elif file_link.get().endswith("ppt"):

            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # create response object
            ppt_req = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_Folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_Folder, file_name)

            # download started
            with open(path, "wb") as ppt:
                for chunk in ppt_req.iter_content(chunk_size=1024):
                    # writing one chunk at a time to ppt file
                    if chunk:
                        ppt.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_Folder)

        # The Process if the Input Link ends with "word".
        elif file_link.get().endswith("docx"):
            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # create response object
            docx_req = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_Folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_Folder, file_name)

            # download started
            with open(path, "wb") as docx:
                for chunk in docx_req.iter_content(chunk_size=1024):

                    # writing one chunk at a time to docx file
                    if chunk:
                        docx.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_Folder)

        elif file_link.get().endswith("doc"):
            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # create response object
            doc_req = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_Folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_Folder, file_name)

            # download started
            with open(path, "wb") as doc:
                for chunk in doc_req.iter_content(chunk_size=1024):

                    # writing one chunk at a time to docx file
                    if chunk:
                        doc.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_Folder)

        elif file_link.get().endswith("xls"):
            # pop up message informing the User that
            # the Download has started.
            messagebox.showinfo("DOWNLOAD Start",
                                "Downloading the File.")

            # Removing "/" so that the file name will be clean.
            file_name = file_link.get().split('/')[-1]

            # create response object
            xls_req = requests.get(file_link.get(), stream=True)

            # Select the optimal location for
            # saving the File.
            download_Folder = download_path.get()

            # Anchoring the Download Location and the File
            # together so that the File will be saved in the
            # desired Location.
            path = os.path.join(download_Folder, file_name)

            # download started
            with open(path, "wb") as xls:
                for chunk in xls_req.iter_content(chunk_size=1024):

                    # writing one chunk at a time to docx file
                    if chunk:
                        xls.write(chunk)

            # pop up message informing the User that
            # the Download has Finished.
            messagebox.showinfo("SUCCESSFULLY",
                                "DOWNLOADED AND SAVED IN\n"
                                + download_Folder)

    # The Process if the Input is
    # neither "mp3", "mp4", or "document" .
    else:
        # Displaying a Warning Message.
        messagebox.showwarning("INVALID INPUT FORMAT",
                               '''ONLY USE "mp3", "mp4", or "document" AS INPUT FORMAT!!\n''')


# creating the variable for tk
root = tkinter.Tk()

# Setting up the size of the window.
root.geometry("434x125")

# Disabling the resizing Property
root.resizable(False, False)

# Setting up the Title of the Window
root.title("3 in 1 File Downloader")

# Setting up the Background Color of the Window.
root.config(background="#ffffff")

# Creating the tkinter Variables 
file_link = StringVar()
download_path = StringVar()
file_format = StringVar()
instruction = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run 
# the application
root.mainloop()
