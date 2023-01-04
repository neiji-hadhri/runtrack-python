def triangle(a, b, c):
  if (a == b == c):
    print("ce triangle est équilatéral")
  elif ((a * a + b * b == round(c * c)) or (a * a + c * c == round(b * b)) or (c * c + b * b == round(a * a))) and ((round(a == b)) or (round(a == c)) or (round(c == b))):
    print("ce triangle est isocèle et rectangle")
  elif (a == b) or (a == c) or (c == b):
    print("ce triangle est isocèle")
  elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
    print("ce triangle est rectangle")
  elif a <= 0 or b <= 0 or c <= 0:
    print("ces dimensions ne representent pas un triangle,impossible de le contruire")
  else:
    print("ce triangle est quelconque.")


triangle(3, 3, 3)
triangle(3, 3, 5)
triangle(3, 4, 5)
triangle(2, 4, 3)
triangle(4, 4, 5.65685424949)
triangle(-2, 9, 3)