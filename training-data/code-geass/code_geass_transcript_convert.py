import os
import sys
import pandas

f = open("training-data\code-geass\code_geass_transcript.txt", encoding="utf8")
lines_stray_newlines = f.readlines()
f.close()

lines_raw = []
for line_raw in lines_stray_newlines:
    if line_raw != "\n":
        lines_raw.append(line_raw)

lines_newlines = []
lines_index = -1
for i in range(len(lines_raw)):
    line = lines_raw[i]
    if ":" in line:
        lines_newlines.append(line)
        lines_index += 1
    else:
        lines_newlines[lines_index] += line

lines_space = [line_newlines.replace("\n", " ") for line_newlines in lines_newlines]

lines = [line[:len(line)-1] for line in lines_space]

script_arr = [["name", "line"]]

lines_name = [line_name.split(":") for line_name in lines]

for line_name_pair in lines_name:
    script_arr.append(line_name_pair)

for j in range(len(script_arr)):
    if len(script_arr[j][0]) > 0:
        if script_arr[j][0][len(script_arr[j][0])-1] == " ":
            script_arr[j][0] = script_arr[j][0][:len(script_arr[j][0])-1]
    if script_arr[j][1][0] == " ":
        script_arr[j][1] = script_arr[j][1][1:]
    if script_arr[j][0] == "C.C":
        script_arr[j][0] = "C.C."
    if script_arr[j][0] == "V.V":
        script_arr[j][0] = "V.V."

counter = 0
for name in script_arr:
    if name[0] == "Nunnally":
        counter += 1

print(counter)

""" csv_str = ""
for k in range(len(script_arr)):
    csv_str += str(script_arr[k][0])
    csv_str += ";"
    csv_str += str(script_arr[k][1])
    csv_str += "\n"

g = open("code_geass_transcript.csv", 'w', encoding="utf8")
g.write(csv_str)
g.close() """

