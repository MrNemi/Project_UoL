import math

class coord_handler:
    def __init__(self, start_pick_position: list, number_pick_positions :int, start_set_position :list, number_set_position : int):
        self.init = self.init()
       
        self.pick_start_position = start_pick_position
        self.set_start_position = start_set_position
        self.pick_positions = self._get_pick_positions(number_pick_positions)
        self.set_positions = self._get_set_positions(number_set_position)

    def _get_pick_positions(self, number_pick_positions):
        # Initialize the list to store pick positions
        pick_positions = []
        pick_positions.append(self.pick_start_position)  # Add the start pick position

        # Calculate subsequent pick positions based on a 4x2 grid
        row_offset = 0  # Start at the first row
        column_offset = 0  # Start at the first column

        for i in range(1, number_pick_positions):
            # Assuming a simple offset of 1 for the sake of example.
            # You can customize how to calculate the offset here
            new_position = self._calculate_new_position(self.pick_start_position, row_offset, column_offset, grid_type="pick")
            pick_positions.append(new_position)

            # Move to the next column, and if we reach the end of columns, move to the next row
            column_offset += 1
            if column_offset == 2:  # If there are 2 columns, reset to the first column and move to the next row
                column_offset = 0
                row_offset += 1
        
        return pick_positions
    

    def _get_set_positions(self, number_set_position):
        # Initialize the list to store set positions
        set_positions = []
        set_positions.append(self.set_start_position)  # Add the start set position

        # Calculate subsequent set positions based on a 4x1 grid (single column, multiple rows)
        row_offset = 1  # Start from the next row after the starting position

        for i in range(1, number_set_position):
            # Assuming a simple offset of 1 for the sake of example.
            # You can customize how to calculate the offset here
            new_position = self._calculate_new_position(self.set_start_position, row_offset, 0, grid_type="set")
            set_positions.append(new_position)

            # Move to the next row
            row_offset += 1
        
        return set_positions


    def _calculate_new_position(self, start_position, row_offset, col_offset, grid_type):
        # Logic for calculating new position based or even 
        new_position = start_position.copy()  # Start with the current position

        # Apply some offset based on whether it's a pick or set position
        if grid_type == "pick":
            # Modify based on even or odd index
            if index % 2 == 0:
                new_position[0] += row_offset # Example offset on x-axis for even index
            else:
                new_position[1] += col_offset  # Example offset on y-axis for odd index
        elif grid_type == "set":
            # For the set grid, the positions are 4x1, so only row changes
            new_position[0] += row_offset  # Modify x-axis based on row offset (for a vertical grid)

        return new_position