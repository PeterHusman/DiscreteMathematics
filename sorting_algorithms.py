import copy

def bubble_sort(input_list, rule=lambda x, y: x <= y):
	while True:		
		sorts = False		
		for i in range(len(input_list) - 1):		
			if not rule(input_list[i], input_list[i + 1]):
        		input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]		
        		sorts = True		
		if not sorts:		
			return input_list
			
def insertion_sort(input_list, rule=lambda x, y: x <= y):
	output_list = copy.deepcopy(input_list)
	for i in range(1, len(input_list)):
		j = i - 1
		while j != -1 and not rule(output_list[j], output_list[i]):
			j -= 1
		output_list = output_list[:(j + 1)] + [output_list[i]] + output_list[(j + 1):i] + output_list[(i + 1):]
	return output_list
