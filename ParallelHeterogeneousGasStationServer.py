from random import seed
from random import randint
import time
# seed random number generator
seed(1)

def Empty(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1

def refill(arr,clock):
    clock=clock+arr[2]
    return clock


serial_no=0 #serial of customer
order=0   ##track serial
delivered=[]  ##to track delivary serial and time
sim_time=0  #simulation clock

arrival_time=0
customer_served=0
delay=0

station=[0,0,0]  #no of server=3
arr_vehicle=[]  #vehicle in main array[serial,arrival time,wash_time,vehicle_type]
gasrefilltime=0
vehicle_type=""


while(sim_time<=300):
    sim_time=sim_time+1
    print(f'When time is {sim_time} ->')
    if(sim_time%5==1): #1 person in 5 minutes
        serial_no=serial_no+1
        type_of_vehicle=randint(1,4)
        arrival_time=sim_time   
        if(type_of_vehicle==1): #smallcar
          gasrefilltime=10
          vehicle_type="Small Car"
        elif (type_of_vehicle==2): #small bus
           gasrefilltime=15
           vehicle_type="Small Bus"
        elif (type_of_vehicle==3): #big bus
           gasrefilltime=20
           vehicle_type="Big Bus"
        else: #big truck
           gasrefilltime=25;
           vehicle_type="Big Truck"
        val=(serial_no,arrival_time,gasrefilltime,vehicle_type)
        arr_vehicle.append(val)

         #print(f'When time is {sim_time} petrol station is idel->')  
         #print(f'When time is {sim_time} disel station is idel->')
    for i in range (0,3):
       if Empty(delivered):
        if (sim_time == delivered[0][0]):
            print(f'Serial NO {delivered[0][1]} has been delevered at {delivered[0][0]} .....')
            del delivered[0]
            customer_served=customer_served+1

    if Empty(arr_vehicle):
        for i in range (0,len(station)):
           if (station[i]<=sim_time) and Empty(arr_vehicle) :

             order=arr_vehicle[0][0]
             if (station[i] < arr_vehicle[0][1]):
                 station[i] = arr_vehicle[0][1]
             print(f"Vehicle No {order} is {arr_vehicle[0][3]} taken for gasrefill at {station[i]}.....")

             delay=delay+(station[i]-arr_vehicle[0][1])
            
             station[i]=refill(arr_vehicle[0], station[i])
             del arr_vehicle[0]
             print(f"Gasrefilling of Vehicle No {order} will be completed at {station[i]}.....")
             #print(f'petrol station is idel->')  
             #print(f'disel station is idel->')  
             # print(normalwash_time)
             val=(station[i],order)
             delivered.append(val)


             
    delivered.sort()


print(f'customer served: {customer_served}')
print(f'Delay: {delay}')