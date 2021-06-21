# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_number_list = list(map(int, input().split()))
room_numbers = list(set(room_number_list))
captains_room = (sum(room_numbers)*k - sum(room_number_list))//(k-1)
print (captains_room)
