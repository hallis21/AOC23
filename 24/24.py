lines = [x.strip() for x in open("24").readlines()]

# x and y min / max
bounds = (200000000000000, 400000000000000)
coooords = []
hails = []
for l in lines:
    p = l.split(" @ ")
    coords = tuple([int(x) for x in p[0].split(", ")])
    vel = tuple([int(x) for x in p[1].split(", ")])

    hails.append((coords, vel))









exit()
import math

def calculate_intersection(point1, velocity1, point2, velocity2):
    # Convert velocities to angles
    angle1 = math.atan2(velocity1[1], velocity1[0])
    angle2 = math.atan2(velocity2[1], velocity2[0])

    # Calculate slopes (m = tan(angle))
    m1 = math.tan(angle1)
    m2 = math.tan(angle2)

    # Calculate y-intercepts (c = y - mx)
    c1 = point1[1] - m1 * point1[0]
    c2 = point2[1] - m2 * point2[0]

    # Check if the lines are parallel
    if m1 == m2:
        return None  # No intersection

    # Calculate intersection point (x = (c2 - c1) / (m1 - m2), y = m1 * x + c1)
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1


    return (x, y)


valid_intersections = []

for i,hail1 in enumerate(hails):
    for i2,hail2 in enumerate(hails[i+1:]):
        if hail1 == hail2:
            continue

        result = calculate_intersection(hail1[0], hail1[1], hail2[0], hail2[1])
        
        if result:
            valid = True
            # print(f"The points intersect at {result} at time t.")

            if result[0] < bounds[0] or result[0] > bounds[1] or result[1] < bounds[0] or result[1] > bounds[1]:
                # print("The points intersect outside the bounds.")
                valid = False
            
            # If the intersection point is greater than the x or y
            # Check if the velocity allows it to reach the intersection point
            # If it does not, then the intersection point is in the past
                
            if hail1[0][0] < result[0] and hail1[1][0] < 0:
                # print("The first point does not reach the intersection point.")
                valid = False
            if hail1[0][0] > result[0] and hail1[1][0] > 0:
                # print("The first point does not reach the intersection point.")
                valid = False
            if hail1[0][1] < result[1] and hail1[1][1] < 0:
                # print("The first point does not reach the intersection point.")
                valid = False
            if hail1[0][1] > result[1] and hail1[1][1] > 0:
                # print("The first point does not reach the intersection point.")
                valid = False

            if hail2[0][0] < result[0] and hail2[1][0] < 0:
                # print("The second point does not reach the intersection point.")
                valid = False
            if hail2[0][0] > result[0] and hail2[1][0] > 0:
                # print("The second point does not reach the intersection point.")
                valid = False
            if hail2[0][1] < result[1] and hail2[1][1] < 0:
                # print("The second point does not reach the intersection point.")
                valid = False
            if hail2[0][1] > result[1] and hail2[1][1] > 0:
                # print("The second point does not reach the intersection point.")
                valid = False


            if valid:
                valid_intersections.append(result)
        else:
            pass
            # print("The points do not intersect.")

print(len(set(valid_intersections)))