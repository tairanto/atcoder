#!/usr/bin/python3
n=input()
if 0<int(n[:2])<13 and 0<int(n[2:])<13:
    print("AMBIGUOUS")
elif (int(n[:2])==0 or int(n[:2])>12) and 0<int(n[2:])<13:
    print("YYMM")
elif 0<int(n[:2])<13 and (int(n[2:])==0 or  int(n[2:])>12):
    print("MMYY")
else:
    print("NA")
