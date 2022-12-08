import csv
def find_marker(marker_length = 4):
    for characters in csv.reader(open('2022_Challenge_6/packet_marker_input.txt')):
        marker_info = characters[0]

    for marker in range(marker_length, len(marker_info)):
        four_set = marker_info[marker-marker_length:marker]

        if len(set(four_set)) == marker_length:
            return marker

print('The start of packet marker is :' , find_marker(4))
print('The start of message marker is :' , find_marker(14))