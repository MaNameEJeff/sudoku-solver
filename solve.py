import math
from smallBox import smallBox
from getNumbers import getNumbers

grid_rows = {
	'Row 1': ['*', '*', '*', '5', '8', '9', '*', '*', '*'],
	'Row 2': ['*', '*', '9', '*', '3', '6', '*', '*', '4'],
	'Row 3': ['*', '5', '8', '4', '1', '*', '*', '*', '*'],
	'Row 4': ['4', '7', '*', '*', '*', '*', '*', '2', '9'],
	'Row 5': ['3', '*', '*', '*', '*', '*', '*', '*', '5'],
	'Row 6': ['5', '9', '*', '*', '*', '*', '*', '1', '7'],
	'Row 7': ['*', '*', '*', '*', '5', '7', '2', '4', '*'],
	'Row 8': ['8', '*', '*', '6', '9', '*', '7', '*', '*'],
	'Row 9': ['*', '*', '*', '3', '2', '8', '*', '*', '*']
}

small_boxes_numbers = {
	"11": [],
	"12": [],
	"13": [],
	"21": [],
	"22": [],
	"23": [],
	"31": [],
	"32": [],
	"33": [],
}

small_boxes = {}
grid = []
not_completed = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for key, value in grid_rows.items():
	grid.append(value)

def update_not_completed():
	for number in not_completed:

		flag = True

		for box in small_boxes:
			if(small_boxes[box].has(number) == False):
				flag = False

		if flag:
			not_completed.remove(number)

def make_small_boxes():	

	for row in range(1, 10):
		arg1 = math.ceil(row/3)

		for column in range(1, 10):

			arg2 = math.ceil(column/3)
			args = str(arg1) + str(arg2)
			small_boxes_numbers[args].append(grid[row-1][column-1])

	for k, v in small_boxes_numbers.items():
		small_boxes[k] = smallBox(k, v)

def solve_puzzle():

	digit = not_completed[0]
	unfilled_boxes = []

	number_in = {
		"11": small_boxes["11"].has(digit),
		"12": small_boxes["12"].has(digit),
		"13": small_boxes["13"].has(digit),
		"21": small_boxes["21"].has(digit),
		"22": small_boxes["22"].has(digit),
		"23": small_boxes["23"].has(digit),
		"31": small_boxes["31"].has(digit),
		"32": small_boxes["32"].has(digit),
		"33": small_boxes["33"].has(digit)
	}

	for location, value in number_in.items():
		if(value == False):
			unfilled_boxes.append(small_boxes[location])

	slots = unfilled_boxes[2].get_empty()
	print(unfilled_boxes[2].location)
	print(slots)
	row_col_of_box = (int(unfilled_boxes[2].location[0]), int(unfilled_boxes[2].location[1]))

	#Check columns
	boxes_to_check_y = []

	if ((row_col_of_box[0] - 1) != 0):
		boxes_to_check_y.append(((row_col_of_box[0] - 1), row_col_of_box[1]))

	if ((row_col_of_box[0] + 1) < 4):
		boxes_to_check_y.append(((row_col_of_box[0] + 1), row_col_of_box[1]))

	#Check rows
	boxes_to_check_x = []
	if ((row_col_of_box[1] - 1) != 0):
		boxes_to_check_x.append((row_col_of_box[0], (row_col_of_box[1] - 1)))

	if ((row_col_of_box[1] + 1) < 4):
		boxes_to_check_x.append((row_col_of_box[0], (row_col_of_box[1] + 1)))

	print(boxes_to_check_x)
	print(boxes_to_check_y)

if __name__ == '__main__':
	make_small_boxes()
	solve_puzzle()