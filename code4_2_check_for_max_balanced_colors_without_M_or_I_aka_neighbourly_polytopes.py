import os
import pandas

def run():
	
	for file_no in range(1, 3316):
		
		file_name = "./feasible_point_sets_with_color_check/point_set_" + str(file_no) + "_with_color_check.csv"

		## Sometimes when reading directly from a directory, Python converts the file names to byte strings, so a conversion to UTF-8 before they can be worked with is neccesary
		if (type(file_name) == 'bytes'):
			feasible_ptset = pandas.read_csv(file_name.decode('utf-8'))
		else:
			feasible_ptset = pandas.read_csv(file_name)
		
		pointset_details = pandas.DataFrame()
		
		for col_name in list(feasible_ptset.columns)[:4]:
			pointset_details[col_name] = feasible_ptset[col_name].values
			
			size_of_all_feasible_sets = feasible_ptset['Feasible_Set_Size'].values.tolist()

		required_colors = ['00001111', '00010111', '00011011', '00011101', '00011110', '00100111', '00101011', '00101101', '00101110', '00110011', '00110101', '00110110', '00111001', '00111010', '00111100', '01000111', '01001011', '01001101', '01001110', '01010011', '01010101', '01010110', '01011001', '01011010', '01011100', '01100011', '01100101', '01100110', '01101001', '01101010', '01101100', '01110001', '01110010', '01110100', '01111000', '10000111', '10001011', '10001101', '10001110', '10010011', '10010101', '10010110', '10011001', '10011010', '10011100', '10100011', '10100101', '10100110', '10101001', '10101010', '10101100', '10110001', '10110010', '10110100', '10111000', '11000011', '11000101', '11000110', '11001001', '11001010', '11001100', '11010001', '11010010', '11010100', '11011000', '11100001', '11100010', '11100100', '11101000', '11110000']
	
		for color in required_colors:

			one_side_color = feasible_ptset[color].values.tolist()
			monochrome_found = 0
			
			for index in range(0, len(size_of_all_feasible_sets)):
				
				## Checking if a monochrome exists for 2 sets and 3 sets and if a monochrome or imbalanced coloring is found for 4 sets
				if size_of_all_feasible_sets[index] == 2 or size_of_all_feasible_sets[index] == 3:
					if ('M' in one_side_color[index]):
						monochrome_found = 1
						break
				elif size_of_all_feasible_sets[index] == 4:
					if ('M' in one_side_color[index] or 'I' in one_side_color[index]):
						monochrome_found = 1
						break
			
			if monochrome_found == 0:
				pointset_details[color] = feasible_ptset[color].values
				
		if (len(pointset_details.columns) > 4):
			
			if not os.path.exists('./max_feasible_without_M_or_I'):
				os.makedirs('./max_feasible_without_M_or_I')

			pointset_details.to_csv('max_feasible_without_M_or_I/Balanced_Set_' + str(file_no) + '.csv', sep = ',', index = False)


if __name__== "__main__":
	run()