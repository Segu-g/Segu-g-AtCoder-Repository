versions = ["Ocelot", "Serval", "Lynx"]
x, y = input().split()
x_idx, y_idx = versions.index(x), versions.index(y)
if (x_idx >= y_idx):
  print("Yes")
else:
  print("No")
