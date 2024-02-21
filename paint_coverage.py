import math
def get_dimensions(height,width,coverage_per_can):

    area_of_your_wall=height*width
    print(area_of_your_wall)
    num_of_cans_req=math.ceil(area_of_your_wall/coverage_per_can)


    print(num_of_cans_req)
cover=7
height=int(input("Enter height of wall in meters"))
width=int(input("Enter width of wall in meters"))
get_dimensions(height,width,coverage_per_can=cover)
