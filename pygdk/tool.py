RED  = '\033[31m' # Red
YELLOW = '\033[93m' # Yellow
ENDC  = '\033[0m'  # End Color

class Tool:

################################################################################
# Tool.__init__() -- Initialize based on parameter dictionary
################################################################################

    def __init__(self, machine, dict=None, i=None):
        if dict and i:
            self._units = dict.get('units', None)
            self._shape = dict.get('shape', None)
            self._length = dict.get('length', None)
            self._diameter = dict.get('diameter', None)
            self._description = dict.get('description', None)
            self._number = i
            diameter = self._diameter * (25.4 if self._units == 'imperial' else 1)
            print(f";{YELLOW} Looking up Tool {i} in Tool Table: [{self._description}] | {diameter:.4f} mm{ENDC}")

################################################################################
# Tool.number -- Tool Table Index
################################################################################

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

################################################################################
# Tool.diameter -- Diameter of the Tool
################################################################################

    @property
    def diameter(self):
        if hasattr(self, '_diameter') and self._diameter is not None:
            return self._diameter * (25.4 if self._units == 'imperial' else 1)
        else:
            return ValueError(f"{RED}Tool.diameter must be set (directly or indirectly) before it is referenced{ENDC}")

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        print(f";{YELLOW} Setting Tool Diameter: {self.diameter} mm | {self.diameter/25.4}\"{ENDC}")
