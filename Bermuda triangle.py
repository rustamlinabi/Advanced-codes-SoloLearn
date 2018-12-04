"""
The code takes 2 random points on the edges of the "ocean". Then it generates a Bermuda triangle in the middle of the ocean. Then it calculates if the route passes through Bermuda triangle. Then it calculates the distance it travels through the triangle. Finally, it calculates if the ship travels safely to its destination or disappears in the triangle. The size of the ocean can be changed on line 30.
"""
import math, random


# This function finds the area of the triangle
def area(sides):
    t = sum(sides) / 2
    ar = math.sqrt(t * (t - sides[0]) * (t - sides[1]) * (t - sides[2]))
    return ar


# This function finds the slope of the line between two points
def linepar(a, b):
    k_ab = (b[1] - a[1]) / (b[0] - a[0])
    b_ab = b[1] - k_ab * b[0]
    par_ab = [k_ab, b_ab]
    return par_ab


# This function checks whether two lines cross and if they do it returns their crossing point
def cross(a, b, c, d):
    l = linepar(a, b)
    tr = linepar(c, d)
    xero = (tr[1] - l[1]) / (l[0] - tr[0])
    yero = xero * l[0] + l[1]
    if xero < max(a[0], b[0]) and xero > min(a[0], b[0]) and yero < max(a[1], b[1]) and yero > min(a[1], b[1]):
        return [xero, yero]
    else:
        return False


# This function return the length of line between two points
def lenline(a, b):
    return math.sqrt((abs(a[0] - b[0])) ** 2 + (abs(a[1] - b[1])) ** 2)


# Size of the ocean and parameters of the triangle
w = 250
while True:
    try:
        a = [random.randint(0, w), random.randint(0, w)]
        b = [random.randint(0, w), random.randint(0, w)]
        c = [random.randint(0, w), random.randint(0, w)]
        trsides = [lenline(a, b), lenline(a, c), lenline(b, c)]
        are = area(trsides)
        if are > (0.3) * w * w and are < (0.49) * w * w:
            break
        else:
            continue
    except:
        continue

trsides = [lenline(a, b), lenline(a, c), lenline(b, c)]
dep = [0, 0]
arr = [0, 0]
while True:
    dep[0] = random.randint(0, w)
    dep[1] = random.randint(0, w)
    arr[0] = random.randint(0, w)
    arr[1] = random.randint(0, w)
    t = True
    coo = [0, w]
    for x in dep:
        for z in arr:
            if x in coo and z in coo:
                if x != z:
                    t = False
                    break
                else:
                    continue
            else:
                continue
    if t == False:
        break
print("The ship departs from point", dep, "for the destination at", arr, "\n ~~~~~~~~~~~~ ")
print("The ocean is", w, "by", w, "kilometers \n ~~~~~~~~~~~~ ")
print("The Bermuda triangle covers", round(area(trsides), 3), "square kilometers, which is around",
      round((area(trsides) * 100) / (w * w), 1), "% of the whole ocean\n ~~~~~~~~~~~~ ")
test = [cross(a, b, dep, arr), cross(b, c, dep, arr), cross(a, c, dep, arr)]

t = 0
intersect = []
for a in test:
    if a == False:
        continue
    else:
        t += 1
        intersect.append(a)
if t > 0:
    print("Travel route crosses through Bermuda triangle\n ~~~~~~~~~~~~ ")
    r1 = intersect[0];
    r2 = intersect[1]
    lenroute = lenline(r1, r2)
    print("The ship travels", round(lenroute, 2), "kilometers in Bermuda\n ~~~~~~~~~~~~ ")
    if lenroute > 0 and lenroute < (0.3 * w):
        print("The travel in triangle is not very long\n ~~~~~~~~~~~~ ")
    elif lenroute > (0.3 * w) and lenroute < (0.6 * w):
        print("The travel in triangle is long\n ~~~~~~~~~~~~ ")
    elif lenroute > (0.6 * w) and lenroute < (0.9 * w):
        print("The travel in triangle is very long, it is very difficult to survive\n ~~~~~~~~~~~~ ")
    else:
        print("The travel in triangle is really long, it would be a miracle to survive it\n ~~~~~~~~~~~~ ")
    prob = lenroute * 0.9
    if random.randrange(w) < prob:
        print("The ship, unfortunately, disappeared")
    else:
        print("The ship safely arrives at destination")
else:
    print("Travel route does NOT cross through Bermuda triangle, the ship safely arrives at destination")