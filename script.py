#Define destinations list
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']
#Define a traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Testing the function
#print(get_destination_index('Los Angeles, USA'))
#print(get_destination_index('Paris, France'))
#print(get_destination_index('Hyderabad, India')) # Value Error is returned as expected TODO: Add an error handler

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#Testing get_traveler_location function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)