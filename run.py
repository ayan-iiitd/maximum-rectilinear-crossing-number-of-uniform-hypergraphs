import code1_convert_hex_to_int as code_1
import code2_generate_feasible_points as code_2
import code3_check_for_balanced_set as code_3
import code4_1_check_for_ptset_details_where_max_feasible_colorings_is_12 as code_4_1
import code4_2_check_for_max_balanced_colors_without_M_or_I_aka_neighbourly_polytopes as code_4_2
import datetime

print ("Execution started at\t", datetime.datetime.now())
code_1.run()
print ("\n\nConversion of hexadecimal to integer completed at\t", datetime.datetime.now(), '\n\n\nStarting to check point sets for feasibility.')
code_2.run()
print ("\n\nChecking point sets for feasibility finished at\t", datetime.datetime.now(), '\n\n\nStarting to check for balanced, monochrome and imbalanced colors.')
code_3.run()
print ("\n\nChecking for balanced, monochrome and imbalanced colors finished at\t", datetime.datetime.now(), '\nStarting to check for details of point sets with maximum umber of balanced feasible colorings.')
code_4_1.run()
print ("\n\nChecking for details of point sets with maximum umber of balanced feasible colorings finished at\t", datetime.datetime.now(), '\nStarting to check for neighboourly polytopes where.')
code_4_2.run()