##x="https://www.google.co.in/search?q=how+r+u&oq=how+r++u&aqs=chrome.0.0l6.2225j0j7&sourceid=chrome&ie=UTF-8"
##y="https://www.google.co.in/search?q=how%2Br%2Bu&oq=how%2Br%2Bu&aqs=chrome..69i57j0l5.514j0j7&sourceid=chrome&ie=UTF-8"
##
##if x==y:
##    print "true"
##
##else:
##    print "false"
##print " bye "
##
##for i in range(1,4):
##    
##    def rental_car_cost(days):
##        if(days <3):
##        
##           return 40*days;
##    
##        elif (days >=3 and days <7):
##            return (days*40)-20;
##        
##        else:
##            return  (days*40)-50;
##        
##
##    days=int(raw_input("enter the number of days : "))
##
##    print rental_car_cost(days);
##


def hotel_cost(nights):
    return 140*nights;
    
def plane_ride_cost(city):
    if (city=="Charlotte"):
        return 183;
    elif  (city=="Tampa"):
        return 220;
    elif (city=="Pittsburgh"):
        return 222;
    else :
        return 475;
        
def rental_car_cost(days):
        if(days <3):
        
           return 40*days;
    
        elif (days >=3 and days <7):
            return (days*40)-20;
        
        else:
            return  (days*40)-50;
        
def trip_cost(city, days):
    sum= rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city);
    return sum

print trip_cost("Tampa",4)
