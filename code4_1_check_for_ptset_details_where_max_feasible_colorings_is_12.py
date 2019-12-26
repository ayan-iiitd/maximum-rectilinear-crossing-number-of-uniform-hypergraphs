import os
import pandas

def run():

	for file_no in range(1, 3316):
		
		file_name = "./feasible_point_sets_with_color_check/point_set_" + str(file_no) + "_with_color_check.csv"
		point_set_details = pandas.DataFrame()

		## Sometimes when reading directly from a directory, Python converts the file names to byte strings, so a conversion to UTF-8 before they can be worked with is neccesary
		if (type(file_name) == 'bytes'):
			feasible_ptset = pandas.read_csv(file_name.decode('utf-8'))
		else:
			feasible_ptset = pandas.read_csv(file_name)
			
		## Checking if the maximum number of balanced color configurations is twelve for all possible colorings of a point set.
		if (list(feasible_ptset.iloc[-1])[4] == '12'):
		
			point_set_details['PointSet'] = feasible_ptset['PointSet']
			point_set_details['Feasible_Set_Size'] = feasible_ptset['Feasible_Set_Size']
			point_set_details['Feasible_Set_Indices'] = feasible_ptset['Feasible_Set_Indices']
			point_set_details['Feasible_Set_Points'] = feasible_ptset['Feasible_Set_Points']
			found_flag = 0
	
			required_colors = ['00001111', '00010111', '00011011', '00011101', '00011110', '00100111', '00101011', '00101101', '00101110', '00110011', '00110101', '00110110', '00111001', '00111010', '00111100', '01000111', '01001011', '01001101', '01001110', '01010011', '01010101', '01010110', '01011001', '01011010', '01011100', '01100011', '01100101', '01100110', '01101001', '01101010', '01101100', '01110001', '01110010', '01110100', '01111000', '10000111', '10001011', '10001101', '10001110', '10010011', '10010101', '10010110', '10011001', '10011010', '10011100', '10100011', '10100101', '10100110', '10101001', '10101010', '10101100', '10110001', '10110010', '10110100', '10111000', '11000011', '11000101', '11000110', '11001001', '11001010', '11001100', '11010001', '11010010', '11010100', '11011000', '11100001', '11100010', '11100100', '11101000', '11110000']
	
			for color in required_colors:
				one_side_color = feasible_ptset[color].values.tolist()
				
				## Checking if a particular color has a total of twelve balanced colorings
				if (one_side_color[-2] == '12'):
					found_flag = 1
					point_set_details[color] = feasible_ptset[color]
				
			if not os.path.exists('./12_balanced_colors'):
				os.makedirs('./12_balanced_colors')
			
			if found_flag == 1:
				point_set_details.to_csv('12_balanced_colors/' + str(file_no) + '.csv', sep = ',', index = False)
		
if __name__== "__main__":
	run()