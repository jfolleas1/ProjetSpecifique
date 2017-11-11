# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
import os.path
import os
import subprocess
from src.util.Logger import Logger
# --------- Constant
MAKE_FILE = 'makefile'
MAKE_COMMAND = "make"
CLEAN = "clean"
NAME_EXECUTABLE = 'Node'

# --------- Code
class Arf():
    """
    This class is an implementation of Arf.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """

    def __init__(self, path):
        self.path = path
        self.logger = Logger('Arf')
        self.compile()

    def compile(self):
        """
        Compile the C++ Code
        :return:
        """
        executable = os.path.join(self.path, MAKE_FILE)
        self.logger.info('Compile C++ code to : '+str(executable))

        if os.path.isfile(executable):
            try:
                old_path = os.getcwd()
                # Change the current directory
                os.chdir(os.path.join(old_path, self.path))

                # clean the repo
                output = subprocess.check_output([MAKE_COMMAND, CLEAN], stderr=None)
                self.logger.debug('Make clean')
                # compile c++ code
            except subprocess.CalledProcessError as e:
                self.logger.error('Impossible to make clean')

            try :
                output = subprocess.check_output([MAKE_COMMAND], stderr=subprocess.STDOUT)
                self.logger.debug('Make')

                # reset the olde path.
                os.chdir(old_path)

            except subprocess.CalledProcessError as e:
                os.chdir(old_path)
                raise(e)

        else:
            raise Exception("Impossible to compile Arf code")


    def execute_program(self, argv):
        """
        Call the c++ program.
        :param argv:
        :return:
        """
        size = None
        false_positive = None
        executable = os.path.join(self.path, NAME_EXECUTABLE)

        print
        if os.path.isfile(executable):
            try:
                old_path = os.getcwd()

                # Change the current directory
                os.chdir(os.path.join(old_path, self.path))

                # clean the repo
                command = './' + " ".join([NAME_EXECUTABLE] + argv)
                self.logger.debug("size: "+ argv[4])
                output = subprocess.check_output(command, shell=True, stderr=subprocess.PIPE)
                outputs = str(output).split("*");
                size = outputs[1]
                false_positive = outputs[3]

                # Reset the directory
                os.chdir(old_path)

            except subprocess.CalledProcessError as e:
                self.logger.error(e.output)
                self.logger.error("Impossible to run Node program")

        else:
            raise Exception("Impossible to find Node program")

        return size, false_positive