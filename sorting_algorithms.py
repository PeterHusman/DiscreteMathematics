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
	for i in range(1, len(input_list[:])):
		j = i - 1
		while not rule(input_list[i], input_list[j]):
			j -= 1
