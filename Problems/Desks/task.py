first_group_count = (int(input()))
second_group_count = (int(input()))
third_group_count = (int(input()))

first_group_count += first_group_count % 2
second_group_count += second_group_count % 2
third_group_count += third_group_count % 2

print(int((first_group_count + second_group_count + third_group_count) / 2))
