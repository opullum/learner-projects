import os  											# System Manipulation
import shutil										# File Movement
from datetime import date, time, datetime			# Date Information / Logs
from pathlib import Path							# File Pathing

log_file = "organizer_log.txt" ; log_message = "" ; name_addition = 1
datetime_obj = datetime.now() ; print(datetime_obj)

# Default Downloads Folder (Modify if organizing a different folder)
downloads_dir = Path.home() / 'Downloads'  			
os.chdir(downloads_dir)

# Generated Subdirectories
organizer_subdirs = ['Documents', 'Images', 'Videos', 'Audio', 'Other', 'Archives']

# File Categories 
video_types = ['.mp4', '.avi', '.mov', '.flv', '.wmv', '.mkv', '.webm', '.mpeg', '.mpg', '.m4v']
audio_types = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a']
document_types = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv', '.rtf']
image_types = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']
archive_types = ['.zip', '.rar']

file_dict = {}

# Adding all file types to file_dict with path to related subdirectory
for file_type in video_types:
	file_dict[file_type] = os.path.join(downloads_dir, 'Videos')

for file_type in audio_types:
	file_dict[file_type] = os.path.join(downloads_dir, 'Audio')

for file_type in document_types:
	file_dict[file_type] = os.path.join(downloads_dir, 'Documents')

for file_type in image_types:
	file_dict[file_type] = os.path.join(downloads_dir, 'Images')

for file_type in archive_types:
    file_dict[file_type] = os.path.join(downloads_dir, 'Archives')


# Function to verify duplicates and return a string of the file.
# Assuming duplicate: example.txt -> example(1).txt
def verify_duplicates(file, directory_path) -> str:

	name_extension = 1
	file_name = file.split('.')[0]
	file_extension = "." + file.split('.')[1]
	checked_path = os.path.join(directory_path, file)

	returned_file = file

	if os.path.exists(checked_path):
		new_file = file_name + "({})".format(name_extension) + file_extension
		checked_path = os.path.join(directory_path, new_file)

		while (os.path.exists(checked_path)):
			name_extension += 1
			new_file = file_name + "({})".format(name_extension) + file_extension
			checked_path = os.path.join(directory_path, new_file)
			
		returned_file = new_file

	return returned_file

# Check if above subdirectories exist
for subdir in organizer_subdirs:
	checked_path = os.path.join(downloads_dir, subdir)

	if not os.path.exists(checked_path):
		message = "[NOTICE]: Unable to find {} directory in {}. \
		Creating directory.\n".format(subdir, downloads_dir)
		log_message += message
		os.mkdir(subdir)

# Move files into relevant/marked subdirectories
for file in os.listdir(downloads_dir):
	
	current_file = file 							# DO NOT DELETE THIS LINE

	# Organization of files + duplication checking
	if os.path.isfile(file):

		file_name = file
		file_path = os.path.join(downloads_dir, file)

		# Retrieve file extension and designate correct target directory
		# If no extension (IndexError), move to 'Other' directory
		try:
			file_name = file.split('.')[0]
			file_extension = "." + file.split('.')[1]
			file_path = os.path.join(downloads_dir, file)

			if file_extension in file_dict:
				destination_folder = file_dict[file_extension]
			else:
				destination_folder = os.path.join(downloads_dir, "Other")
		except IndexError as error:
			destination_folder = os.path.join(downloads_dir, "Other")
			log_message += "[ERROR]: Unable to find extension for {}, file\
				will be moved to 'Other'\n".format(file)
		except:
			log_message += "[ERROR]: An unknown error has occured for {}".format(file)

		# Move file to target directory (destination_folder, checked_path)
		checked_path = os.path.join(destination_folder, file)
		if os.path.exists(checked_path):
			new_file = verify_duplicates(file, destination_folder)
			old_path = os.path.join(downloads_dir, file)
			new_path = os.path.join(downloads_dir, new_file)

			os.rename(old_path, new_path)
			file_path = new_path
			current_file = new_file

			log_message += "[RENAME]: {} renamed to {}\n".format(file, new_file)

		shutil.move(file_path, destination_folder)

		log_message += "[MOVE]: Moved {} to {}.\n"\
		.format(current_file, destination_folder)

# Generating log file. Logs differentiated by numerical index.
if os.path.isfile(log_file):

	log_name = log_file.split('.')[0]

	# Add name addition to log file if log file already present
	new_file = log_name + "({})".format(name_addition) + ".txt"

	# Update name addition in order to create a unique log file
	while (os.path.isfile(new_file)):
		name_addition += 1
		new_file = log_name + "({})".format(name_addition) + ".txt"

	log_file = new_file

	# Create new log file with name addition
	# TODO: This might be redundant, might remove or rewrite to remove.
	with open(new_file, "w") as generated_log:
		# log_file = generated_log
		pass

print("DEBUG: {}".format(log_file))

# Generate log file as "organizer_log.txt"
# Duplicate log files generated following organizer_log(#) format
with open(log_file, "a") as created_log:
	created_log.write("Generated Log {}\n\n".format(datetime_obj))
	created_log.write(log_message)
		
