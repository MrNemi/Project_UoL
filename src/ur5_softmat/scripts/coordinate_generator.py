

class coord_handler:
    def __init__(self, start_pick_position: list  , number_pick_positions :int , start_set_position :list , number_set_position : int):
        self.init = self.init()
       
        self.pick_start_position = start_pick_position
        self.set_start_position = start_set_position
        self.pick_positions = self._get_pick_positions()
        self.set_positions = self._get_set_positions()

        # Origin positions for vial racks
        self.rack1_origin = []
        self.rack0_origin = []
        self.base_position = []

        col_space = 0.0035  # Convert mm to meters
        row_space = 0.044  # Convert mm to meters
        num_rows = 4; num_col = 2

    # rIndex: 0 or 1
    # vIndex: 0-7 for rack 0, 0-3 for rack 1

    def _get_pick_positions(self, vIndex: int, rIndex: int):
        ## do the pick position code here
        ## this should be an array of number_pick_positions (each element is a 6 element list) with all those on the LEFT as even indexes
        pick_positions = []
        
        if rIndex == 0:
            print("Geting coordinates for picking vial from sample rack")
            rackPosX = 0
            rackPosY = 0
            rackPosZ_grasp = self.rack0_origin[2]
            rackPosZ_lift = self.rack0_origin[2] + 80
            if vIndex < 4:
                rackPosX = self.rack0_origin[0] + (vIndex * 26.6)
                rackPosY = self.rack0_origin[1]
            elif vIndex >= 4 and vIndex < 8:
                rackPosX = self.rack0_origin[0] + ((vIndex - 4) * 26.6)
                rackPosY = self.rack0_origin[1] + 45
            else:
                print("Invalid Vial Index!")

            """Returns the picking coordinates based on the number_pick_position."""
            try:
                return pick_positions[vIndex]
            except IndexError:
                raise ValueError("Invalid index for vial pick coordinates.")
    

    def _get_set_positions(self, vIndex: int, rIndex: int):
        ## do the set position code here
        ## this should be an array of number_set_positions (each element is a 6 element list) with the set positions
        set_positions = []

        if rIndex == 1:
            print("geting coordinates for setting vial in place rack")
            rackPosX = 0
            rackPosY = 0
            rackPosZ_grasp = self.rack0_origin[2]
            rackPosZ_lift = self.rack0_origin[2] + 80
            if vIndex < 4:
                rackPosX = self.rack0_origin[0] + (vIndex * 26.6)
                rackPosY = self.rack0_origin[1]
            elif vIndex >= 4 and vIndex < 8:
                rackPosX = self.rack0_origin[0] + ((vIndex - 4) * 26.6)
                rackPosY = self.rack0_origin[1] + 45
            else:
                print("Invalid Vial Index!")

            """Returns the placing coordinates based on the number_set_position."""
            try:
                return set_positions[vIndex]
            except IndexError:
                raise ValueError("Invalid index for vial placing coordinates.")