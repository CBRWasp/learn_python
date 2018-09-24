score_list = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5a', 'scores': [5,4,5,5,3]}, {'school_class': '6a', 'scores': [2,5,3,3,4]}]
all_sum = 0
class_sum = 0
avg_sum = 0

for class_ in score_list:
	class_sum = 0	
	for x in class_['scores']:
		class_sum += x

	avg_class =  class_sum / float(len(class_['scores']))
	avg_sum += avg_class
	print('In :', class_['school_class'], ' average score is', avg_class)
	
	all_sum += class_sum

all_sum = avg_sum / float(len(score_list))

avg_school = float('{:.2f}'.format(all_sum))
print('School average score is: ', avg_school)
