# --------------------------------------------------------------------#
# OS Module:

# The OS module in Python provides a way of using operating system dependent functionality.
# The functions that the OS module provides allows you to interface with the underlying operating--
# --system that Python is running on – be that Windows, Mac or Linux.
# The OS module in Python provides a way of using operating system dependent functionality.
# --------------------------------------------------------------------#

import os  # Import the OS module.

# --------------------------------------------------------------------#

# the most important functions in the OS module are:

os.getcwd()  # Returns the current working directory.

os.chdir()  # Change the current working directory.

os.listdir()  # Returns a list of all files and directories in the specified directory.

os.mkdir()  # Create a new directory.

os.rename()  # Rename a directory.

os.rmdir()  # Remove a directory.

os.path.exists()  # Check if a file exists.

os.path.isdir()  # Check if a directory exists.

os.path.isfile()  # Check if a file exists.

os.path.split()  # Split the path name into a pair head and tail.

os.path.splitext()  # Split the extension from a path.

os.path.getsize()  # Get the size of a file.

os.path.getmtime()  # Get the last modification time of a file.

os.path.getatime()  # Get the last access time of a file.

# --------------------------------------------------------------------#

# Get the current working directory:

os.getcwd()

# Change the current working directory:

os.chdir('C:\\Users\\User\\Desktop\\Python')


# List the content of a directory:

os.listdir()

# Create a new directory:

os.mkdir('new_dir')

# Rename a directory:

os.rename('new_dir', 'new_dir2')

# Remove a directory:

os.rmdir('new_dir2')

# Check if a file exists:

os.path.exists('file.txt')

# Check if a directory exists:

os.path.isdir('new_dir2')

# Check if a file exists:

os.path.isfile('file.txt')

# Split the path name into a pair head and tail:

os.path.split('C:\\Users\\User\\Desktop\\Python\\file.txt')

# Split the extension from a path:

os.path.splitext('C:\\Users\\User\\Desktop\\Python\\file.txt')

# Get the size of a file:

os.path.getsize('file.txt')

# Get the last modification time of a file:

os.path.getmtime('file.txt')

# Get the last access time of a file:

os.path.getatime('file.txt')

# Get the creation time of a file:

os.path.getctime('file.txt')

# Check if a file is a symbolic link:

os.path.islink('file.txt')

# Check if a file is a mount point:

os.path.ismount('file.txt')

# Get the system configuration:

os.uname()

# Get the environment variables:

os.environ

# Get the value of an environment variable:

os.getenv('HOME')

# Set the value of an environment variable:

os.putenv('HOME', '/new_home')

# Get the current user:

os.getlogin()

# Get the effective group id:

os.getegid()

# Get the effective user id:

os.geteuid()

# Get the real group id:

os.getgid()

# Get the real user id:

os.getuid()

# Get the group ids:

os.getgroups()

# Get the process id:

os.getpid()

# Get the parent process id:

os.getppid()

# Get the effective process group id:

os.getpgid()

# Get the process group id:

os.getpgrp()

# Get the process group id of the session leader:

os.getsid()